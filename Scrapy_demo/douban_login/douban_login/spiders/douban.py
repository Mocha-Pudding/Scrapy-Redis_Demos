# -*- coding: utf-8 -*-
import scrapy
from urllib import request
from PIL import Image

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://accounts.douban.com/passport/login']
    login_url = 'https://accounts.douban.com/passport/login'

    def parse(self, response):
        formdata = {
            'source': 'None',
            'redir':'https://www.douban.com/',
            'form_email':'253496831@qq,com',
            'form_password':'pythonspider',
            'remember':'on',
            'login':'登录'
        }
        captcha_url = response.css('img#captcha_image:attr(src)').get()
        # print('='*60)
        # print(captcha_img)
        if captcha_url:
            captcha = self.recognize_captcha(captcha_url)
            formdata['captcha-solution'] = captcha
            captcha_id = response.xpath("//input[@name='captcha-id']/@value").get()
            formdata['captcha-id'] = captcha_id
        yield scrapy.FormRequest(url=self.login_url,formdata=formdata,callback=self.parse_after_login)

    def parse_after_login(self, response):
        if response.url == 'https://www.douban.com/':
            print('登录成功！')
        else:
            print('登录失败！')

    def recognize_captcha(self,image_url):
        request.urlretrieve(image_url, 'captcha.png')
        image = Image.open('captcha.png')
        image.show()
        captcha = input('请输入验证码：')
        return captcha
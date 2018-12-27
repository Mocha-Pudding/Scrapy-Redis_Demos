# 继承自threading.Thread类：
# 为了让线程代码更好的封装。可以使用threading模块下的Thread类，继承自这个类，然后实现run方法，线程会自动运行run方法

import threading
import time

#定义线程类 CodingThread
class CodingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print('正在写代码%s' % threading.current_thread())
            # threading.current_thread()是当前线程的名称
            time.sleep(1)

#定义线程类 DrawingThread
class DrawingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print('正在画图%s' % threading.current_thread())
            time.sleep(1)

def main():
    t1 = CodingThread()   #通过创建对象的方式来创建一个线程
    t2 = DrawingThread()

    t1.start()
    t2.start()

if __name__ == '__main__':
    main()
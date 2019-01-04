# Lock版本生产者和消费者模式

import threading
import random
import time

gMoney = 1000
gLock = threading.Lock()
gTotalTimes = 10
gTimes = 0

# 生产者类 (不断生产money)
class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTimes
        while True:    # 使用while true死循环来不断生产
            money = random.randint(100,1000)
            gLock.acquire()
            if gTimes >= gTotalTimes:
                gLock.release()
                break
            gMoney += money
            print("%s生产了%d元钱，剩余%d元钱" %(threading.current_thread(), money, gMoney))
            gTimes += 1
            gLock.release()
            time.sleep(0.5)

# 消费者类 (断消费money)
class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(100,1000)
            gLock.acquire()
            if gMoney >= money:
                gMoney -= money
                print("%s消费了%d元钱,剩余%d元钱" %(threading.current_thread(), money, gMoney))
            else:
                if gTimes >= gTotalTimes:
                    gLock.release()
                    break
                print("%s消费者准备消费%d元钱，剩余%d元钱，余额不足！"%(threading.current_thread(), money, gMoney))
            gLock.release()
            time.sleep(0.5)

def main():
    for x in range(5):
        t = Consumer(name="消费者线程%d"%x)   #指定进程的名字
        t.start()

    for x in range(5):
        t = Producer(name="生产者线程%d"%x)   #指定进程的名字
        t.start()

if __name__ == '__main__':
    main()
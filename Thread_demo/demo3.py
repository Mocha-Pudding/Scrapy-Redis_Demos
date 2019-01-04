# 多线程共享全局变量的问题 以及锁机制

import threading

VALUE = 0

gLock = threading.Lock()   #创建锁

def add_value():
    global VALUE      #使用全局变量，需要用global关键字来声明
    gLock.acquire()   #上锁
    for x in range(1000000):
        VALUE += 1
    gLock.release()   #释放锁
    print('value: %d'  %VALUE)

def main():
    for x in range(3):
        t = threading.Thread(target=add_value)
        t.start()

if __name__ == '__main__':
    main()
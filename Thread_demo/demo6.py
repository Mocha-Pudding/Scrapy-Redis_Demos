# Queue线程安全队列：

# 在线程中，访问一些全局变量，加锁是一个经常的过程。如果你是想把一些数据存储到某个队列中，那么Python内置了一个线程安全的模块叫做queue模块。Python中的queue模块中提供了同步的、线程安全的队列类，包括FIFO（先进先出）队列Queue，LIFO（后入先出）队列LifoQueue。这些队列都实现了锁原语（可以理解为原子操作，即要么不做，要么都做完），能够在多线程中直接使用。可以使用队列来实现线程间的同步。相关的函数如下：
#
# 初始化Queue(maxsize)：创建一个先进先出的队列。
# qsize()：返回队列的大小。
# empty()：判断队列是否为空。
# full()：判断队列是否满了。
# get()：从队列中取最后一个数据。
# put()：将一个数据放到队列中。

from queue import Queue
import time
import threading

# q = Queue(4)       # 初始化Queue(maxsize)：创建一个先进先出的队列。
# q.put(1)           # put()：将一个数据放到队列中。
# q.put(2)
# for x in range(2):
#     q.put(x)
#
# print(q.full())     # full()：判断队列是否满了。
# print(q.empty())    # empty()：判断队列是否为空。
# print(q.qsize())    # qsize()：返回队列的大小。
# print(q.get())

def set_value(q):
    index = 0
    while True:
        q.put(index)
        index += 1
        time.sleep(3)

def get_value(q):
    while True:
        print(q.get())

def main():
    q = Queue(4)
    t1 = threading.Thread(target=set_value, args=[q])
    t2 = threading.Thread(target=get_value, args=[q])

    t1.start()
    t2.start()

if __name__ == '__main__':
    main()
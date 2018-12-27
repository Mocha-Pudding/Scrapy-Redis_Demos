# 多线程共享全局变量的问题

import threading

VALUE = 0

def add_value():
    global VALUE
    for x in range(1000):
        VALUE += 1
    print('value: %d'  %VALUE)

def main():
    for x in range(3):
        t = threading.Thread(target=add_value)
        t.start()

if __name__ == '__main__':
    main()
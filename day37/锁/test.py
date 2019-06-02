from multiprocessing import Lock, Process
import json
import time
import os, sys

def buy_ticket(i, lock):
    lock.acquire()
    with open(r'D:\python\day37\锁\ticket') as f:
        dic = json.load(f)
        if dic['ticket'] > 0:
            print('%s买到票了' % i)
            dic['ticket'] -= 1
        else:
            print('%s没买到票' % i)
    time.sleep(1)
    with open(r'D:\python\day37\锁\ticket', 'w') as f:
        json.dump(dic, f)
    lock.release()


if __name__ == '__main__':
    print(os.getcwd())
    lock = Lock()
    p_list = []
    for i in range(5):
        p = Process(target=buy_ticket, args=(i, lock))
        p.start()
        p_list.append(p)
    [p.join() for p in p_list]
    dic = {}
    dic['ticket'] = 3
    with open(r'D:\python\day37\锁\ticket', 'w') as f:
        json.dump(dic, f)
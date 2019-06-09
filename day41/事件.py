from threading import Thread, Event
import time
import random


def conn_db(e):
    count = 0
    while count < 3:
        e.wait(3)  # 阻塞状态下只停留一面
        if e.is_set() == True:
            print('链接数据库')
            break
        else:
            count += 1
            print('第%s次链接失败' % count)
    else:  # 当while没有被break时，将会执行这行代码
        raise TimeoutError('链接超时')


def check_conn(e):
    time.sleep(random.randint(0, 3))
    e.set()
    print('网络正常')


e = Event()
Thread(target=conn_db, args=(e, )).start()
Thread(target=check_conn, args=(e, )).start()

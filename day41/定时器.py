from threading import Timer
import time


def func():
    print('time')


while True:
    Timer(5, func).start()
    time.sleep(5)
from multiprocessing import Pool


def func1(n):
    print('in func1')
    return n * n


def func2(nn):
    print('in func2')
    print(nn)


if __name__ == '__main__':
    p = Pool(5)
    # 回调函数将进程池的函数返回值，当做回调参数的参数执行，和进程池中的函数不在一个进程
    for i in range(10):
        p.apply_async(func1, args=(i, ), callback=func2)
    p.close()
    p.join()
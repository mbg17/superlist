from multiprocessing import Pool


def func(n):
    return n * n


if __name__ == '__main__':
    p = Pool(5)
    for i in range(10):
        # 需要关闭进程池后获取结果
        ret = p.apply_async(func, args=(i, ))
        # 等待函数执行完毕后获取结果 返回当前函数的结果
        print(ret.get())
    res = p.map(func, range(10))
    # 以列表的方式返回所有结果
    print(res)
    for i in range(10):
        ret = p.apply(func, args=(i, ))
        # 直接返回当前函数的结果
        print(ret)

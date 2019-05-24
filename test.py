def test():
    for i in range(10):
        yield i

i = test()
s=i.__next__()
print(s)
for x in i:
    print(x)

# callable 检查函数是否可调用
# 可调用返回True 不可调用返回 False

# yield 生成器 惰性调用
# 可迭代协议 包含__iter__()函数
# 迭代器包含 __iter__()和__next__()函数

# help() 返回用""""""中的备注

# id 内存地址
# hash 可哈希不可迭代 不可哈希可迭代

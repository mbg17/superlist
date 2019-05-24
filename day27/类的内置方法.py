# 内置的类方法
# 双下方法
# print()方法方法默认调用str方法 对象.__str__方法
# 可以用%s 格式化字符串


class A:
    def __init__(self):
        self.li = [1, 1, 1, 1, 1, 1, 1]

    # 自定义输出的内容
    # 只能返回字符串类型的值
    # def __str__(self):
    #     return "A's object"

    def func(self):
        return 'func'

    # repr 和 %r 都是走的该方法
    # repr 是str的备胎 如果%s str 找不到__str__ 就会找__repr__
    # 反过来不行
    def __repr__(self):
        return 'a'

    # 调用len() 执行该方法
    # 只能返回int类型
    def __len__(self):
        return 100

    # 执行先执行这个函数，在删除了这个变量
    # 程序结束后也会执行这个函数了
    # 内部有一个引用计数的机制
    def __del__(self):  # 析构函数
        print('执行del')

    # call方法
    # 对象() 执行了该方法
    def __call__(self):
        print('执行我了')


# 可以直接用 str() 打印 格式化字符串低啊用·调用__str__
a = A()
print('%s' % a, len(a))  # 调用__str__方法
print(str(a))
a.__call__()
del a  # 先执行了内置的__del__方法再删除变量 ，所以下面的函数会报错，通常用来执行函数的收尾工作
print(a.__dict__)

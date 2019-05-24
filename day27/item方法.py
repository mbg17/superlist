# item 双下方法
# 操作方式类似字典
class Foo:
    def __init__(self):
        self.name = 'luyuan'
        self.age = 12
        self.sex = 'man'

    def __getitem__(self, item):
        if hasattr(self, item):
            return self.__dict__[item]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __delitem__(self, key):
        del self.__dict__[key]


a = Foo()
# 执行__getitem__方法
print(a['name'])
# 执行__setitem__方法
a['like'] = 'python'
# 执行__delitem__方法
print(a.__dict__)
del a['like']
print(a.__dict__)


# __new__构造方法：创建一个对象
# 先执行__new__在执行__init__方法
# 单例模式
class dan:
    __instanse = False

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        if cls.__instanse:
            return cls.__instanse
        cls.__instanse = object.__new__(dan)
        return cls.__instanse


a = dan('luyuan')
b = dan('xuzhongxiao')
print(a)
print(b)


class Eq:
    def __init__(self, name):
        self.name = name

    # 比较执行该方法
    def __eq__(self, other):
        if self.name == other.name:
            return True
        return False


e1 = Eq('luyuan')
e2 = Eq('luyuan')
print(e1 == e2)

# hash()内部实现__hash__函数
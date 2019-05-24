# 属性隐藏不让看 属性前面__
# 封装的属性可以使用_类名__属性名 调用
# 私有属性或方法不能再类的外部生成
# 私有属性方法不要再外部调用
# 私有方法 私有属性 私有静态变量
class Person:
    __language = 'Chinese'  #私有静态属性

    def __init__(self, name, age):
        self.__name = name  # 私有属性
        self.__age = age

    def __change_name(self, new_name):
        self.__name = new_name  # 私有属性内部调用方式不变，外部无法直接调用

    def change_language(self, new_language):
        Person.__language = new_language

    def get_name(self):
        self.__change_name('sb')
        return self.__name


p = Person('陆远', 12)
print(p._Person__name)  # 私有属性外部调用方式
print(p._Person__language)  # 私有静态属性外部调用方式
print(p.get_name())  # 私有方法使用公用方法调用，保证私有函数的安全性
# property 内置装饰器函数 只在面向对象中使用
# 伪装成一个属性
from math import pi


class Circle:
    def __init__(self, r):
        self.__r = r

    @property  # 伪装成属性 不能传参数
    def area(self):
        return self.__r**pi * 2

    @area.setter  # 和property配合使用 只能接受一个值
    def area(self, new_r):
        self.__r = new_r

    @area.deleter  # 删除方法
    def area(self):
        del self.__r


c = Circle(4)
print(c.__dict__)
print(c.area)  #以属性的方式调用
c.area = 100
print(c.area)
del c.area  # 执行@area.deleter下的方法,具体操作看方法
print(c.__dict__)
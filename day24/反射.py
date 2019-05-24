# isinstance(obj,cls) 判断对象是否是该类的实例化对象
# issubclass(sub,super) 判断子类是否是父类的子类

# 反射自己模块的函数和变量
year = 2018
import sys
moudle = sys.modules
print(getattr(sys.modules['__main__'], 'year'))


# 反射自己模块中的函数
def my_func():
    print('my_func')


getattr(sys.modules['__main__'], 'my_func')()

# 获取当前时间
import time

print(getattr(time, 'strftime')('%Y-%m-%d'))


# serattr 设置一个变量
class A:
    pass


setattr(A, 'name', 'alex')
print(A.__dict__)
# delattr 删除一个变量
# 同 del A.name
delattr(A, 'name')
print(A.__dict__)
# 实例化对象先从自己空间里找变量，在去类里找变量
# getattr
# 获取自己模块的变量·类和方法
# 获取基本库的变量·类和方法
# 获取自定义模块的类和方法

# 其余的内置方法

# __str__  str()

# __repr__  repr()显示变量原有的类型
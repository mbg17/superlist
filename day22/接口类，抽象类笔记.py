#python原生并没有接口类这一概念,但是为了实现接口隔离原则,而划分出来的

# 接口隔离原则:
# 使用多个专门的接口,而不使用单一的总接口,即客户端不应该依赖那些不需要的接口

# 因为python天生能实现多继承,所以并没有接口类

# 应该算符合原则,强行区分出来这么一类吧

# 抽象类：单继承，定义规范，子类拥有相同类似的方法，必须实现，一般情况下单继承能实现的功能都是一样的

# 抽象类和接口类都不能实例化

# 通常用abc模块 的metaclass = ABCMeta 和 @abstractmethod装饰器定义抽象类必须实现的函数

# 鸭子方法值得是，虽然拥有相同方法，但不是继承同一个父类实现的功能，而是自己实现功能的方法就是鸭子方法

# 抽象类实例
# 接口类 抽象类
from abc import abstractmethod, ABCMeta


class Payment(metaclass=ABCMeta):  # 指定元类为ABCMeta
    # 抽象类装饰器 和metaclass=ABCMeta 配合使用
    @abstractmethod  # 指定规范继承该类必须实现这个方法
    def pay(self, money):
        print('支付了%s' % money)

    def huixie(self):
        pass


class Wechat(Payment):
    def pay(self, money):
        print('支付了%s' % money)


# 多态
# 不同的类执行相同的方法 叫做多态
def pay(obj, money):
    obj.pay(money)


# 接口类 支持多继承
# 抽象类 不支持多继承
# p = Payment() 抽象类不能调用
w = Wechat()
pay(w, 100)

# 抽象类 子类实现的功能类似 单继承
# 接口类 实现的功能不同 多继承
# 鸭子类型
# 不崇尚根据继承得来的相似
# 只实现自己的代码
# 如果两个类相似，是自己写代码约束的，而不是父类约束的


# 接口类
# 一个类继承多种规范
class Swim_animal(metaclass=ABCMeta):
    @abstractmethod
    def swim(self):
        print('swimming')


class Walk_animal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        print('walking')


class Fly_animal(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        print('flying')


class Tiger(Swim_animal, Walk_animal):
    def swim(self):
        print('swimming')

    def walk(self):
        print('walking')


class Bird(Walk_animal, Fly_animal):
    def fly(self):
        print('flying')

    def walk(self):
        print('walking')


b = Bird()
b.fly()
from abc import abstractmethod, ABCMeta


# 接口类 抽象类
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


def pay(obj, money):
    obj.pay(money)


# 接口类 支持多继承，接口类所有的方法都必须不能实现
# 抽象类 不支持多继承 抽象类中可以实现一些方法
# p = Payment() 抽象类不能调用
w = Wechat()
pay(w, 100)
# 抽象类 子类实现的功能类似 单继承
# 接口类 实现的功能不同 多继承

# 鸭子类型
# 不崇尚根据继承得来的相似
# 只实现自己的代码
# 如果两个类相似，是自己写代码约束的，而不是父类约束的
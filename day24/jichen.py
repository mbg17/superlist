# 父类 基类 超类
# 子类 派生类
# __bases__ 查看父类
# object 类是所有类的祖宗（新式类）
# super()集成父类的元素 省略了当前类和self super(当前类，self) 外部必传参数
# 只在新式类有 super关键字
# 多继承方法执行顺序从左到右找最近的 找不到再找最顶层的继承类
# python 2.7 深度优先（不走重复路线）  python 3 广度优先
class A:
    def func(self):
        print(1)


class B(A):
    # def func(self):
    #     print(2)
    pass


class C:
    # def func(self):
    #     print(3)
    pass


class D(B, C):
    # def func(self):
    #     print(4)
    pass


# 先从左到右找，找不到在从下往上找
# 查找顺序以具体继承方式走
# mro()函数显示查找顺序
d = D()
d.func()
print(D.mro())
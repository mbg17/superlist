class Dog:
    def __init__(self, name, blood, aggr, kind):
        self.name = name
        self.blood = blood
        self.aggr = aggr
        self.kind = kind

    def bite(self, person):
        person.blood -= self.aggr
        print('%s被咬了，掉了%s血' % (person.name, self.aggr))


class Person:
    def __init__(self, name, blood, aggr, sex):
        self.name = name
        self.blood = blood
        self.aggr = aggr
        self.sex = sex

    def attack(self, dog):
        dog.blood -= self.aggr
        print('%s被打了，掉了%s血' % (dog.name, self.aggr))


class Game:
    def __init__(self, person, dog):
        self.person = person
        self.dog = dog

    def start(self):
        while True:
            self.dog.bite(self.person)
            if self.dog.blood == 0:
                print('%s死了' % self.dog.name)
                break
            self.person.attack(jin)
            if self.person.blood == 0:
                print('%s死了' % self.person.name)
                break


jin = Dog('金老板', 100, 20, 'teddy')
ren = Person('我', 100, 20, '男')
Game(ren, jin).start()

# 类中的静态变量可以被对象和类调用
# 类.__dict__ 只能查看不能修改
# 实例出来的对象指向同一个类
# 不可变类变量最好用类调用 ，可变类变量可以用对象调用

# 练习题
# 创建一个类，没实例化一个对象就记录下来


class foo:
    count = 0

    def __init__(self):
        foo.count += 1


f_1 = foo()
f_2 = foo()

print(f_2.count)
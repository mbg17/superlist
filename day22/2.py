class Animal:
    def __init__(self, name, aggr, hp):
        self.name = name
        self.aggr = aggr
        self.hp = hp

    def eat(self):
        print(self.name, '回血')
        self.hp += 100


class Person(Animal):
    def __init__(self, name, aggr, hp, sex):
        super().__init__(name, aggr, hp)
        # Animal.__init__(self, name, aggr, hp)
        self.sex = sex

    def eat(self):
        super().eat()
        # Animal.eat(self)
        self.teeth = 2


a = Animal('hah', 10, 200)
person = Person('haha', 10, 200, '男')
person.eat()
print(person.hp, a.hp)

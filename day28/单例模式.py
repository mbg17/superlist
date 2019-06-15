class Singleton:
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance


one = Singleton()
two = Singleton()

two.a = 3
print(one.a)
# 3
# one和two完全相同,可以用id(), ==, is检测
print(id(one))
# 29097904
print(id(two))
# 29097904
print(one == two)
# True
print(one is two)

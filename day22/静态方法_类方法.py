class j_l_method:
    usr = 'luyuan'
    __pwd = '123456'

    def __init__(self, usr, pwd):
        if usr == self.usr and pwd == self.__pwd:
            print('登陆成功')
        else:
            print('登录失败')

    # 通常用来操作静态变量才使用类方法
    @classmethod  # 类方法 需要传默认参数cls
    def change_pwd(cls, new_pwd):
        cls.__pwd = new_pwd

    # 方法与属性和类无关才使用静态方法
    @staticmethod  # 静态方法不需要传参数
    def login():
        usr = input('用户名')
        pwd = input('密码')
        j_l_method(usr, pwd)


# 静态方法和类方法都可以被实例化对象调用
j_l_method.login()  #静态方法的调用
j_l_method.change_pwd('654321')
j_l_method.login()
j_l = j_l_method('luyuan', '123456')
j_l.login()
j_l.change_pwd('654321')

# 反射
# hasattr getattr delattr


class fanshe:
    dic = {'name': 'get_name', 'pwd': 'get_pwd'}

    def __init__(self):
        self.age = 100

    @classmethod
    def get_name(cls):
        print('name')

    def get_pwd(self):
        print('pwd')


f = fanshe()
# hasattr 判断类是否含有对象或方法
# 反射类方法
if hasattr(fanshe, 'get_name'):
    l_f = getattr(fanshe, 'get_name')
    l_f()
# 反射类属性
if hasattr(fanshe, 'get_name'):
    l_d = getattr(fanshe, 'dic')
    print(l_d)
# hasattr 判断对象是否含有对象或方法
# 反射对象方法
if hasattr(f, 'get_pwd'):
    d_f = getattr(f, 'get_pwd')
    d_f()
# 反射对象属性
if hasattr(f, 'age'):
    d_d = getattr(f, 'age')
    print(d_d)
import pickle


# 学校
class Classroom:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_student(self, name):
        for i in self.students:
            if name == i.name:
                return i
        return ''


class School:
    def __init__(self, local):
        self.local = local
        if self.local == '上海':
            self.course = ('go')
        elif self.local == '北京':
            self.course = ('python', 'linux')
        else:
            self.course = None


class Teacher:
    def __init__(self, name):
        self.name = name
        self.classroom = None
        self.course = None
        self.password = 123456
        self.school = None

    def watch_class(self):
        if self.classroom == None:
            print('暂未分配班级')
        else:
            print(self.classroom.name)

    def watch_course(self):
        if self.course == None:
            print('无法查看课程')
        else:
            print(self.course)

    def watch_student(self):
        if self.classroom == None:
            print('无法查看学员')
        else:
            for i in self.classroom.students:
                print(i.name, end=' ')
            print()

    def change_score(self, name, score):
        student = self.classroom.get_student(name)
        if student != '':
            student.score = score
        else:
            print('无此人')


class Student:
    def __init__(self, name, age, classroom=None):
        self.name = name
        self.age = age
        self.classroom = classroom
        self.password = 123456
        self.score = 0

    def login(self):
        name = input('输入用户名')
        password = int(input('输入密码'))
        if self.name == name and self.password == password:
            print('登录成功')
        else:
            print('用户名或密码错误')

    def watch_class(self):
        if self.classroom == None:
            print('暂未选择班级')
            if len(root.classroom_list) > 0:
                for i, n in zip(root.classroom_list, range(3)):
                    print(n, i.name, end='')
                print()
                id = int(input('请选择班级'))
                if id <= len(root.classroom_list) - 1:
                    self.classroom = root.classroom_list[id - 1]
                    root.classroom_list[id].add_student(self)
                else:
                    print('选择错误重新选择')
                    self.watch_class()
            else:
                print('暂未创建班级')

        else:
            print(self.classroom.name)

    def watch_course(self):
        print(self.classroom.course)

    def watch_myself(self):
        classroom = self.classroom.name if self.classroom is not None else '暂未分配'
        print('名字:%s 年龄:%s 教室:%s 密码:%s 分数:%s' %
              (self.name, self.age, self.classroom.name, self.password,
               self.score))


class Root:
    teacher_list = []
    classroom_list = []
    student_list = []
    course_list = []
    teacher_login = []
    student_login = []
    root_user_name = 'superuser'
    root_password = 123456789
    menu = ('创建老师', '创建学生', '创建教室', '创建课程', '分配课程', '分配教室')
    school = {'上海': ['go'], '北京': ['linux', 'python']}

    def create_teacher(self):
        while True:
            i = input('请输入老师所在的学校')
            if i in Root.school.keys():
                school = i
                break
        name = input('请输入老师的名字')
        teacher = Teacher(name)
        teacher.school = school
        Root.teacher_list.append(teacher.name)
        Root.teacher_login.append({
            'name': teacher.name,
            'password': teacher.password,
            'userinfo': teacher
        })
        return teacher

    def create_student(self, name, age):
        student = Student(name, age)
        Root.student_list.append(student)
        Root.student_login.append({
            'name': student,
            'password': student.password,
            'userinfo': student
        })
        return student

    def create_classroom(self, name):
        classroom = Classroom(name)
        Root.classroom_list.append(classroom)
        return classroom

    def create_course(self, course):
        Root.course_list.append(course)
        return course

    def give_course(self, teacher, course):
        id = 0
        if teacher.name in Root.teacher_list:
            for i in Root.school[teacher.school]:
                print(id, i)
                id += 1
            course = input('请输入课程编号')
            while True:
                if int(course) <= len(Root.school[teacher.school]):
                    teacher.course = Root.school[teacher.school][int(course)]
                    break
                else:
                    print('请重新输入')
            teacher.course = course
        else:
            print('没有这个老师')

    def give_classroom(self, teacher, classroom):
        if teacher.name in Root.teacher_list:
            teacher.classroom = classroom
        else:
            print('没有这个老师')

    def Menu(self, caidan):
        # ('创建老师','创建学生','创建教室','创建课程','分配课程','分配教室')
        for i in Root.menu:
            if i == '创建老师' and caidan == i:
                self.create_teacher
            elif i == '创建教室' and caidan == i:
                self.create_classroom
            elif i == '创建课程' and caidan == i:
                self.create_course
            elif i == '创建学生' and caidan == i:
                self.create_student
            elif i == '分配教室' and caidan == i:
                self.give_classroom
            elif i == '分配课程' and caidan == i:
                self.give_course
            else:
                print('输入有误')


root = Root()


def login(biaoshi, name, password):
    if biaoshi == 'root':
        if name == Root.root_user_name and password == Root.root_password:
            print('登陆成功')
            return root
        else:
            print('不要吃饱了撑得')
    elif biaoshi == 'student':
        for i in Root.student_login:
            if name == i['name'] and password == i['password']:
                print('登陆成功')
                return i['userinfo']
                break
            else:
                print('不要吃饱了撑得')
    elif biaoshi == 'teacher':
        for i in Root.teacher_login:
            if name == i['name'] and password == i['password']:
                print('登陆成功')
                return i['userinfo']
                break
            else:
                print('不要吃饱了撑得')


c = root.create_classroom('三班')
t = root.create_teacher()
s = root.create_student('徐忠孝', 50)
s_2 = root.create_student('me', 50)
course = root.create_course('python')

root.give_course(t, course)
root.give_classroom(t, c)
s.watch_class()
s_2.watch_class()
t.watch_student()
t.watch_class()
t.watch_course()
t.change_score('徐忠孝', 100)
s.watch_myself()
dl = login('root', 'superuser', 123456789)
print(dl.root_password)
print(s.score)
with open('学校管理系统', 'wb') as f:
    pickle.dump(s, f)
    pickle.dump(c, f)
    pickle.dump(s_2, f)
    pickle.dump(t, f)
    pickle.dump(course, f)
with open('学校管理系统', 'rb') as f:
    print(pickle.load(f))
    print(pickle.load(f))
    print(pickle.load(f))
    print(pickle.load(f))
    print(pickle.load(f))
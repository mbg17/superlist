from greenlet import greenlet


# 定义两个函数
def eat():
    print('eat start')
    g2.switch()  # 切换到另一个函数并记录执行的位置
    print('eat end')
    g2.switch()


def play():
    print('play start')
    g1.switch()
    print('play end')


g1 = greenlet(eat)  # 注册协程函数
g2 = greenlet(play)
g1.switch()  # 切换协程

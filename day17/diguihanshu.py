# 什么是递归函数：函数自己调用自己就是递归函数
# RecursionError:超过最大递归深度报错
# import sys
# sys.setrecursionlimit() 设置递归上限
#46 1
#44 2
#42 3
#40 4
def age(n):
    # 如果问到第四个人的年龄则返回40岁
    if n==4:
        return 40
    elif n>0 and n<4:
    # 第一个人的年龄为第二个人的年龄+2岁
        return age(n+1)+2
# 调用顺序：第一个人向第二个人问年龄，第二个人向第三个人问年龄，第三个人向第四个人问年龄
# 返回顺序：第四个人说出他的年龄，第三个人知道了自己的年龄，第二个人知道了自己的年龄，第一个人知道了自己的年龄
#print(age(1))
# 二分查找
def find(l,aim,start=0,end=None):
    end = len(l) if end is None else end
    middle_index = (end - start)//2 + start
    if start - end <= 0:
        if l[middle_index] <aim:
            return find(l,aim,start=middle_index+1,end=end)
        elif l[middle_index] > aim:
            return find(l, aim, start=start, end=middle_index -1)
        else:
            return middle_index
    else:
        return '没有找到'

#三级菜单

#斐波那契
def fq(n):
    if n==1 or n==2:
        return 1
    else:
        return fq(n-1)+fq(n-2)

def fq_2(n,l=[0]):
    l[0] += 1
    if n==2:
        l[0] -= 1
        return 1,1
    elif n==1:
        l[0] -= 1
        return  1
    else:
        a,b = fq_2(n-1)
        l[0] -= 1
        if l[0]==0:
            return a+b
        return b,a+b
#阶乘
def jc(n):
    if n==1:
        return 1
    else:
        return n * jc(n-1)

l=[1,2,22,33,56,78,99,100]
print(find(l,99))
print(fq_2(1))
#print(jc(100))
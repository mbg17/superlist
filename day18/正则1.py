# ======量词=======
# * 0次或多次
# + 一次或多次
# ？ 0次或一次
# {n} 重复n次
# {n,} 重复n次或更多次
# {n,m} 重复n-m次
# ======元字符=======
#\w 匹配所有英文数字下划线 \W 匹配非所有英文数字下划线 一块用可以匹配所有内容
#\s 匹配所用空格符 \S 匹配所有非空格符 一块用可以匹配所有内容
#\d 匹配所有数字 \D 匹配所有非数字 一块用可以匹配所有内容
#\n 匹配所有换行符 \t 匹配所有制表符
#\b 匹配一个单词的结尾
# . 匹配所有
#| 匹配其中之一 通常范围大的放前面
#^ 匹配开头 $匹配结尾 一起用约束一整串字符
# []匹配括号内的所有字符 括号内可用[0-9]类似的写法，小的在前大的在后
# [^]不匹配括号内的所有字符
# 量词后面+？惰性匹配 ？后面有符号惰性匹配到制定符号的位置
# *？ 重复任意次 尽可能少重复
# +？ 重复一次或多次 尽可能少重复
# ？？ 重复0次或多次 尽可能少重复
# ｛n,m｝ 重复n-m次 尽可能少重复
# ｛n,｝ 重复n次以上，尽可能少重复
# .*? 任意字符匹配0次以上，非贪婪匹配
import re
import requests


# findall 返回所有结果放在列表中 优先匹配（）内的条件 ?:取消优先匹配
# search 从前往后找到一个就返回 返回的是一个结果的对象 需要调用group()才能返回结果
# match 从头开始匹配 如果正则规则从头开始完全匹配上，就返回结果 需要用group()返回结果
# ret = requests.get('http://tool.chinaz.com/regex')
# print(ret.text)
# req = re.finditer('<a href="(?P<url>http:.+(com|cn)/).*?(</a>)',ret.text)
# for i in req:
#     print(i.group('url'))
# sub 用正则规则匹配替换 sub（替换前的内容，替换后的内容，被替换的内容）
# subn fanhui 返回替换的结果 并返回替换了几次
# compile 编译正则规则 返回一个正则规则对象 通过规则查找内容
# finditer 返回查询到结果的迭代器
def add_op(arg):  # 定义加法函数
    arg = arg.replace("++", "+").replace("--",
                                         "+").replace("+-",
                                                      "-").replace("-+",
                                                                   "-")  # 替换符号
    num = re.findall("([+\-]?\d+\.?\d*)", arg)  #匹配所有数字
    result = 0
    for i in num:  #循环数字列表进行累加
        result = result + float(i)
    return result


def mul(arg):  #定义乘除函数
    while True:
        result = re.split("(\d+\.?\d*[\*/][\+-]?\d+\.?\d*)", arg, 1)  #匹配乘法或除法
        if len(result) == 3:
            bef, cen, aft = result
            if "*" in cen:  #判断乘号是否在cen里面
                num1, num2 = cen.split("*")  #将乘号进行分割得到乘数
                new_cen = float(num1) * float(num2)  #将乘数相乘得到乘积
                arg = bef + str(new_cen) + aft  #将乘积放入新的字符串表达式
            elif "/" in cen:  #判断除号是否在cen里面
                num1, num2 = cen.split("/")  #分割除号得到除数和被除数
                new_cen = float(num1) / float(num2)  #进行除法运算
                arg = bef + str(new_cen) + aft  #将商放入新的字符串表达式
        else:
            return add_op(arg)


def calc(arg):
    while True:
        arg = arg.replace(" ", "")
        result = re.split("\(([^()]+)\)", arg, 1)  #匹配最里面的括号并且只取括号中的内容
        if len(result) == 3:
            bef, cen, aft = result
            # 计算括号中的表达式，先乘除后加减，得到计算结果
            r = mul(cen)
            #使用计算结果组成新的字符串表达式
            arg = bef + str(r) + aft
        else:  #计算完括号后开始按照先乘除再加减的运算
            return mul(arg)


s = '1 - 2 *((60 -30 + (-40/5)*(9-2*5/3 +7/3*99/4*2998+10 * 568/14))-( -4 *3)/(16 - 3*2))'
s = s.replace(' ', '')
result = re.split("\(([^()]+)\)", s, 1)  #匹配最里面的括号并且只取括号中的内容
print(result)
ret = re.split("(\d+\.?\d*[\*/][\+-]?\d+\.?\d*)", result[1], 1)
print(ret)
r = calc(s)
print(r)

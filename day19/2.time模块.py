# 字符串格式化：显示给人看 format_time
# time.strftime(格式化字符串) %Y 年%m 月%d 日%H 小时%M 分钟%S 秒
# 时间戳-- 给计算机看的 timestamp
# 结构化时间 --- 元祖 (struct_time)： 计算用的
# time.localtime()
# import time
# stryct_time = time.localtime()  # 结构化时间
# 时间戳 结构化时间互转
# t = time.time()  # 获取时时间戳
# print(time.localtime(t))  # 本地化时间
# print(time.gmtime(t))  # 格林制时间
# print(time.mktime(time.localtime()))  # 结构化转时间戳
# 格式化时间转结构化时间
# print(time.strptime('2000-12-31', '%Y-%m-%d'))
# 结构化时间转格式化时间
# print(time.strftime('%Y-%m-%d', time.localtime()))
# 结构化转格式化时间（详细）
# time.atime(time.localtime())
# 结构化转时间戳（详细）
# time.ctime(150000)

import time


# 练习题 计算时间差
def sumtime(strf, model='%Y-%m-%d'):
    if type(strf) == str:
        now_time = time.localtime()
        last_time = time.strptime(strf, model)
    elif type(strf) == int or type(strf) == float:
        now_time = time.localtime()
        last_time = time.localtime(strf)
    else:
        return '输入有误'
    return ("经厉了 %s年%s月%s日 %s小时%s分钟%s秒" %
            (now_time.tm_year - last_time.tm_year, now_time.tm_mon -
             last_time.tm_mon, now_time.tm_mday - last_time.tm_mday,
             now_time.tm_hour - last_time.tm_hour, now_time.tm_min -
             last_time.tm_min, now_time.tm_sec - last_time.tm_sec))


print(sumtime(1500000))
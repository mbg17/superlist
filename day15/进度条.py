import time
for i in range(0,101,2):
    time.sleep(1)
    num = i//2
    # \r回到行首 \n换行
    st = '\r%s%%:%s\n' % (i,'*'*num) if i==100 else '\r%s%%:%s'%(i,'*'*num)
    print(st,end='',flush=True)
"""
file 指定到文件输出
sep 分隔符
flush 不缓存直接输出
end 以什么为结尾
"""
# eval exec 执行为字符串格式的python语句
# eval有返回值 exec 没有返回值
# eval 简单计算
# exec 流程控制
# complie(代码，从哪个文件读，执行方式)
# 执行方式：single（交互式代码） exec（流程控制） eval(简单计算)
# bin oct hex 二进制 八进制 十六进制

# x and y： 布尔”与” ——如果 x 为 False，x and y 返回 False。否则它返回 y 的计算值。 (a and b) 返回 20。
#
# x or y： 布尔”或” —— 如果 x 是 True，它返回 x 的值。否则它返回 y 的计算值。 (a or b) 返回 10。
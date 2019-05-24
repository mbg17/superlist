# 数据类型-》字符串 序列化
# 字符串——》数据类型 反序列化
# json
# 通用的序列化格式
# 少部分数据类型才能用json转化成字符串
# pickle
# 所有数据类型都可以转成字符串形式
# 只有python才能理解序列化后的内容
# 以来pyhton代码
# shelve
# 操作简单 序列化句柄
# 使用句柄直接操作
# ----------json----------
#dumps 序列化方法 loads 反序列化方法
# 数字 字典 列表 元祖（以列表形式序列化） 字符串
# dump load 对文件操作 ensure_ascii是否已bytes类型写入
import json
f = open('file', 'w')
json.dump({'k': 'q'}, f, ensure_ascii=False)  # ensure_ascii指定是否允许以Bytes类型写入文件
f.close()
f = open('file')
print(json.load(f))  # 一次只能读一条数据
f.close()
# 读多条数据写法
l = [{'k': 'q'}, {'k1': 'q'}, {'k2': 'q'}]
f = open('file_2', 'w')
# 将数据换行写入文件
for i in l:
    str_d = json.dumps(i)
    f.write(str_d + '\n')
f.close()
# 读文件反序列读取数据
with open('file_2', 'r') as f:
    for i in f:
        print(json.loads(i.strip()))
#-----------pickle----------
# 可以逐条读逐条写 序列化任何对象
# dumps dump loads load
# dumps loads 操作数据
# dump load 将数据写入文件 操作文件时要用二进制模式
import pickle
import time
f = open('pickle', 'wb')
date = time.localtime()
pk = pickle.dumps(date)  # 将参数序列化
pickle.dump(date, f)  # 将参数序列化写入文件
print(pickle.loads(pk).tm_year)
f.close()
f_2 = open('pickle', 'rb')  # 打开文件
ti = pickle.load(f_2)  # 反序列化文件
print(ti.tm_year)  # 读取参数
f_2.close()
#------shelve--------
# 操作类似字典
# open打开 以字典的形式写入 ，以字典的方式读取
import shelve  # 不允许操作同一个文件 操作同一个文件用r模式 flag=r
she = shelve.open('test', writeback=True, flag='w')  #writeback有更新追加内容 flag 模式
she['key']['tt'] = {'1': '2'}
print(she['key'])
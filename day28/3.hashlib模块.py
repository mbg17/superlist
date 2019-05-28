# hashlib 摘要算法模块
# 不管算法多么不停，摘要的功能始终相同
# 同一个字符串，使用的同一个算法，结果始终相同
# 不同算法对相同的字符串，结果一定不同
# 不管什么算法，hashlib的方法始终不变
# sha算法越复杂越安全，但是时间成本和空间成本成正比例上升
# 摘要算法用于密码的验证，文件的比对
#https://blog.csdn.net/secret5/article/details/70150486
from hashlib import md5, sha1, sha224, sha256, sha384, sha512
from pprint import pprint

hash_funcs = [md5, sha1, sha224, sha256, sha384, sha512]


def hash_show(s):
    result = []
    for func in hash_funcs:
        # 用hashlib函数对当前数据进行编码
        s_hash_obj = func(s)
        # 获取当前的字符串的哈希值
        s_hash_hex = s_hash_obj.hexdigest()
        # 用列表返回加密后的数据
        result.append((s_hash_obj.name, s_hash_hex, len(s_hash_hex)))
    return result


if __name__ == '__main__':
    s = b'hello python'
    rs = hash_show(s)
    pprint(rs)

#单个函数方法加密
from hashlib import md5
m1 = md5()  # 构造hash对象
m1.update(b'hello')
m1.update(b' ')
m1.update(b'python')
m2 = md5(b'hello python')
# hexdigest获取加密后的结果
print(m1.hexdigest() == m2.hexdigest())  # 两种方式的效果相同

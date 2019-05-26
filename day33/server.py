import socket
import hmac
import os
# 秘钥
secure_key = b'luyuan'


# 核对秘钥方法
def check_secure(conn):
    # 随机生成32位bytes类型的字符串
    key = os.urandom(32)
    # 将秘钥发送给客户端
    conn.send(key)
    # 生成秘钥
    h = hmac.new(secure_key, key)
    digest = h.digest()
    client_digest = conn.recv(1024)
    # 返回效验结果
    return hmac.compare_digest(digest, client_digest)


sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()

conn, addr = sk.accept()
status = check_secure(conn)
# 根据结果做相应的处理
if status:
    print('True')
    conn.close()
else:
    print('False')
    conn.close()

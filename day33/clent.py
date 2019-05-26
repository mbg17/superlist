import socket
import hmac


# 生成秘钥
def generate_secure(key, secure_key):
    h = hmac.new(secure_key, key)
    digest = h.digest()
    return digest


sk = socket.socket()
sk.connect(('127.0.0.1', 8080))

secure_key = bytes(input('请输入秘钥:'), encoding='utf-8')
key = sk.recv(1024)

digest = generate_secure(key, secure_key)
sk.send(digest)
sk.close()

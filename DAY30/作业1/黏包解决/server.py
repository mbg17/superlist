import socket
import struct
sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()
coon, sddr = sk.accept()
while True:
    info = input('>>>')
    if info == 'q':
        coon.send(b'q')
        break
    coon.send(info.encode('gbk'))
    r_num = coon.recv(4)
    num = struct.unpack('i', r_num)[0]  # 解包数据，返回一个元祖，用[0],获取第一个数字
    print(num)
    msg = coon.recv(num).decode('gbk')
    print(msg)
sk.close()
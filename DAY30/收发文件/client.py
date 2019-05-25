import socket
import os
import json
import struct
buffer = 4096
sk = socket.socket()
sk.connect(('127.0.0.1', 8080))
# 定义报文头
head = {'filepath': 'D:\笔记', 'filename': '反射.xmind', 'filesize': None}
# 拼接路径
filepath = os.path.join(head['filepath'], head['filename'])
# 计算文件大小并赋值
head['filesize'] = os.path.getsize(filepath)
filesize = head['filesize']
# 用json将数据序列化
head_json = json.dumps(head)
# 转换成bytes类型
bytes_json = head_json.encode('utf-8')
# 计算bytes类型的长度 用struct模块包装后发送给服务端，防止黏包
head_len = len(bytes_json)
pack_len = struct.pack('i', head_len)
# 先发送报文长度 在发送报文数据
sk.send(pack_len)
sk.send(bytes_json)
# 发送逻辑
with open(filepath, 'rb') as f:
    while filesize:
        if filesize >= buffer:
            content = f.read(buffer)
            sk.send(content)
            filesize -= buffer
        else:
            content = f.read(filesize)
            sk.send(content)
            break
sk.recv(1024)
sk.close()

import socket
import json
import struct
buffer = 4096
sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()
conn, addr = sk.accept()

ret = conn.recv(4)
ret = struct.unpack('i', ret)[0]
head_json = conn.recv(ret).decode('utf-8')
head = json.loads(head_json)
filesize = head['filesize']
filename = head['filename']
print(filename)
with open('./' + filename, "wb") as f:
    while filesize:
        if filesize >= buffer:
            content = conn.recv(buffer)
            f.write(content)
            filesize -= buffer
        else:
            content = conn.recv(filesize)
            f.write(content)
            break
conn.send(b'ok')
conn.close()
sk.close()
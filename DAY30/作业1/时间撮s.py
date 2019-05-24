import socket
import time
sk = socket.socket()
ip = '127.0.0.1'
dk = 8080

sk.bind((ip, dk))
sk.listen()
#time.strftime('%Y-%m-%d', time.localtime())
conn, addr = sk.accept()
while True:
    ret = int(conn.recv(1024).decode('utf-8'))
    timeStruct = time.localtime(ret)
    strTime = time.strftime("%Y-%m-%d %H:%M:%S", timeStruct)
    print(strTime)

conn.close()
sk.close()
import socket
from multiprocessing import Pool
def server_send(conn):
    conn.send(b'hello')
    msg = conn.recv(1024).decode('utf-8')
    print(msg)
    conn.close()
if __name__ =='__main__':
    sk = socket.socket()
    sk.bind(('127.0.0.1',8080))
    sk.listen()
    pool = Pool(5)
    while True:
        conn,addr = sk.accept()
        pool.apply_async(server_send,args = (conn,))
    sk.close()


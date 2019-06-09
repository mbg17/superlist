import socket
from threading import Thread


def server_send(conn):
    conn.send(b'hello')
    msg = conn.recv(1024).decode('utf-8')
    print(msg)
    conn.close()


if __name__ == '__main__':
    sk = socket.socket()
    sk.bind(('127.0.0.1', 8080))
    sk.listen()
    while True:
        conn, addr = sk.accept()
        Thread(target=server_send, args=(conn, )).start()
    sk.close()

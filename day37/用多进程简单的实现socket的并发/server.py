from multiprocessing import Process
import socket


def serve(conn, addr):
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
        p = Process(target=serve, args=(conn, addr))
        p.start()
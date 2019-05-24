import socket
import subprocess
sk = socket.socket()
sk.connect(('127.0.0.1', 8080))
while True:
    cmd = sk.recv(1024).decode('gbk')
    if cmd == 'q':
        break
    msg = subprocess.Popen(cmd,
                           shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    std_out = msg.stdout.read()
    std_err = msg.stderr.read()
    sk.send(str(len(std_out) + len(std_err)).encode('gbk'))
    sk.recv(1024)
    sk.send(std_out)
    sk.send(std_err)
sk.close()
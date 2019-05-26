import socketserver


class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            msg = self.request.recv(1024).decode('utf-8')
            if msg == 'q':
                break
            else:
                print(msg)
                info = input('>>>').encode('utf-8')
                self.request.send(info)


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8080), Myserver)
    server.serve_forever()
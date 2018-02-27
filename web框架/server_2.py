import socketserver

class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        print("服务器端启动")
        while True:
            conn = self.request
            print(self.client_address)
            while True:
                client_data = conn.recv(1024)
                print(str(client_data,"utf-8"))
                print("waiting----")
                conn.sendall(client_data)
            conn.clos()

if __name__ == "__main__":
    sever = socketserver.ThreadingTCPServer(('127.0.0.1',1234), MyServer)
    sever.serve_forever()


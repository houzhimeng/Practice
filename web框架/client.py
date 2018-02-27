import socket

sk = socket.socket(socket.SOCK_DGRAM)
sk.connect(('127.0.0.1',1234))


while True:
    inp = input('>>>>')
    if inp == 'exit':
        break
    sk.send(bytes(inp,'utf8'))
    data = sk.recv(1024)
    print(str(data,'utf-8'))

sk.close()

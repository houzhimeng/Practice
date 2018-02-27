import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('127.0.0.1',1234)
sk.connect(address)


while True:
    inp = input('>>>>')
    if inp == 'exit':
        break

    sk.send(bytes(inp,'utf8'))

    result_len = int(str(sk.recv(1024),'utf8'))

    sk.sendall(b'ok')
    # print(result_len)

    data = bytes()

    while len(data) != result_len:
        recv = sk.recv(1024)
        data += recv

    print(str(data,'utf8'))

sk.close()

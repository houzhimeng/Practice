import socket

socket.socket()
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(sk)
sk.bind(('127.0.0.1',1234))
sk.listen(3)
print('watting....')

while 1:
    conn,info = sk.accept()
    print(conn)

    while 1:
        data = conn.recv(1024)
        if not data: break

        print('.........',str(data,'utf-8'))

        inp = input('>>>')
        conn.send(bytes(inp,'utf8'))

conn.close()

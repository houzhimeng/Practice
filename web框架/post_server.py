import socket
import subprocess
import os


socket.socket()
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(sk)
address = ('127.0.0.1',1234)
sk.bind(address)

sk.listen(3)
print('watting....')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


while 1:
    conn,info = sk.accept()
    print(info)

    while 1:
        data = conn.recv(1024)       #拿到客户端发来的数据解析
        cmd,filename,filesize = str(data,'utf8').split('|')
        path = os.path.join(BASE_DIR,'文件上传',filename)

        filesize = int(filesize)

        f = open(path,'ab')
        has_recv = 0
        while has_recv != filesize:
            data = conn.recv(1024)
            f.write(data)
            has_recv += len(data)
        f.close()



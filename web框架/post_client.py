import socket
import os

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('127.0.0.1',1234)
sk.connect(address)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


while True:
    inp = input('>>>>').strip()  # post|11.jpg   #input方式
    cmd,path = inp.split('|')            #参数结构，分割字符

    path = os.path.join(BASE_DIR,path)   #路径拼接
    filename = os.path.basename(path)        #取文件的名字
    file_size = os.stat(path).st_size         #取文件大小
    file_info = 'post|%s|%s'%(filename,file_size)

    sk.sendall(bytes(file_info,'utf8'))

    f = open(path,'rb')

    has_send = 0

    while has_send != file_size:
        data = f.read(1024)
        sk.sendall(data)
        has_send += len(data)

    f.close()
    print('上传成功')





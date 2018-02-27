import socket
import subprocess

socket.socket()
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(sk)
address = ('127.0.0.1',1234)
sk.bind(address)

sk.listen(3)
print('watting....')

while 1:
    conn,info = sk.accept()
    print(info)

    while 1:
        # try:
        data = conn.recv(1024)
        # except Exception as e:
        #     print(e)
        #     break
        # print('.........',str(data,'utf8'))

        if not data: break

        obj = subprocess.Popen(str(data,'utf8'),shell=True,stdout=subprocess.PIPE)
        cmd_result = obj.stdout.read()

        result_len = bytes(str(len(cmd_result)),'utf8')

        conn.sendall(result_len)
        conn.recv(1024)
        conn.sendall(cmd_result)

sk.close()

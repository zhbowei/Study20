#__author:  bwzhang
#__date:    2018/6/28

import subprocess


import socket
sk = socket.socket()
address = ('127.0.0.1',8000)
sk.bind(address) #绑定ip地址及端口
sk.listen(4)  #容纳排队连接的数量
print('warning....')


while 1:
    conn,addr =sk.accept()
    print(addr)
    while 1:
        try:
            data = conn.recv(1024)
        except Exception:
            break
        if not data:break
        print('....',str(data,'utf8'))

        obj = subprocess.Popen(data.decode('utf8'),shell=True,stdout=subprocess.PIPE)
        cmd_result =obj.stdout.read()

        result_len = bytes(str(len(cmd_result)),'utf8')
        print('>>>>>',result_len)
        conn.sendall(result_len) #粘包现象
        # import time
        # time.sleep(1)
        # conn.recv(1024) #解决粘包，中间加一个recv请求
        conn.sendall(cmd_result)

        # conn.send(result_len)

sk.close()

        # conn.send(cmd_result)


        # if not data:break
        # inp = input('>>>')
        # conn.send(bytes(inp,'utf8'))


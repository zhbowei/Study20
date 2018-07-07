#__author:  bwzhang
#__date:    2018/7/3

import socket,select
sk = socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen(3)
inp = [sk,]
while 1 :
    inputs,outputs,errors = select.select(inp,[],[],)
    for i in inputs:
        conn,addr = i.accept()
        print(conn)
        data = conn.recv(1024)
        print(data.decode('utf8'))
        conn.sendall(data)

    # while True:
    #     data = sk.recv(1024)
    #     print(bytes(data))
    #     sk.sendall(data)




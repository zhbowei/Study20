#__author:  bwzhang
#__date:    2018/6/28

import socket
sk = socket.socket()  #套接字
address = ('127.0.0.1',8001)
sk.bind(address) #绑定ip地址及端口
sk.listen(3)  #容纳排队连接的数量
print('warning....')
# conn,addr = sk.accept()  #在此阻塞，等待连接
# while 1:
#     data = conn.recv(1024)
#     print('.....',str(data,'utf8'))
#     if not data:
#         conn.close()
#         conn,addr = sk.accept()
#         print(addr)
#         continue
#     inp = input('>>>>')
#     conn.send(bytes(inp,'utf8'))
while 1:
    conn,addr =sk.accept()
    print(addr)
    while 1:
        try:
            data = conn.recv(1024)
        except Exception:
            break
        print('....',str(data,'utf8'))
        if not data:break
        inp = input('>>>')
        conn.send(bytes(inp,'utf8'))
conn.close()




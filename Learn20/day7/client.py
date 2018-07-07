#__author:  bwzhang
#__date:    2018/6/30

import socket
sk = socket.socket()
ip_port = ('127.0.0.1',8091)
sk.connect(ip_port)
print('客户端启动....')
while True:
    inp = input('>>>>>')
    sk.sendall(bytes(inp, 'utf8'))
    serve_re = sk.recv(1024)
    print(str(serve_re,'utf8'))



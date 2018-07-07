#__author:  bwzhang
#__date:    2018/6/28

import socket
sk = socket.socket()
address = ('127.0.0.1',8001)
sk.connect(address)

while True:
    inp = input('>>>')
    if inp == 'exit':
        break
    sk.send(bytes(inp,'utf8'))
    data = sk.recv(1024)
    print(str(data,'utf8'))
sk.close()



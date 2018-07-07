#__author:  bwzhang
#__date:    2018/6/28

import socket
sk=socket.socket()
print(sk)
address = ('127.0.0.1',8000)
sk.connect(address)


while True:
    inp = input('>>>')
    if inp == 'exit':
        break
    sk.send(bytes(inp,'utf8'))
    result_len = int(str(sk.recv(1024),'utf8'))
    # sk.sendall(111)
    print(result_len)
    data = bytes()
    while len(data) != result_len:
        recv = sk.recv(1024)
        data+=recv
    # data = sk.recv(1024)
    print(str(data,'gbk'))

sk.close()



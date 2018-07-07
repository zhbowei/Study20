#__author:  bwzhang
#__date:    2018/7/3
import socket
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.connect(('127.0.0.1',8080))
while 1:
    inp = input('>>>')
    sk.sendall(bytes(inp.encode('utf8')))
    data = sk.recv(1024)
    print(data.decode('utf8'))



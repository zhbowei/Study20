#__author:  bwzhang
#__date:    2018/7/6

import socket
def handle_request(client):
    buf = client.recv(1024)
    print(buf.decode('utf8'))
    client.send('HTTP/1.1 200 OK\r\n\r\n'.encode('utf8')) #请求头
    with open('index.html','rb') as f:
        data = f.read()
    client.send(data) #请求体
def main():
    sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sk.bind(('127.0.0.1',8001))
    sk.listen(5)
    while True:
        conn,addr = sk.accept() #等待客户端的链接
        handle_request(conn)
        conn.close()
if __name__ == '__main__':
    main()


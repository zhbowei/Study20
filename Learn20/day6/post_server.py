#__author:  bwzhang
#__date:    2018/6/28
import socket
import os
sk=socket.socket()
address=('127.0.0.1',8000)
sk.bind(address)
BASE_DAR=os.path.dirname(os.path.abspath(__file__))
while 1:
    conn, addr=sk.accept()
    print(addr)
    while 1:
        data = conn.recv(1024)
        cmd,filename,file_size = str(data,'utf8').split('|')
        path = os.path.join(BASE_DAR,'zhan',filename)
        file_size=int(file_size)

        f=open(path,'wb')
        had_receive = 0
        while had_receive != file_size:
            conn.recv(1024)
            f.write(data)
            had_receive += len(data)
        f.close()



# sk.listen(4)
# print('waring........')



sk.close()



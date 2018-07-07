#__author:  bwzhang
#__date:    2018/6/28

import socket
import os
sk = socket.socket()
print(sk)
address = ('127.0.0.1',8000)
sk.connect(address)
BASE_DAR=os.path.dirname(os.path.abspath(__file__))

while True:
    inp=input('>>>')    # post\11.pang
    cmd,path = inp.split('|')
    path = os.path.join(BASE_DAR,path)
    filename=os.path.basename(path)    #获取文件名字
    file_size=os.stat(path).st_size   #获取文件大小
    file_info='post|%s|%s'%(filename,file_size)
    sk.sendall(bytes(file_info,'utf8'))


    f=open(path,'rb')
    had_sent=0
    while had_sent!=file_size:
        data = f.read(1024)
        sk.sendall(data)
        had_sent+=len(data)
    f.close()
    print("上传成功")



sk.close()



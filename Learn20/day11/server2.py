#__author:  bwzhang
#__date:    2018/7/6
from wsgiref.simple_server import make_server
def application(environ,start_response):   #environ 是用于后续获取响应信息environ【path】再做判断分析给什么响应头信息,environ是一个携带请求信息的字典
    start_response('200 OK',[('Content-Type','text/html')]) #设定响应头
    return [b'<h1>Hello web!</h1>']
httpd = make_server('',8002,application) #封装了socker过程
print('Serving HTTP on port 8000...')
#开始监听请求
httpd.serve_forever()

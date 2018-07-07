#__author:  bwzhang
#__date:    2018/7/7

from wsgiref.simple_server import make_server
import time
def current_time(request):
    cur_time = time.ctime(time.time())
    f = open("current_time.html","rb")
    data = f.read()

    data=str(data,"utf8").replace("!cur_time!",str(cur_time))
    return [data.encode('utf8')]



def application(environ,start_response):
    start_response('200,OK',[('Content-type','text/html')])
    path =environ('PATH_INFO')
    urlpatterns = routers()
    func = None
    for item in urlpatterns:
        if item[0] == path:
            func = item[1]
            break
    if func:
        return func(environ)
    else:
        return ["<h1>404</h1>".encode('utf8')]




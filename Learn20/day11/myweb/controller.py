#__author:  bwzhang
#__date:    2018/7/7
# 放入url选择的函数
import time
def current_time(request):
    cur_time = time.ctime(time.time())
    f = open("current_time.html","rb")
    data = f.read()


    data = str(data,"utf8").replace("!cur_time!",str(cur_time))
    return [data.encode('utf8')]


def f1():
    pass



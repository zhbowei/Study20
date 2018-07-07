#__author:  bwzhang
#__date:    2018/7/1

import gevent
import time

# def foo():
#     print('Running in the foo',time.ctime())
#     time.sleep(1)
#     print('Explicit context switch to foo again',time.ctime())
# def bar():
#     print('Running in the bar',time.ctime())
#     time.sleep(2)
#     print('Implicit context switch back to bar',time.ctime())
#
#
# gevent.joinall([
#     gevent.spawn(foo),
#     gevent.spawn(bar),
# ])

from urllib.request import urlopen
from gevent import monkey
monkey.patch_all()

def scr(url):
    print('GET is %s'%url)
    resp = urlopen(url)
    data = resp.read()

    print('%d bytes received is %s.'%(len(data),url))

gevent.joinall([
    gevent.spawn(scr,'http://www.baidu.com')
])



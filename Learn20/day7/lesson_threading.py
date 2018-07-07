#__author:  bwzhang
#__date:    2018/6/30
import time
import threading
# def time_sleep(ex):
#     def inner(n):
#         time.sleep(8)
#         ex(n)
#         return inner
#
# def foo(n):
#     print('foo%s'%n)
#     # time.sleep(8)
#     print('end foo')
# def bar(n):
#     print('bar%s'%n)
#     # time.sleep(8)
#     print('end bar')
# print('.....in the main....')


# foo(2)
# bar(1)
# t1 = threading.Thread(target=foo,args=(2,))
# t2 = threading.Thread(target=bar,args=(1,))
# t1.start()
# t2.start()

#类创建线程
class MyThread(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num #self是实例变量
    def run(self):
        print('running on number:%s'%self.num)
        time.sleep(3)
if __name__=='__main__':
    t1 = MyThread(1)
    t2 = MyThread(2)
    t1.start()
    t2.start()


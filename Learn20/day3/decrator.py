#__author:  bwzhang
#__date:    2018/6/15
import time
# start = time.time()
# time.sleep(2)
# end = time.time()
# print(end-start)
# print(start)
# def show_time(f):
#     def inner():
#         start = time.time()
#         f()
#         end = time.time()
#         print('speed %s' % (end - start))
#     return inner

# @show_time # foo = show_time(foo)
# def foo():
#     print('foo......')
#     time.sleep(3)
# # foo = show_time(foo)
# @show_time
# def bar():
#     print('bar......')
#     time.sleep(2)
# foo()


# 功能函数加参数
# def show_time(f):
#     def inner(*a):
#         start = time.time()
#         f(*a)
#         end = time.time()
#         print('speed %s' % (end - start))
#     return inner
# @show_time
# def add(*a):
#     sum = 0
#     for i in a:
#         sum += i
#     print(sum)
#     time.sleep(1)
# add(2,3,4,5,7)


# 装饰器加参数
def logger(flag=''):
    def show_time(f):
        def inner(*a):
            start = time.time()
            f(*a)
            end = time.time()
            print('speed %s' % (end - start))
            if flag=='true':
                print('日志记录')
        return inner
    return show_time
@logger('ture')  #==@showtime
def bar():
    print('bar......')
    time.sleep(2)
bar()


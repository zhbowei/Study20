#__author:  bwzhang
#__date:    2018/6/15

# l = [1,2,3]
# print(l[0])

# s = (x for x in range(10))
# # print(next(s)) #等价于,__next__() in Py2:  s.next()
# print(type(s))
# # 生成器就是一个可迭代对象(interable)
# for i in s: #不断next打印下一个属，打印本次时上一次指向被隔断垃圾清理
#     print(i)
# def foo():
#     print('ok')
#     yield 1
#     print('ok2')
#     yield 2
# g=foo()
# a=next(g)
# b=next(g)
# print(a,b)
# for i in foo():
#     print (i)


# def fib(max):
#     n,before,after = 0,0,1
#     while n < max:
#         # print(after)
#         yield after
#         before,after = after,before+after  #先执行before+after
#         n = n + 1
# g = fib(8)   #<generator object fib at 0x0000025669804C50>
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# def bar():
#     print('ok1')
#     count = yield 1
#     print(count)
#     # print('ok')
#     yield 2
#
# b = bar()
# # next(b)
# b.send(None)  #==next(b)
# b.send('eee')







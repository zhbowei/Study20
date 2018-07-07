#__author:  bwzhang
#__date:    2018/6/26
# import sys
# import calculate,time    #调用模块
# print(calculate.add(1,2))
# print(calculate.x)


# from calculate import add   #从模块调用方法
# print(add(1,4))
# print(calculate.x)

from calculate import add as plus
print(plus(1,5))
# print(x)
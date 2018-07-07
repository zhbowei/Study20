#__author:  bwzhang
#__date:    2018/7/1
# from greenlet import greenlet
#
#
# def a():
#     print(12)
#     gr2.switch()
#     print(34)
#     gr2.switch()
# def b():
#     print(56)
#     gr1.switch()
#     print(78)
#     # gr1.switch()
# gr1 = greenlet(a)
# gr2 = greenlet(b)
# gr1.switch() # 类似于next的方法，去调用生成器并使其保存特定状态
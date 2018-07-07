#__author:  bwzhang
#__date:    2018/6/16

# import time


# print(time.time())  #1529109957.008654时间戳
# time.sleep(3)     #*****
# print(time.clock())   #计算cpu使用时间
# print(time.gmtime())     #结构化时间，utc时间，英国格林尼治，世界标准时间
# print(time.localtime())    #****本地时间
# print(help(time.strftime))
# struct_time = time.localtime()  #****
# print(time.strftime('%Y--%m--%d %H:%M:%S',struct_time))
# print(time.strptime('2018--06--16 10:22:10','%Y--%m--%d %H:%M:%S'))
# a = time.strptime('2018--06--16 10:22:10','%Y--%m--%d %H:%M:%S')
# print(a.tm_year)
# print(a.tm_wday)

# print(time.ctime(3600))   #距离时间戳的时间
# print(time.mktime(time.localtime()))  #距离时间戳的秒数

import datetime

# datetime.datetime.now()
# print(datetime.datetime.now())




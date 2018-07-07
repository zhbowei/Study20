#__author:  bwzhang
#__date:    2018/6/26
import re

source ='1-2'
def check(s):
    flag = True
    if re.findall('[a-zA-Z]',s):
        print('Invalid')
        flag=False
    return flag
def format(s):
    s = s.replace(' ','')
    s = s.replace('++','+')
    return s
def cal_mul_div(s):
    ret1 = re.search('\d+\.?\d*  [*/]   \d+\.?\d*').group()
    x,y=ret1.split('[*/]',ret1)
    #if
    ret2 = float(x)/float(y)
    str(ret2)
    s.replace(ret1,ret2)

def cal_add_sub(s):
    pass

if check(source):
    strs = format(source)
    while re.search('\('):
        re.search('\([^()]\)',strs).group()
        strs = cal_mul_div(strs) #2+15
        strs = cal_add_sub(strs) #"(17)"str[1:-1]
    else:
        str = cal_mul_div(strs)
        strs = cal_add_sub(strs)



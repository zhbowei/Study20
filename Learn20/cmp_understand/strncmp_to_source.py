#__author:  bwzhang
#__date:    2018/7/23
# from past.builtins import cmp
#
# s1 = '1.2.3a'
# s2 = '1.2.3b'
# print(cmp(s1,s2))
def inp():
    s1,s2 = input('请输入任意两个软件版本号大小:').split()
    #print(s1,s2)
    return s1,s2
def strncmp_to_source(s1,s2):
    # s1 = '1.2.3a'
    # s2 = '1.2.3b'
    s1 = s1.split('.')#对软件版本号进行以分割，以‘.’分割
    s2 = s2.split('.')
    # print(s1,s2)#['1', '2', '3a'] ['1', '2', '3b']
    if len(s1)>=len(s2):
        num = len(s2)
    else:
        num = len(s1)
    #判断n的数字位的大小
    for i in range(num):
        # print(s1[i])
        #针对于 s1=[1,2,3a] s2=[1,3,3b]
        if(s2[i]>s1[i]):
            status_code = 1
            return status_code
        #针对于 s1=[1,3,3a] s2=[1,2,3b]
        elif (s2[i]<s1[i]):
            status_code =-1
            return status_code
        else:
            #针对于s1=[1,2,3] s2=[1,2,3]
            if(len(s1)==len(s2)):
                status_code = 0
             #针对于s1=[1,2,3.4a] s2=[1,2,3]
            elif (len(s1)>len(s2)):
                status_code = -1
            else:
            #针对s1=[1,2,3] s2=[1,2,3,4b]
                status_code = 1
    return status_code
def outp(status_code):
    if status_code == 1:
        print('s1<s2')
    elif status_code == 0:
        print('s1=s2')
    else:
        print('s1>s2')
def main():
    while True:
        s1,s2 =  inp()#屏幕随机输入，返回s1，s2
        # s1 = '1.2.3a'
        # s2 = '1.2.3b'
        sta_code = strncmp_to_source(s1,s2)#s1,s2封装到处理数据的函数中，并返还状态码
        # print(sta_code)
        outp(sta_code)#根据状态码判断，输出结果
if __name__ == '__main__':
    main()
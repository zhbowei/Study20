#__author:  bwzhang
#__date:    2018/6/15
# 闭包
def outer(x): # x为外部变量
    x=10      # x为外部变量
    def inner():  #内部函数
        print(x)   #x为外部环境变量
    return inner  #inner为一个闭包
# inner()#inner 为局部变量，全局无法调用
f = outer()
f()

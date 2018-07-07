#__author:  bwzhang
#__date:    2018/6/15
def f(n):
    return n*n
print(f(4))

def foo(a,b,fanc):
    return fanc(a)+fanc(b)
print(foo(1,2,f))

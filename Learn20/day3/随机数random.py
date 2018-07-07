#__author:  bwzhang
#__date:    2018/6/16

import random
# print(random.random())
# print(random.randint(1,8))  #包括8
# print(random.choice([[1,2],[1,2,3],4]))
# print(help(random.randint))
# print(random.sample(['123',4,[1,2]],2))  #设置随机取2个数
# print(random.randrange(1,3))

def v_code():
    code =''
    for i in range(4):
        add= random.choice([random.randrange(10),chr(random.randrange(65,91))])
        # if i ==random.randint(0,3):
        #     add = random.randrange(10)
        # else:
        #     add = chr(random.randrange(65,91))
        code+=str(add)

    print(code)
v_code()



# print(chr(65))


#__author:  bwzhang
#__date:    2018/6/29

# 方法1
# list1 = [1,1,2,3,3,4]
# set1 = set(list1)
# list1 = list(set1)
# print(set1)
# print(list1)
# 方法2
# list2 = []
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list2)

from functools import wraps
def start_word_upper(func):
    @wraps(func)
    def inner(*args,**kwargs):
        word = func(*args,**kwargs)
        return word.capitalize()
    return inner
def greetins(word='i there'):
    return word.lower()
t = greetins()
print(t)
#__author:  bwzhang
#__date:    2018/6/5
# dic = {'name':'alex','age':35,'hobby':'girls'}
#
# print (dic['name'])
# a = list((1,2,3))
# print(a)
# dic2 = dict((('name','alex'),))
# print dic2
# dic1 = {'name':'alex',}
# dic1 ['age'] = 18
# ret2 = dic1.setdefault('hobby','girl')
# print ret2
# print dic1

# cha
# dic3 = {'hobby': 'girl', 'age': 18, 'name': 'alex'}
# print dic3['name']
# # dic3.keys()
# print (list(dic3.keys()))
# print (list(dic3.values()))
# print (list(dic3.items()))

# gai
# dic4 = {'hobby': 'girl', 'age': 18, 'name': 'alex'}
# # dic4 ['age'] = 20
# # print dic4
# dic5 = {'1':'111','name':'222'}
# dic4.update(dic5)
# print dic4

# shan
# dic6 = {'hobby': 'girl', 'age': 18, 'name': 'alex'}
# # del dic6['name']
# # dic6.clear()
# # a = dic6.popitem()
# # print a
# # ret2 = dic6.pop('age')
# # print ret2
# del dic6
# print dic6

# qita fangfa
# dic7 = dict.fromkeys(['host1','host2','host3'],'test')
# print dic7
# dic7['host2'] = 'abc'
# print(dic7)

# dic7 = dict.fromkeys(['host1','host2','host3'],['test1','test2'])
# print dic7
# dic7['host2'][1] = 'test3'
# print(dic7)

# dic8 = {2:666,3:333,4:444}
# print(sorted(dic8.values()))
# print(sorted(dic8.keys()))
# print(sorted(dic8.items()))
# dic9 = {'name':'alex','age':18}
# # xiaolugao
# for i in dic9:
#     print(i,dic9[i])
# # xiaolubugao
# for i,v in dic9.items():
#     print(i,v)

# String操作
#5
# a = '123'
# b = 'abc'
# d = '44'
# c = a + b
# #效率更高
# #c = ''.join([a,b,d])
#
# print c

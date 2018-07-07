#__author:  bwzhang
#__date:    2018/6/6
import json
import pandas as pd
fr = open('json01.txt','r')
dic = {}
for i in fr.readlines():

     jsonmessage = json.loads(i)

print jsonmessage
for keys,values in jsonmessage.items():
    print(keys,values)
# print (type(dic))
# dic2 = {'age':23}
# print (type(dic2))
# print(dic2['age'])
fr.close()



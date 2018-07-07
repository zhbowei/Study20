#__author:  bwzhang
#__date:    2018/7/4

import pymysql
conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',db='music',charset='utf8')
cursor = conn.cursor()
row = cursor.execute('insert into name(name)values("haha")')
print(row)   #row受影响的行数
conn.commit()
cursor.close()
conn.close()


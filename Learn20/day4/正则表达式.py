#__author:  bwzhang
#__date:    2018/6/26

#用于匹配字符串

# s = 'hello world'
# print(s.find('l'))
# ret = s.replace('ll','xx')
# print(ret)
# print(s.split(' '))


import re
#元字符
#.通配符
# ret = re.findall('w..l','hello world')    #.可代之任一字符，除换行符外
# ret = re.findall('w\w{2}l','hello world')
# print(ret)
# ^ 尖角符 （只在开始时匹配）
# ret = re.findall('^h..o','hjaoflhello')
# print(ret)

# $ 只在结束时匹配
# ret  = re.findall('a..x$','hfajklsdhgalexauyx')
# print(ret)

# * 重复匹配,可匹配0到多次
# ret = re.findall('ba.*a','aurqeqirbaaafalfja')
# print(ret)

# + 重复匹配，可匹配1到多次
# ret = re.findall('ba+','gdgdfgcabarere')
# print(ret)

# ? [0,1]
# ret =re.findall('a?b','aaaaabhgabfb')
# print(ret)

# {} 大括号
# ret = re.findall('a{5}b','aaaaaaab')
# print(ret)

# {} 贪婪匹配
# ret = re.findall('a{1,}b','aaaaab') #{1,}什么都不加是到正无穷
# print(ret)
#正则元字符： . ^  $  *  +  ?  {}

#字符集
# ret = re.findall('[a-z]','adx')
# print(ret)

#[] ： 取消元字符的特殊功能(\ ^ ~)
# ret = re.findall('[w,.]','aw.dx*')
# print(ret)

# ret = re.findall('[1-9,a-z,A-Z]','12tyAS')
# print(ret)

# ^ 在[]内用为非的意思
# ret = re.findall('[^3,4]','it234dfsa')
# print(ret)

# \ 根源字符去除特殊意义，后面跟普通字符具有特殊意义，例如/d代表数字
# print(re.findall('\d{11}','dsfsg12345677855'))

# \ \D 匹配任何非数字字符 ， \s 匹配任何空白字符  \ S 空白字符
# \w 匹配任何字母数字字符 \W匹配非字母数字字符 ，\b 匹配一个特殊边界
# print(re.findall(r'\bI','hello,I am a LI#ST'))

#只招符合第一个的位置
# print(re.search('sb','ffdjjsiisfsb')) #<_sre.SRE_Match object; span=(10, 12), match='sb'>
# print(re.search('sb','ffdjjsiisfsb').group())

# ret = re.search('a\+','a+gj').group()
# print(ret)

# ret = re.findall(r'\\','abc\de')
# print(ret)
# m = re.search(r'\bblow','blow')
# print(m)

#()
# print(re.search('(as)+','sdjkfasssas').group())

# import re
# ret = re.search('(?P<id>\d{3})/(?P<name>\w{3})','weeew34ttt123/ooo')
# print(ret.group('id'))
# print(ret.group('name'))

# ret = re.match('asd','asdfegasd')
# print(ret.group())


# split()
# ret = re.split('[j,s]','sdjksal')
# print(ret)

# sub()三个参数
# ret = re.sub('a..x','s..bi','hahhshfalexfh')
# print(ret)

#comple()
# re.findall('\.com','fafsh.comhhshf')
#
# obj = re.compile('\.com')
# ret = obj.findall('fafsh.comhhshf')
# print(ret)
# ret = re.findall('a[bc]d','acd')
# print(ret)
# ret = re.findall('[^ab]','45hgh"ab"dhdh')
# print(ret)

# ret = re.findall('www.(?:\w+).com','www.baidu.com')
# print (ret)

# ret = re.finditer('\d','ds2sdjda3fjs4')
# print (next(ret).group())

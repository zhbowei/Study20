#__author:  bwzhang
#__date:    2018/6/4
print(' ')
name = raw_input('Name:')
age = raw_input('Age:')
job = raw_input('Job:')
salary = raw_input('Salary:')

# if salary.isdigit():
#     salary = int(salary)
# else:
#     print 'er'
#     exit()

msg = '''
-----------info of %s---------
Name: %s
Age:  %s
Job:  %s
Salary: %d
-----------info of %s---------
'''%(name,name,age,job,salary,name)
print msg
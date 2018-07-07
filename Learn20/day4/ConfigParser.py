#__author:  bwzhang
#__date:    2018/6/26




import configparser
config = configparser.ConfigParser()
# config["DEFAULT"] = {'ServerAliveIntarval':'45',
#                      'Compression':'yes',
#                      'CompressionLevel':'9'}
# config['config.org'] = {'user':'hg'}
# config['topsercret.server.com'] = {"host port" : '50022',
#                                    'forwardxll':'no'}
# with open('example.ini','w') as configfile:
#     config.write(configfile)

# config.remove
config.read('example.ini')
print(config.sections())
print(config.defaults())   #OrderedDict有序的字典
for key in config['bitback.org']:
     print(key)





#__author:  bwzhang
#__date:    2018/6/17
# 无法实现屏幕输出
# import logging
# logging.basicConfig(level=logging.WARNING,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a %d %b %Y %H:%M:%S',
#                     filename='test.log',
#                     filemode='a')
# logging.debug('debug message')
# logging.info('info message' )
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')
#可实现屏幕输出

import logging
logger = logging.getLogger()
#创建一个handler，用于写入日志
fh = logging.FileHandler('test.log')
#用于输出到控制台
ch = logging.StreamHandler()

#标准输出格式对象
formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formater)
ch.setFormatter(formater)

logger.addHandler(fh)
# logger.addHandler(ch)
logger.setLevel(logging.DEBUG)
logger.debug('debug message')
logger.info('info message' )
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')










import logging

# logging.basicConfig(level=logging.DEBUG,
#                     format="%(asctime)-15s %(levelname)s %(filename)s[line:%(lineno)d] %(process)d %(message)s",
#                     datefmt="%a %d %b %Y %H:%M:%S",
#                     filename='test.log',
#                     filemode='w')
#
#
# #
# # logging.debug('debug message')
# # logging.info('info message')
# # logging.warn('warn message')
# # logging.error('error message')
# # logging.critical('critical message')



#### 第二种方式：
#创建一个logging对象
logger = logging.getLogger()
formatter = logging.Formatter("%(asctime)-15s %(levelname)s %(filename)s[line:%(lineno)d] %(process)d %(message)s")
 
#创建一个handle,写入文件
fh = logging.FileHandler('test2.log')

#创建一个handle，输出到屏幕
ch = logging.StreamHandler()

fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.setLevel(logging.DEBUG)
logger.addHandler(fh)
logger.addHandler(ch)

logging.debug('debug message')
logging.info('info message')
logging.warn('warn message')
logging.error('error message')
logging.critical('critical message')
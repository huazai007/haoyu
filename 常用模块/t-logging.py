import logging
logging.debug("debug message")
logging.info("info message")
logging.warning("warnng message")
logging.error("error message")
logging.critical("critical message")

#创建一个logger对象
logger=logging.getLogger()
#创建一个文件管理操作符
fh=logging.FileHandler('logger.log',encoding='utf-8')
#创建一个屏幕管理操作符
sh=logging.StreamHandler()
format1=logging.Formatter('%(asctime)s %(name)s - %(levelname)s - %(message)s')

#文件管理操作符 绑定一个格式
fh.setFormatter(format1)
sh.setFormatter(format1)
logger.setLevel(logging.DEBUG)
logger.addHandler(sh)

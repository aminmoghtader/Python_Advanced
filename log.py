import logging

file = "/home/am/Documents/python/advanced/test.log"
log_format = ("%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s")
data_format = "day:%d%H:%M:%S"
logging.basicConfig(filename=file, format=log_format, datefmt=data_format)
logger = logging.getLogger()
logger.warning('this is warning')

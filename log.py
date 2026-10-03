import logging.handlers

file = "Documents/python/advanced/test.log"
log_format = ("%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d " \
"- %(message)s - %(name)s - %(pathname)s - %(process)s - %(processName)s -"\
"%(thread)s - %(threadName)s")
data_format = "day:%d%H:%M:%S"
logging.basicConfig(filename=file, format=log_format, datefmt=data_format)
logger = logging.getLogger(__name__)
logger.warning('this is warning')

num = [1, 2, 3, 4]

try:
    num[4] += 1
except Exception as e:
    logger.error("Exeption occurred", exc_info=True)

f_handler = logging.handlers.RotatingFileHandler('test1.log',\
                        maxBytes= 5 * 1024, backupCount=4)
s_handler = logging.StreamHandler()

f_handler.setLevel(logging.WARNING)
s_handler.setLevel(logging.ERROR)

f_format = logging.Formatter("%(asctime)s - %(levelname)s - \
                             %(filename)s:%(lineno)d")

s_format = logging.Formatter("%(asctime)s - %(message)s")
f_handler.setFormatter(f_format)
s_handler.setFormatter(s_format)

logger.addHandler(f_handler)
logger.addHandler(s_handler)

while True:
    logger.warning("Warning Log")

import logging.config
import yaml

file = 'Documents/python/advanced/config.yaml'
with open (file, 'r') as f:
    config = yaml.safe_load(f.read())

logging.config.dictConfig(config)
f_logger = logging.getLogger('f_logger')
s_logger = logging.getLogger('s_logger')

f_logger.warning('Warning Log')
s_logger.warning('Warning Log')


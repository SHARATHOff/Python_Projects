import logging


logging.basicConfig(filename="mylog.log",format='%(asctime)s:%(message)s',filemode='w')
logger = logging.getLogger()

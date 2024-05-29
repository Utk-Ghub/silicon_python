import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

h = logging.FileHandler('logtest.log')
logger.addHandler(h)

def do_something():
    logging.info('from logtest4 info')
    logger.info('from logtest4')
    logger.debug('from logtest4 debug')
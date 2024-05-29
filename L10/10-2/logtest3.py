import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def do_something():
    logger.info('from logtest3')
    logger.debug('from logtest3 debug')
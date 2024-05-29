import logging

import logtest4

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('from main')
logtest4.do_something()
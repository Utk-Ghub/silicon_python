import logging

import logtest3
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)
logger.info('from main')

logtest3.do_something()
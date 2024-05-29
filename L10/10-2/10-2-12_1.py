import logging

import logtest1

logging.basicConfig(level=logging.INFO)
logging.info('info')
logtest1.do_something()
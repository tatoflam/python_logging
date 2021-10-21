from logging import getLogger

logger = getLogger(__name__)

def sample5_func():
    print(__name__)
    logger.debug("this is logged by sample5_called")


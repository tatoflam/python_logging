from logging import config, getLogger
from sample5.sample5_called import sample5_func

config.fileConfig('sample5/logging5.conf')
logger = getLogger(__name__)

def main():
    logger.debug("this is logged by main()")
    sample5_func()

if __name__ == '__main__':
    main()
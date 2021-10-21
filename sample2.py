from logging import config, getLogger
from sample2_called import sample2_func

config.fileConfig('logging2.conf')
#logger = getLogger()
logger = getLogger(__name__)

def main():
    logger.debug("this is logged by main()")
    sample2_func()    

if __name__ == '__main__':
    main()
from logging import config, getLogger
from sample4_called import sample4_func

config.fileConfig('logging4.conf')
#logger = getLogger()
logger = getLogger("sampleLogger")

def main():
    logger.debug("this is logged by main()")
    sample4_func()    

if __name__ == '__main__':
    main()
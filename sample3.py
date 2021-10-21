from logging import config, getLogger
from sample3_called import sample3_func

config.fileConfig('logging3.conf')
#logger = getLogger()
logger = getLogger("sampleLogger")

def main():
    logger.debug("this is logged by main()")
    sample3_func()    

if __name__ == '__main__':
    main()
from logging import config, getLogger

config.fileConfig('logging.conf')
#logger = getLogger()
logger = getLogger(__name__)

def main():
    logger.debug("this is logged by main()")

if __name__ == '__main__':
    main()
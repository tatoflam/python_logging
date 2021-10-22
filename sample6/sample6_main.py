import json
from logging import config, getLogger
from sample6.sample6_called import sample6_func

config_dict = None
with open('sample6/logging_conf.json', 'r', encoding='utf-8') as f:
    config_dict = json.load(f)

config.dictConfig(config_dict)
logger = getLogger(__name__)

def main():
    logger.debug("this is logged by main()")
    sample6_func()

if __name__ == '__main__':
    main()
import logging
import logging.config
import json

with open('logging_config.json', 'rt') as file:
    config = json.load(file)
    logging.config.dictConfig(config)
logger = logging.getLogger(__name__)


def main():
    logger.debug("hi")
    import package1.test
    package1.test.log_test_message()


if __name__ == '__main__':
    main()

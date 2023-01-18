import logging
from core.config import WebAppConfig as c
from core.logging.log_handler import LogMongoHandler

logger = logging.getLogger('root')


def logging_init():
    set_logging_lvl(c.LOGGING_LEVEL)
    logger.addHandler(LogMongoHandler())


def set_logging_lvl(level='DEBUG'):
    logger.setLevel(level)
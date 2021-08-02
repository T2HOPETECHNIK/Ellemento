from logging import log
from lib.logging.logger_initialiser import EllemengtoLogger

if __name__ == '__main__':
    logger = EllemengtoLogger.initialize_logger()
    logger.info("test") 
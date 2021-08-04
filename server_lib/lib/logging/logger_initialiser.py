import logging
import os.path
from datetime import datetime

from logging.handlers import TimedRotatingFileHandler

"""
    Usage instructions:

    import logger_initialiser

    logging = logger_initialiser.initialize_logger(PATH_TO_LOG_FILE)
    logging.debug("debug message")
    logging.info("info message")ls
    logging.warning("warning message")
    logging.error("error message")
    logging.critical("critical message")

"""

class EllementoLogger(object):  
    log_folder = os.path.join(os.path.dirname(__file__), "log")

    def __init__ (self):
        super().__init__()
     


    @staticmethod
    def initialize_logger(output_dir = os.path.dirname(__file__), log_file_name = "debug"):
        """ Initialises the log to do the following:
            (1) Output all log levels (from DEBUG upwards) to stdout
            (2) Log ERROR and CRITICAL messages to file
        """
        LOG_FORMAT = "[%(levelname)s] - %(message)s - %(asctime)s"
        str_date = datetime.today().strftime('%Y-%m-%d')
        LOG_DEBUG_FILE = log_file_name + "_" + str_date + ".log"
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        # create console handler and set level to debug
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(LOG_FORMAT)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Creates output directory if it does not exist
        output_dir = os.path.join(output_dir, "log"); 
        EllementoLogger.log_folder = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # create error file handler and set level to error
        handler = TimedRotatingFileHandler(
            os.path.join(output_dir, LOG_DEBUG_FILE),
            when="midnight",
            encoding=None,
            interval=1,
            delay="true",
            backupCount=30)
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(LOG_FORMAT)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        return logger
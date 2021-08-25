import logging
import os.path
from datetime import datetime

from logging.handlers import TimedRotatingFileHandler


class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

# python 3 style
class EllementoLogger(object, metaclass=SingletonType):
    # __metaclass__ = SingletonType   # python 2 Style
    _logger = None


    def __init__(self, log_file_name = "debug", log_lvl = logging.DEBUG, output_dir = os.path.dirname(__file__)):
        """ Initialise the log to do the following:
            (1) Output all log levels (from DEBUG upwards) to stdout
            (2) Log ERROR and CRITICAL messages to file
        """
        LOG_FORMAT = "[%(levelname)s] - %(message)s - %(asctime)s"
        str_date = datetime.today().strftime('%Y-%m-%d')
        LOG_DEBUG_FILE = log_file_name + "_" + str_date + ".log"
        logger = logging.getLogger()
        logger.propagate = False 
        logger.setLevel(log_lvl)
        # create console handler and set level to debug
        handler = logging.StreamHandler()
        handler.setLevel(log_lvl)
        formatter = logging.Formatter(LOG_FORMAT)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Creates output directory if it does not exist
        output_dir = os.path.join(output_dir, "log"); 
        self._log_folder = output_dir
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
        handler.setLevel(log_lvl)
        formatter = logging.Formatter(LOG_FORMAT)
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        self._logger = logger
    
    @property
    def logger(self):
        return self._logger

    @property 
    def log_folder(self): 
        return self._log_folder


# class EllementoLogger(object):  
#     log_folder = os.path.join(os.path.dirname(__file__), "log")
#     logger = None 

#     def __init__ (self):
#         super().__init__()
     


#     @staticmethod
#     def initialize_logger(log_file_name = "debug", log_lvl = logging.DEBUG, output_dir = os.path.dirname(__file__)):
#         """ Initialise the log to do the following:
#             (1) Output all log levels (from DEBUG upwards) to stdout
#             (2) Log ERROR and CRITICAL messages to file
#         """
#         if EllementoLogger.logger is not None: 
#             return EllementoLogger.logger
#         LOG_FORMAT = "[%(levelname)s] - %(message)s - %(asctime)s"
#         str_date = datetime.today().strftime('%Y-%m-%d')
#         LOG_DEBUG_FILE = log_file_name + "_" + str_date + ".log"
#         logger = logging.getLogger()
#         logger.propagate = False 
#         logger.setLevel(log_lvl)
#         # create console handler and set level to debug
#         handler = logging.StreamHandler()
#         handler.setLevel(log_lvl)
#         formatter = logging.Formatter(LOG_FORMAT)
#         handler.setFormatter(formatter)
#         logger.addHandler(handler)

#         # Creates output directory if it does not exist
#         output_dir = os.path.join(output_dir, "log"); 
#         EllementoLogger.log_folder = output_dir
#         if not os.path.exists(output_dir):
#             os.makedirs(output_dir)

#         # create error file handler and set level to error
#         handler = TimedRotatingFileHandler(
#             os.path.join(output_dir, LOG_DEBUG_FILE),
#             when="midnight",
#             encoding=None,
#             interval=1,
#             delay="true",
#             backupCount=30)
#         handler.setLevel(log_lvl)
#         formatter = logging.Formatter(LOG_FORMAT)
#         handler.setFormatter(formatter)

#         logger.addHandler(handler)
#         EllementoLogger.logger = logger; 
#         return EllementoLogger.logger
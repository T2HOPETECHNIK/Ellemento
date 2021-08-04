from logging import log
import unittest
import os 

from lib.logging.logger_initialiser import EllemengtoLogger


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        log_folder = os.path.join(os.path.dirname(__file__), "log")
        logger = EllemengtoLogger.initialize_logger(os.path.dirname(__file__)); 
        logger.info("test")
        self.assertEqual(EllemengtoLogger.log_folder, log_folder)
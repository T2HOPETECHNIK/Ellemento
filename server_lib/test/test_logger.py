from logging import log
import unittest
import os 

from lib.logging.logger_initialiser import EllementoLogger


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        #log_folder = os.path.join(os.path.dirname(__file__) + "..\\..\\lib\\logging", "log")
        #logger = EllementoLogger.initialize_logger(os.path.dirname(__file__)); 

        logger = EllementoLogger.__call__().logger
        al = EllementoLogger()
        al.logger.info("test")
        self.assertEqual(EllementoLogger.__call__().log_folder, EllementoLogger.__call__().log_folder)
        #self.assertEqual(EllementoLogger.log_folder, log_folder)
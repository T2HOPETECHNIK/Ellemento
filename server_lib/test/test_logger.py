from logging import log
import unittest
import os 

from lib.logging.logger_initialiser import EllementoLogger


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        log_folder = os.path.join(os.path.dirname(__file__), "log")
        logger = EllementoLogger.initialize_logger(os.path.dirname(__file__)); 
        self.assertEqual(EllementoLogger.log_folder, log_folder)
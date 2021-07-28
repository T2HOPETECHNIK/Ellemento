import unittest

from ellemento.model.tray import *


class TestTray(unittest.TestCase):

    def test_tray(self):
        tray_1 = Tray(1)
        self.assertEqual(tray_1.id, 1)
    
    def test_tray_id(self):
        tray_1 = Tray(1)
        tray_1.id = 2
        self.assertEqual(tray_1.id, 2)


if __name__ == '__main__':
    unittest.main()
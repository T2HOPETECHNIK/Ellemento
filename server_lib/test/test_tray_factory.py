import unittest

from ellemento.model.tray_factory import *

class TestTrayFactory(unittest.TestCase):
    def test_tray_creation_success(self):
        tray_1 = TrayFactory.create_tray(id = 1, type_name = "phase1")
        self.assertEqual(tray_1.id, 1)
        self.assertEqual(tray_1.type_name, "phase1-3")

    def test_tray_creation_invalid_type_1(self):
        with self.assertRaises(TypeError) as cm:
            tray_new = TrayFactory.create_tray(id = 1, type_name = "phase-1")

    def test_tray_creation_invalid_type_2(self):
        with self.assertRaises(TypeError) as cm:
            tray_new = TrayFactory.create_tray(id = 1, type_name = "xxx")
        

if __name__ == '__main__':
    unittest.main()
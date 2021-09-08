import unittest

from ellemento.model.shelf_factory import *

class TestShelfFactory(unittest.TestCase):
    def test_tray_creation_success(self):
        shelf_1 = ShelfFactory.create_shelf(id = 1)
        self.assertEqual(shelf_1.id, 1)
        self.assertEqual(shelf_1.type_name, "default")

if __name__ == '__main__':
    unittest.main()
from ellemento.plc.modbus_io_manager import ModbusIOManager
import unittest

class TestModbusIOManangerMethods(unittest.TestCase):

    def test_upper(self):
        num_plc = ModbusIOManager.create_modbus_io()
        self.assertEqual(num_plc, 2)

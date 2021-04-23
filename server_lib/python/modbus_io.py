from pymodbus.client.sync import ModbusTcpClient
from pymodbus.constants import Defaults
from pymodbus.exceptions import ModbusException
from pymodbus.client.common import ModbusClientMixin
from pymodbus.bit_read_message import ReadCoilsResponse, ReadDiscreteInputsResponse
from pymodbus.register_read_message import ReadHoldingRegistersResponse, ReadInputRegistersResponse
from pymodbus.register_read_message import ReadWriteMultipleRegistersResponse
from pymodbus.bit_write_message import WriteSingleCoilResponse, WriteMultipleCoilsResponse
from pymodbus.register_write_message import WriteSingleRegisterResponse, WriteMultipleRegistersResponse

class plc(object):

    def __init__ (self):
        super().__init__()

    def __del__(self):
        print ("plc destructor")

    def setIP(self, ip):
        error = 0
        try:
            self.client = ModbusTcpClient(ip)
        except:
            error = 1
        
        return error

    def write_register(self, addr, data):
        error = 0
        try:
            res = self.client.write_registers(addr, data, unit=1)
        except:
            error = 1
        return res, error

    def read_register(self, addr, size):
        error = 0
        try:
            res = self.client.read_holding_registers(addr, size, unit=1)
        except:
            error = 1
        return res, error
    
    

   
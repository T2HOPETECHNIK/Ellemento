from pymodbus.client.sync import ModbusTcpClient
from pymodbus.constants import Defaults
from pymodbus.exceptions import ModbusException
from pymodbus.client.common import ModbusClientMixin
from pymodbus.bit_read_message import ReadCoilsResponse, ReadDiscreteInputsResponse
from pymodbus.register_read_message import ReadHoldingRegistersResponse, ReadInputRegistersResponse
from pymodbus.register_read_message import ReadWriteMultipleRegistersResponse
from pymodbus.bit_write_message import WriteSingleCoilResponse, WriteMultipleCoilsResponse
from pymodbus.register_write_message import WriteSingleRegisterResponse, WriteMultipleRegistersResponse

class PLCManager(object):

    def __init__ (self, name = "rack1", id = 1):
        super().__init__()
        self.name = name 
        self.id = id

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
        res = 0
        try:
            res = self.client.write_registers(addr, data, unit=1)
            assert(res.function_code < 0x80)     # test that we are not an error
        except:
            error = 1
        return res, error


    def read_register(self, addr, size):
        error = 0
        res = 0
        try:
            res = self.client.read_holding_registers(addr, size, unit=1)
        except:
            error = 1
        return res, error


    def bitvalue(self, bitpos):
        return (32768 >> (15-bitpos))


    # Self implemented coil
    def write_coil(self, addr, bitpos, bdata):

        error = 0
        res = 0
        try:
            binvalue = self.bitvalue(bitpos)
            res = self.client.read_holding_registers(addr, 1, unit=1)
            data = res.registers[0] # read current value
            if bdata == True:
                data = data | binvalue
            else:
                data = data ^ binvalue

            res = self.client.write_register(addr, data, unit=1)
            assert(res.function_code < 0x80)     # test that we are not an error

        except:
            error = 1
        return res, error


    # Self implemented coil
    def read_coil(self, addr, bitpos):
        error = 0
        bres = False
        try:
            binvalue = self.bitvalue(bitpos)
            res = self.client.read_holding_registers(addr, 1)
            andresult = (res.registers[0] & binvalue)

            if andresult == 0:
                bres = False
            else:
                bres = True
        except:
            error = 1
        return bres, error


    '''
    def write_system_coil(self, addr, val):
        error = 0
        try:
            res = self.client.write_coil(addr,val)
        except:
            print("write_coil error")
            error = 1
        return res,error


    def read_system_coil(self, addr):
        error = 0
        try:
            res = self.client.read_coils(addr, 1)
        except:
            print("read_coil error")
            error = 1

        return res, error
    '''



    








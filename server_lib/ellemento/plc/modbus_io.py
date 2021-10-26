import json 
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.constants import Defaults
from pymodbus.exceptions import ModbusException
from pymodbus.client.common import ModbusClientMixin
from pymodbus.bit_read_message import ReadCoilsResponse, ReadDiscreteInputsResponse
from pymodbus.register_read_message import ReadHoldingRegistersResponse, ReadInputRegistersResponse
from pymodbus.register_read_message import ReadWriteMultipleRegistersResponse
from pymodbus.bit_write_message import WriteSingleCoilResponse, WriteMultipleCoilsResponse
from pymodbus.register_write_message import WriteSingleRegisterResponse, WriteMultipleRegistersResponse
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian


class PLCManager(object):
    # name = '', id = '', ip = '', cfg = cfg_json
    def __init__ (self, **kwargs):
        super().__init__()
        self.__name = ''
        self.__id = -1
        self.__ip = "0.0.0.0"
        self.__parse_args(**kwargs)
        self.setIP(self.__ip)
       
   
    def __parse_args(self, **kwargs): 
        for key, value in kwargs.items():
            if key == 'name': 
                self.__name = value
            if key == "id": 
                self.__id = value
            if key == 'ip':
                self.__ip = value
            if key == 'cfg':
                self.__cfg = value
                self.__parse_config(value)
       
    def __parse_config(self, cfg): 
        self.__name = cfg['name']
        self.__id = cfg['id']
        self.__ip = cfg['ip']
        self.__address = cfg['address']
        self.__cfg = cfg; 
        pass
        # to do 
    
    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value  

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property 
    def config(self):
        return self.__cfg; 

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def ip(self):
        return self.__ip

    @ip.setter
    def ip(self, value):
        self.__ip = value
    
    def __print__(self):
        return json.dumps(self.__cfg)
        #return json.dump(self.__cfg)

    def __repr__(self):
        return json.dumps(self.__cfg)
        #return "------"
        
        # print("id  : %d", self.__id)
        # print("name: " + self.__name)
        # print("ip  : " + self.__ip)


    def __del__(self):
        pass
        #print ("plc destructor")

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
            print(res)
            assert(res.function_code < 0x80)     # test that we are not an error
        except:
            error = 1
        return res, error


    def read_register(self, addr, size):
        error = 0
        res = 0
        try:
            res = self.client.read_holding_registers(addr, count = size, unit=8)
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
                data = data & (65535 ^ binvalue)

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



    








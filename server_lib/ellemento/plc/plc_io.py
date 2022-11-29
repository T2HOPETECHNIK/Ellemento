from pymodbus.client.sync import ModbusTcpClient
import pyads
import time


class PLCManager(object):
    def __init__(self, **kwargs):
        super().__init__()
        self.modbus_client = None
        self.twincat_client = None
        self.__name = ''
        self.__id = -1
        self.__ip = "0.0.0.0"
        self.__ads = ""
        self.__parse_args(**kwargs)
        self.setIP(self.__ip, self.__id, self.__ads)

    def __parse_args(self, **kwargs):
        for key, value in kwargs.items():
            if key == 'name':
                self.__name = value
            if key == "id":
                self.__id = value
            if key == 'ip':
                self.__ip = value
            if key == 'ads':
                self.__ads = value
            if key == 'cfg':
                self.__cfg = value
                self.__parse_config(value)

    def __parse_config(self, cfg):
        self.__name = cfg['name']
        self.__id = cfg['id']
        self.__ip = cfg['ip']
        self.__ads = cfg['ads']
        self.__address = cfg['address']
        self.__cfg = cfg
        pass

    @property
    def config(self):
        return self.__cfg

    def setIP(self, ip, id, ads):
        error = 0
        try:
            'creating twinCAT modbus_client'
            if id >= 20:
                self.twincat_client = pyads.Connection(ads, pyads.PORT_TC3PLC1, ip)
                self.twincat_client.open()
            'creating modbus modbus_client'
            if id < 20:
                self.modbus_client = ModbusTcpClient(ip)
        except:
            error = 1
        return error

    def write_register(self, address, data):
        error = 0
        res = 0
        try:
            res = self.modbus_client.write_registers(address, data, unit=1)
            print(res)
            assert (res.function_code < 0x80)  # test that we are not an error
        except:
            error = 1
        return res, error

    def read_register(self, address, size):
        error = 0
        res = 0
        try:
            res = self.modbus_client.read_holding_registers(address, count=size, unit=8)
        except:
            error = 1
        return res, error

    def bitvalue(self, bitpos):
        return 32768 >> (15 - bitpos)

    # Self implemented coil
    def write_coil(self, address, bitpos, bdata):
        error = 0
        res = 0
        try:
            binvalue = self.bitvalue(bitpos)
            res = self.modbus_client.read_holding_registers(address, 1, unit=1)
            data = res.registers[0]  # read current value
            if bdata:
                data = data | binvalue
            else:
                data = data & (65535 ^ binvalue)
            res = self.modbus_client.write_register(address, data, unit=1)
            assert (res.function_code < 0x80)  # test that we are not an error
        except:
            error = 1
        return res, error

    def write_direct_coil(self, address, Value):
        hell = self.modbus_client.write_coil(address, Value)
        print(hell)

    # Self implemented coil
    def read_coil(self, address, bitpos):
        error = 0
        bres = False
        try:
            binvalue = self.bitvalue(bitpos)
            res = self.modbus_client.read_holding_registers(address, 1)
            andresult = (res.registers[0] & binvalue)
            if andresult == 0:
                bres = False
            else:
                bres = True
        except:
            error = 1
        return bres, error

    def write_system_coil(self, address, val):
        error = 0
        try:
            res = self.modbus_client.write_coil(address, val)
        except:
            print("write_coil error")
            error = 1
        return res, error

    def read_system_coil(self, address):
        error = 0
        try:
            res = self.modbus_client.read_coils(address, 1)
        except:
            print("read_coil error")
            error = 1
        return res, error

    def read_plctag(self, address, type):
        if type == 'int':
            tag_type = pyads.PLCTYPE_INT
        elif type == 'bool':
            tag_type = pyads.PLCTYPE_BOOL
        result = self.twincat_client.read_by_name(address, tag_type)
        time.sleep(3)
        print("beckhoff_read_result",address, result)
        return result

    def write_plctag(self,address,value,type):
        if type == 'int':
            tag_type = pyads.PLCTYPE_INT
        elif type == 'bool':
            tag_type = pyads.PLCTYPE_BOOL
        else:
            raise "data type not found"
            return
        if type == 'bool' and value > 1:
            raise "please input boolean"
            return
        self.twincat_client.write_by_name(address,value,tag_type)

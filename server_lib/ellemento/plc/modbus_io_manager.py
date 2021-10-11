import json 
import os
import sys 
from ellemento.plc.modbus_io import PLCManager
from lib.logging.logger_initialiser import EllementoLogger

logger = EllementoLogger.__call__().logger

# Used to hold all the modbus io 
class ModbusIOManager(object):  
    modbus_io_dict = {}; 
    
    def __init__ (self):
        super().__init__()

      # name = '', id = '', ip = '',

    @staticmethod
    def get_modbus_io(**kwargs):
         for key, value in kwargs.items():
            if key == 'name': 
                return ModbusIOManager.modbus_io_dict[value]
            if key == "id": 
                return ModbusIOManager.modbus_io_dict[value]
            if key == 'ip':
                return ModbusIOManager.modbus_io_dict[value]

    @staticmethod
    def print_modbus_io(): 
        for key, value in ModbusIOManager.modbus_io_dict.items():
            print(key, ':')
            print(value)


    @staticmethod
    def create_modbus_io(): 
        # to do - Load all mod bus from init file 
        # read json file 
        # Create PLCS
        # add to the dict 
        try:
            script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
            init_file = script_dir + "\\" + "address.json"
            logger.info(init_file)
            json_file = open(init_file)
            cfg = json.load(json_file)
            json_file.close()
            for x in cfg['modbus']: 
                plc_from_json = PLCManager(cfg = x)
                print(x['ip'])
                #print(cfg)
                ModbusIOManager.modbus_io_dict[x['name']] = plc_from_json 
                ModbusIOManager.modbus_io_dict[x['id']] = plc_from_json
                ModbusIOManager.modbus_io_dict[x['ip']] = plc_from_json
            return len(cfg['modbus'])
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise 
    
    def __add_modbus_io(self, plc):
        # add pic to the master list 
        ModbusIOManager.create_modbus_io[plc.id] = plc; 

    def __get_modbus_io(self, id): 
        return ModbusIOManager.create_modbus_io[id]


import json 
import os

from ellemento.plc.modbus_io import PLCManager


# Used to hold all the modbus io 
class ModbusIOManager(object):  
    modbus_io_dict = [[]]; 

    def __init__ (self):
        super().__init__()
        json.load()
        

    @staticmethod
    def create_modbus_io(): 
        # to do - Load all mod bus from init file 
        # read json file 
        # Create PLCS
        # add to the dict 
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        init_file = script_dir + "\\" + "address.json"
        print(init_file)
        json_file = open(init_file)
        cfg = json.load(json_file)
        json_file.close()
        
        #print(cfg['modbus'][0])
        return len(cfg['modbus'])
        pass  
    
    def __add_modbus_io(self, plc):
        # add pic to the master list 
        ModbusIOManager.create_modbus_io[plc.id] = plc; 

    def __get_modbus_io(self, id): 
        return ModbusIOManager.create_modbus_io[id]


# The code here is to bridge plc and 
# Global libary import 
import json 
import os
import sys 

# Local library import 
from ellemento.bridge.plc_bridge import ModelPlcBridge
from lib.logging.logger_initialiser import EllementoLogger
from ellemento.plc.modbus_io_manager import ModbusIOManager

logger = EllementoLogger.__call__().logger



class LightModelPlcBridge(ModelPlcBridge):
    ModelPlcDict = {}
    
    def __init__(self, id = -1, type_name = "Default", light_id = -1, plc_id = -1, address = None):                   
        self._id        = id
        self._type_name = type_name
        self._light_id  = light_id
        self._plc_id    = plc_id 
        self.modbus_io  = ModbusIOManager.get_modbus_io(id = self._plc_id)
        self.address    = address

    def print_model(self, type = "Light", id = 1): 
        print(self.cfg[type])
        #all_lights = json.load(self.cfg[type])
        #print(all_lights)

    def on_light(self): 
        pass 

    def off_light(self): 
        pass 

    def dim_light(self): 
        pass 

    def bright_light(self ):
        pass 

    def intensity(self): 
        pass

    def on_off_status(self): 
        print(self.address['on']['tag'])
        print(self.modbus_io.config)
        register_address = self.modbus_io.config['address']['SHELF_LIGHT_ON_OFF_FEEDBACK']['position']
        res, error = self.modbus_io.read_register(register_address, 1)
        print(register_address)
        print(res.registers)
        #self.modbus_io. 
        pass 

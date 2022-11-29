# bridge for water control and plc control 

# Global libary import 

import json 
import os
import sys 

# Local library import 
from ellemento.bridge.plc_bridge import ModelPlcBridge
from lib.logging.logger_initialiser import EllementoLogger
from ellemento.plc.plc_io_manager import PlcIOManager

logger = EllementoLogger.__call__().logger

class ValveModelPlcBridge(ModelPlcBridge):
    ModelPlcDict = {}
    
    def __init__(self, id = -1, type_name = "Default", valve_id = -1, plc_id = -1, address = None):                   
        self._id        = id
        self._type_name = type_name
        self._valve_id  = valve_id
        self._plc_id    = plc_id 
        self.modbus_io  = PlcIOManager.get_plc_io(id = self._plc_id)
        self.address    = address

    def on_valve(self):
        tag_name = self.address['control']['tag']
        location = self.address['control']['position'] 
        register_address = self.modbus_io.config['address'][tag_name]['position']
        res, error = self.modbus_io.write_coil(register_address, location, True)
        return res, error 

    def off_valve(self): 
        tag_name = self.address['control']['tag']
        location = self.address['control']['position'] 
        register_address = self.modbus_io.config['address'][tag_name]['position']
        res, error = self.modbus_io.write_coil(register_address, location, False)
        return res, error

    def set_percentage(self, percent): 
        tag_name = self.address['control_rpm']['tag']
        location = self.address['control_rpm']['position']
        register_address = self.modbus_io.config['address'][tag_name][location]
        print("------", register_address)
        res, error = self.modbus_io.write_address_json(register_address, percent)
        ret = True  
        if error: 
            ret = False
        return ret, error 


    # Read intensity value of lights 
    def get_percentage(self): 
        tag_name = self.address['control_rpm']['tag']
        location = self.address['control_rpm']['position']
        register_address = self.modbus_io.config['address'][tag_name][location]
        res, error = self.modbus_io.read_address_json(register_address, 1)
        ret = None 
        if not error: 
            ret = res.registers[0]
        return ret, res 
        
    # Read of/off status of the lights 
    def on_off_status(self): 
        # To do, not having for the moment 
        pass 
        # tag_name = self.address['status']['tag']
        # location = self.address['status']['position']
        # register_address = self.plc_io.config['address'][tag_name]['position']
        # res, error = self.plc_io.read_coil(register_address, location)
        # return res, error 
     

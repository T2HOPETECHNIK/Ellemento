# bridge for water control and plc control 

# Global libary import 

import json 
import os
import sys 

# Local library import 
from ellemento.bridge.plc_bridge import ModelPlcBridge
from lib.logging.logger_initialiser import EllementoLogger
from ellemento.plc.modbus_io_manager import ModbusIOManager

logger = EllementoLogger.__call__().logger

class ShelfModelPlcBridge(ModelPlcBridge):
    ModelPlcDict = {}
    
    def __init__(self, id = -1, type_name = "Default", shelf_id = -1, plc_id = -1, address = None):                   
        self._id        = id
        self._type_name = type_name
        self._shelf_id  = shelf_id
        self._plc_id    = plc_id 
        self.modbus_io  = ModbusIOManager.get_modbus_io(id = self._plc_id)
        self.address    = address
     
    def use_scheduler(self): 
        tag_name = self.address['use_scheduler']['tag']
        tag_position = self.address['use_scheduler']['position']
        register_address = self.modbus_io.config['address'][tag_name]
        res, error = self.modbus_io.write_coil(register_address, tag_position, True)
        return res, error

    def set_pv_on_hh(self):
        tag_name = self.address['pv_on_hh']['tag']
        tag_position = self.address['pv_on_hh']['position']
        register_address = self.modbus_io.config['address'][tag_name]
        res, error = self.modbus_io.write_register(register_address, tag_position, True)
        return res, error
    
    def set_pv_on_mm(self): 
        tag_name = self.address['pv_on_mm']['tag']
        tag_position = self.address['pv_on_mm']['position']
        register_address = self.modbus_io.config['address'][tag_name]
        res, error = self.modbus_io.write_register(register_address, tag_position, True)
        return res, error

    def set_pv_off_hh(self): 
        tag_name = self.address['pv_off_hh']['tag']
        tag_position = self.address['pv_off_hh']['position']
        register_address = self.modbus_io.config['address'][tag_name]
        res, error = self.modbus_io.write_register(register_address, tag_position, True)
        return res, error

    def set_pv_off_mm(self): 
        tag_name = self.address['pv_off_mm']['tag']
        tag_position = self.address['pv_off_mm']['position']
        register_address = self.modbus_io.config['address'][tag_name]
        res, error = self.modbus_io.write_register(register_address, tag_position, True)
        return res, error

    def set_schedule_pv_value(self): 
        tag_name = self.address['schedule_pv_value']['tag']
        tag_position = self.address['schedule_pv_value']['position']
        register_address = self.modbus_io.config['address'][tag_name]
        res, error = self.modbus_io.write_register(register_address, tag_position, True)
        return res, error

    def set_light_on_hh(self): 
        tag_name = self.address['light_on_hh']['tag']
        tag_position = self.address['light_on_hh']['position']
        register_address = self.modbus_io.config['address'][tag_name]
        res, error = self.modbus_io.write_register(register_address, tag_position, True)
        return res, error

    def set_light_on_mm(self):
        tag_name = self.address['light_on_mm']['tag']
        tag_position = self.address['light_on_mm']['position']
        register_address = self.modbus_io.config['address'][tag_name]
        res, error = self.modbus_io.write_register(register_address, tag_position, True)
        return res, error

    def set_light_off_hh(self): 
        tag_name = self.address['light_off_hh']['tag']
        tag_position = self.address['light_off_hh']['position']
        register_address = self.modbus_io.config['address'][tag_name]
        res, error = self.modbus_io.write_register(register_address, tag_position, True)
        return res, error

    def set_light_off_mm(self): 
        tag_name = self.address['light_off_mm']['tag']
        tag_position = self.address['light_off_mm']['position']
        register_address = self.modbus_io.config['address'][tag_name]
        res, error = self.modbus_io.write_register(register_address, tag_position, True)
        return res, error

    def set_scheule_light_intensity(self):
        tag_name = self.address['schedule_light_intensity']['tag']
        tag_position = self.address['schedule_light_intensity']['position']
        register_address = self.modbus_io.config['address'][tag_name]
        res, error = self.modbus_io.write_register(register_address, tag_position, True)
        return res, error


    

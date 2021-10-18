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
    
    def __init__(self, id = -1, type_name = "Default", valve_id = -1, plc_id = -1, address = None):                   
        self._id        = id
        self._type_name = type_name
        self._valve_id  = valve_id
        self._plc_id    = plc_id 
        self.modbus_io  = ModbusIOManager.get_modbus_io(id = self._plc_id)
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
        res, error = self.modbus_io.write_register(register_address, percent)
        ret = True  
        if error: 
            ret = False
        return ret, error 


    # Read intensity value of lights 
    def get_percentage(self): 
        tag_name = self.address['control_rpm']['tag']
        location = self.address['control_rpm']['position']
        register_address = self.modbus_io.config['address'][tag_name][location]
        res, error = self.modbus_io.read_register(register_address, 1)
        ret = None 
        if not error: 
            ret = res.registers[0]
        return ret, res 
        
    # Read of/off status of the lights 
    def on_off_status(self): 
        tag_name = self.address['apply_update']['tag']
        pass 
        # tag_name = self.address['status']['tag']
        # location = self.address['status']['position']
        # register_address = self.modbus_io.config['address'][tag_name]['position']
        # res, error = self.modbus_io.read_coil(register_address, location)
        # return res, error 
     
    def set_control_section_mode(self):
        tag_name = self.address['CTRL_SECTION_MODE']['tag']
        location = self.address['CTRL_SECTION_MODE']['position']
        register_address = self.modbus_io.config['address'][tag_name][location]
        res, error = self.modbus_io.read_register(register_address, 1)
        ret = None 
        if not error: 
            ret = res.registers[0]
        return ret, res 

    def appy_update(self): 
        tag_name = self.address['apply_update']['tag']
        register_address = self.modbus_io.config['address'][tag_name]
        res, error = self.modbus_io.write_system_coil(register_address, True)
        return res, error 
    
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


    

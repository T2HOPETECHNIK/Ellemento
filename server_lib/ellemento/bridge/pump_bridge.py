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

class PumpModelPlcBridge(ModelPlcBridge):
    ModelPlcDict = {}
    
    def __init__(self, id = -1, type_name = "Default", valve_id = -1, plc_id = -1, address = None):                   
        self._id        = id
        self._type_name = type_name
        self._valve_id  = valve_id
        self._plc_id    = plc_id 
        self.modbus_io  = ModbusIOManager.get_modbus_io(id = self._plc_id)
        self.address    = address

    # 3 operation modes for pum: 0 – auto, 2 – flowrate, 3 – rev/rpm
    def set_mode(self, mode):
        tag_name = self.address['control_mode']['tag']
        location = self.address['control_mode']['position'] 
        register_address = self.modbus_io.config['address'][tag_name][location]
        res, error = self.modbus_io.write_register(register_address, mode)
        ret = True  
        if error: 
            ret = False
        return ret, error 

    def pump_on(self): 
        tag_name = self.address['control']['tag']
        location = self.address['control']['position'] 
        register_address = self.modbus_io.config['address'][tag_name]['position']
        res, error = self.modbus_io.write_coil(register_address, location, True)
        return res, error
    

    def pump_off(self): 
        tag_name = self.address['control']['tag']
        location = self.address['control']['position'] 
        register_address = self.modbus_io.config['address'][tag_name]['position']
        res, error = self.modbus_io.write_coil(register_address, location, False)
        return res, error

    def set_flowrate(self, flowrate): 
        tag_name = self.address['control_rpm']['tag']
        location = self.address['control_rpm']['position']
        register_address = self.modbus_io.config['address'][tag_name][location]
        print("------", register_address)
        res, error = self.modbus_io.write_register(register_address, flowrate)
        ret = None   
        if error: 
            ret = res.registers[0]
        return ret, error 


    # Read intensity value of lights 
    def set_rpm(self, rpm): 
        tag_name = self.address['control_rpm']['tag']
        location = self.address['control_rpm']['position']
        register_address = self.modbus_io.config['address'][tag_name][location]
        print("------", register_address)
        res, error = self.modbus_io.write_register(register_address, rpm)
        ret = None   
        if error: 
            ret = res.registers[0]
        return ret, error 

        
    # get pump status 
    def status_on_off(self): 
        tag_name = self.address['status']['tag']
        location = self.address['status']['position']
        register_address = self.modbus_io.config['address'][tag_name]['position']
        res, error = self.modbus_io.read_coil(register_address, location)
        return res, error 

    # only for type b racks
    def enable_fill_drain_mode(self):
        tag_name = self.address['fill_drain_control']['tag']
        location = self.address['fill_drain_control']['position'] 
        register_address = self.modbus_io.config['address'][tag_name]['position']
        res, error = self.modbus_io.write_coil(register_address, location, False)
        return res, error


    def set_fill_mode_flowrate(self, flowrate):
        tag_name = self.address['control_fill_flowrate']['tag']
        location = self.address['control_fill_flowrate']['position']
        register_address = self.modbus_io.config['address'][tag_name][location]
        print("------", register_address)
        res, error = self.modbus_io.write_register(register_address, flowrate)
        ret = None   
        if error: 
            ret = res.registers[0]
        return ret, error 

    def set_drain_mode_flowrate(self, flowrate):
        tag_name = self.address['control_drain_flowrate']['tag']
        location = self.address['control_drain_flowrate']['position']
        register_address = self.modbus_io.config['address'][tag_name][location]
        print("------", register_address)
        res, error = self.modbus_io.write_register(register_address, flowrate)
        ret = None   
        if error: 
            ret = res.registers[0]
        return ret, error 

    def set_fill_mode_duration(self, duration): 
        tag_name = self.address['control_fill_duration']['tag']
        location = self.address['control_fill_duration']['position']
        register_address = self.modbus_io.config['address'][tag_name][location]
        print("------", register_address)
        res, error = self.modbus_io.write_register(register_address, duration)
        ret = None   
        if error: 
            ret = res.registers[0]
        return ret, error 

    def set_drain_mode_duration(self, duration): 
        tag_name = self.address['control_drain_duration']['tag']
        location = self.address['control_drain_duration']['position']
        register_address = self.modbus_io.config['address'][tag_name][location]
        print("------", register_address)
        res, error = self.modbus_io.write_register(register_address, duration)
        ret = None   
        if error: 
            ret = res.registers[0]
        return ret, error 
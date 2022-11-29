# The code here is to bridge plc and 
# Global libary import 
import json
import os
import sys

# Local library import 
from ellemento.bridge.plc_bridge import ModelPlcBridge
from lib.logging.logger_initialiser import EllementoLogger
from ellemento.plc.plc_io_manager import PlcIOManager

logger = EllementoLogger.__call__().logger


class LightModelPlcBridge(ModelPlcBridge):
    ModelPlcDict = {}

    def __init__(self, id=-1, type_name="Default", light_id=-1, plc_id=-1, address=None):
        super().__init__()
        self._id = id
        self._type_name = type_name
        self._light_id = light_id
        self._plc_id = plc_id
        self.modbus_io = PlcIOManager.get_plc_io(id=self._plc_id)
        self.address = address

    def print_model(self, type="Light", id=1):
        print(self.cfg[type])
        # all_lights = json.load(self.cfg[type])
        # print(all_lights)

    def on_light(self):
        tag_name = self.address['control']['tag']
        location = self.address['control']['position']
        register_address = self.modbus_io.config['address'][tag_name]['position']
        res, error = self.modbus_io.write_coil(register_address, location, True)
        return res, error

    def off_light(self):
        tag_name = self.address['control']['tag']
        location = self.address['control']['position']
        register_address = self.modbus_io.config['address'][tag_name]['position']
        res, error = self.modbus_io.write_coil(register_address, location, False)
        return res, error

    def set_intensity(self, percent):
        tag_name = self.address['control_intensity']['tag']
        location = self.address['control_intensity']['position']
        register_address = self.modbus_io.config['address'][tag_name][location]
        print("------", register_address)
        res, error = self.modbus_io.write_address_json(register_address, percent)
        ret = True
        if error:
            ret = False
        return ret, error

        # Read intensity value of lights

    def intensity(self):
        tag_name = self.address['intensity']['tag']
        location = self.address['intensity']['position']
        register_address = self.modbus_io.config['address'][tag_name][location]
        res, error = self.modbus_io.read_address_json(register_address, 1)
        ret = None
        if not error:
            ret = res.registers[0]
        return ret, res

        # Read of/off status of the lights

    def on_off_status(self):
        tag_name = self.address['status']['tag']
        location = self.address['status']['position']
        register_address = self.modbus_io.config['address'][tag_name]['position']
        res, error = self.modbus_io.read_coil(register_address, location)
        return res, error

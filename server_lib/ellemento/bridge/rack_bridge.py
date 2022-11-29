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


class RackModelPlcBridge(ModelPlcBridge):
    ModelPlcDict = {}

    def __init__(self, id=-1, type_name="Default", rack_id=-1, plc_id=-1, address=None):
        super().__init__()
        self._id = id
        self._type_name = type_name
        self._rack_id = rack_id
        self._plc_id = plc_id
        self.modbus_io = PlcIOManager.get_plc_io(id=self._plc_id)
        self.address = address

    def set_control_section_mode(self, section, mode):
        tag_name = self.address['CTRL_SECTION_MODE']['tag']
        location = self.address['CTRL_SECTION_MODE']['position'][section - 1]
        register_address = self.modbus_io.config['address'][tag_name][location]
        res, error = self.modbus_io.write_address_json(register_address, mode)
        ret = None
        if not error:
            ret = res.registers[0]
        return ret, res

    def appy_update(self):
        tag_name = self.address['apply_update']['tag']
        register_address = self.modbus_io.config['address'][tag_name]
        res, error = self.modbus_io.write_coil(register_address, True)
        return res, error

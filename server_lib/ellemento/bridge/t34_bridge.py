# Local library import
from ellemento.bridge.plc_bridge import ModelPlcBridge
from lib.logging.logger_initialiser import EllementoLogger
from ellemento.plc.plc_io_manager import PlcIOManager

logger = EllementoLogger.__call__().logger


class T34ModelPlcBridge(ModelPlcBridge):
    ModelPlcDict = {}

    def __init__(self, id=-1, type_name="Default", t34_id=-1, plc_id=-1, address=None):
        super().__init__()
        self._id = id
        self._type_name = type_name
        self._t34_id = t34_id
        self._plc_id = plc_id
        self.plc_io = PlcIOManager.get_plc_io(id=self._plc_id)
        self.address = address

    def ready_to_place(self):
        tag_name = self.address['read']['part_ready_S3']
        register = self.plc_io.config['address'][tag_name]
        result = self.plc_io.read_plctag(register[0], register[1])
        return result

    def ready_to_pick(self):
        tag_name = self.address['read']['part_ready_S4']
        register = self.plc_io.config['address'][tag_name]
        result = self.plc_io.read_plctag(register[0], register[1])
        return result

    def lock_ASRS_place_pos(self):
        tag_name = self.address['read']['lock_ASRS_S3']
        register = self.plc_io.config['address'][tag_name]
        result = self.plc_io.read_plctag(register[0], register[1])
        return result

    def lock_ASRS_pick_pos(self):
        tag_name = self.address['read']['lock_ASRS_S4']
        register = self.plc_io.config['address'][tag_name]
        result = self.plc_io.read_plctag(register[0], register[1])
        return result

    def ASRS_arrived_place_pos(self, value):
        tag_name = self.address['write']['ASRS_arrived_S3']
        register = self.plc_io.config['address'][tag_name]
        self.plc_io.write_plctag(register[0], value, register[1])

    def ASRS_arrived_pick_pos(self,value):
        tag_name = self.address['write']['ASRS_arrived_S4']
        register = self.plc_io.config['address'][tag_name]
        self.plc_io.write_plctag(register[0], value, register[1])

    def part_placed(self,value):
        tag_name = self.address['write']['part_placed_S3']
        register = self.plc_io.config['address'][tag_name]
        self.plc_io.write_plctag(register[0], value, register[1])

    def part_picked(self, value):
        tag_name = self.address['write']['part_picked_S4']
        register = self.plc_io.config['address'][tag_name]
        self.plc_io.write_plctag(register[0], value, register[1])

    def ASRS_part_presence_place_pos(self, value):
        tag_name = self.address['write']['part_presence_S3']
        register = self.plc_io.config['address'][tag_name]
        self.plc_io.write_plctag(register[0], value, register[1])

    def ASRS_part_presence_pick_pos(self,value):
        tag_name = self.address['write']['part_presence_S4']
        register = self.plc_io.config['address'][tag_name]
        self.plc_io.write_plctag(register[0], value, register[1])

    def ASRS_locked_place_pos(self,value):
        tag_name = self.address['write']['ASRS_locked_S3']
        register = self.plc_io.config['address'][tag_name]
        self.plc_io.write_plctag(register[0], value, register[1])

    def ASRS_locked_pick_pos(self,value):
        tag_name = self.address['write']['ASRS_locked_S4']
        register = self.plc_io.config['address'][tag_name]
        self.plc_io.write_plctag(register[0], value, register[1])

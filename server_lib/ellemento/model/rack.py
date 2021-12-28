from enum import Enum
from ellemento.model.shelf import Shelf
from ellemento.model.pump_control import PumpControl
from ellemento.bridge.bridge_factory import ModelPlcBridgeFactory


class RackStatus(Enum):
    IDLE = 1  # clean and ready to use
    NOT_FULL = 2  # with plants
    FULL = 3  # empty but not clean


# Other status could be added later
# light control 
# water control 
class RackType(Enum):
    TYPE_A_1 = 1
    TYPE_A_2 = 2
    TYPE_B_2 = 3


# type b has 2 sections
class RackSection(Enum):
    TOP = 1
    BOTTOM = 2


class SectionMode(Enum):
    AUTO = 1
    SEMI_AUTO = 2
    MANUAL = 3


# Each rack has 1-3 sections, each section has 1 pump and a few shelves


# B - two sections ,, 8-5 ,,
# A - 1 sections 12 
class Rack:
    class Section:
        # constant values 
        MAX_A1_SHELVES = 12
        MAX_A2_SHELVES = 12
        MAX_B2_TOP_SHELVES = 8
        MAX_B2_BOTTOM_SHELVES = 5

        def __init__(self, id=-1, rack_type=RackType.TYPE_A_1, section=RackSection.TOP):
            self.pump = None
            self.shelves = []
            self.rack_type = rack_type
            self.rack_section = section
            self.section_mode = SectionMode.MANUAL

        # Add a shelf to the rack
        def add_shelf(self, shelf):
            if shelf is None:
                return False
            if self.rack_type is RackType.TYPE_A_1:
                if len(self.shelves) < self.MAX_A1_SHELVES:
                    self.shelves.append(shelf)
            elif self.rack_type is RackType.TYPE_A_2:
                if len(self.shelves) < self.MAX_A2_SHELVES:
                    self.shelves.append(shelf)
            elif self.rack_type in [RackType.TYPE_B_2]:
                if self.rack_section == RackSection.TOP:
                    if len(self.shelves) < self.MAX_B2_TOP_SHELVES:
                        self.shelves.append(shelf)
                if self.rack_section == RackSection.BOTTOM:
                    if len(self.shelves) < self.MAX_B2_BOTTOM_SHELVES:
                        self.shelves.append(shelf)

            shelf.rack = self

        def add_pump(self, pump):
            self.pump = pump

    all_racks = {}

    @staticmethod
    def add_rack(rack):
        Rack.all_racks[rack.id] = rack
        pass

    @staticmethod
    def get_rack(id):
        return Rack.all_racks[id]

    @staticmethod
    def print():
        for rack_x in Rack.all_racks:
            print(Rack.all_racks[rack_x])

    def __init__(self, id=-1, type_name="Default", rack_type=RackType.TYPE_A_1):
        self._id = id
        self._type_name = type_name
        self._status = RackStatus.IDLE
        self._shelves = []
        # Set tray status of the rack. if it has, it shall be tray number
        self._pumps = []
        self._enable = True
        self._sections = []
        self._rack_type = rack_type
        if rack_type in [RackType.TYPE_A_1, RackType.TYPE_A_2]:
            # CREATE 1 SECTION 
            section = Rack.Section(1, rack_type=rack_type)
            self._sections.append(section)
        elif rack_type == RackType.TYPE_B_2:
            section_top = Rack.Section(1, rack_type=rack_type, section=RackSection.TOP)
            self._sections.append(section_top)
            section_bottom = Rack.Section(1, rack_type=rack_type, section=RackSection.BOTTOM)
            self._sections.append(section_bottom)
        self.mod_bus = ModelPlcBridgeFactory.get_bridge(type='Rack', id=self._id)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value

        # Add a shelf to the rack

    def add_shelf(self, shelf, section=RackSection.TOP):
        if shelf is None:
            return False

        if self._rack_type in [RackType.TYPE_A_1, RackType.TYPE_A_2]:
            self._sections[0].add_shelf(shelf)
            return

        if self._rack_type in RackType.TYPE_B_2:
            if section == RackSection.TOP:
                self._sections[0].add_shelf(shelf)
            if section == RackSection.BOTTOM:
                self._sections[1].add_shelf(shelf)

        self._shelves.append(shelf)
        shelf.rack = self

    # Add a pump control to the rack 
    def add_pumps(self, pump_id, section=RackSection.TOP):
        if pump_id not in self._pumps:
            self._pumps[pump_id] = PumpControl.get_pump(pump_id)

    def __repr__(self):
        return "<object: %s, id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)

    def __str__(self):
        return "<object: %s, id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)

    def appy_update(self):
        self.mod_bus.apply_update()
        pass

    def change_session_model(self, section=RackSection.TOP, mode=SectionMode.MANUAL):
        self.mod_bus.set_control_section_mode(section, mode)
        self._sections[section].section_mode = mode
        pass

    def transfer_in(self, tray_id):
        pass

    def transfer_out(self, tray_out):
        pass

    def water_on(self):
        pass

    def water_off(self):
        pass

    def light_on(self):
        pass

    def light_off(self):
        pass

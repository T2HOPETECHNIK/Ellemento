# each shelf has 9 trays maximum 
# Each shelf has light and water control 
from ellemento.model.water_control import WaterControl
from enum import Enum

from ellemento.model.tray import Tray, TrayStatus
from ellemento.model.light_control import LightControl

class ShelfStatus(Enum):
    IDLE = 1        # clean and ready to use
    LOADING = 2     # System is loading the shelf with plants
    UNLOADING = 3   # System is unloading the shelf with plants 
    FULL = 4       # empty but not clean 
# Other status could be added later 
# light control 
# water control 

class Phase(Enum):
    NOT_PLANNED     = 0 
    PHASE1          = 1
    PHASE2          = 2
    PHASE3          = 3
    PHASE4          = 4
    PHASE5          = 5 
    PHASE1_BACK_UP  = 6
    PHASE2_BACK_UP  = 7
    PHASE3_BACK_UP  = 8
    PHASE4_BACK_UP  = 9
    PHASE5_BACK_UP  = 10
    SOWER_2_PHASE1  = 11
    PHASE3_2_TRANSPLANT = 12
    TRANSPLANT_2_PHASE4 = 13
    PHASE4_2_TRANSPLANT = 14
    TRANSPLANT_2_PHASE5 = 15 

class Shelf:
    all_shelves = {} 
    
    @staticmethod 
    def get_shelf(id):
        return Shelf.all_shelves[id]

    @staticmethod
    def add_shelf(shelf): 
        print(shelf)
        Shelf.all_shelves[shelf.id] = shelf
    
    @staticmethod 
    def print(): 
        for shelf_x in Shelf.all_shelves:
            print(Shelf.all_shelves[shelf_x])

    def __init__(self, id = -1, type_name='default', max_tray = 9):
        self._id = id
        self._status = ShelfStatus.IDLE
        self._rack =  -1
        # each shelf must be 1 of the phase, [1, 2, 3, 4, 5]
        self._phase = Phase.NOT_PLANNED 
        self._max_tray = max_tray
        # Set tray status of the rack. if has, it shall be tray number 
        self._trays = {}
        self._lights = {}
        self._valves = {}
        self._enable = True 
        self._type_name = type_name

    def __repr__(self):
        return "<object: %s, id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)

    def __str__(self):
        return "<object: %s, id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self.id = value 

    @property
    def status(self): 
        return self._status

    @property 
    def type_name(self): 
        return self._type_name

    @type_name.setter
    def type_name(self, value): 
        self._type_name = value 

    @property 
    def enable(self):
        return self._enable 

    @enable.setter
    def enable(self, value): 
        self._enable = value   

    @property 
    def phase(self): 
        return self._phase 
    
    @phase.setter
    def phase(self, value): 
        self._phase - value; 
        
    def add_tray(self, tray_id): 
        if tray_id not in self._trays: 
            self._trays[tray_id] = Tray.get_tray(tray_id)
        if len(self._trays) == 1: 
            self._status = ShelfStatus.LOADING
        
        if len(self._trays) == self._max_tray:
            self._status = ShelfStatus.FULL
     

    def remove_tray(self, tray_id): 
        if tray_id in self._trays: 
            del self._trays[tray_id]
        if len(self._trays) == self._max_tray - 1: 
            self._status = ShelfStatus.UNLOADING
        if len(self._trays) == 0: 
            self._status = ShelfStatus.IDLE

    def add_light(self, light_id):
        if light_id not in self._lights: 
            self._lights[light_id] = LightControl.get_light(light_id)

    def remove_light(self, light_id): 
        if light_id in self._lights: 
            del self._lights[light_id]
    
    def add_valve(self, valve_id): 
        if valve_id not in self._valves: 
            self._valves[valve_id] = WaterControl.get_valve(valve_id)

    def remove_valve(self, valve_id): 
        if valve_id in self._valves: 
            del self._valves [valve_id]

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
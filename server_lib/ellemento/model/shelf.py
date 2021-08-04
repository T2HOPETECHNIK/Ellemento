# each shelf has 9 trays maximum 
# Each shelf has light and water control 
from enum import Enum

from ellemento.model.tray import Tray
from ellemento.model.light_control import LightControl

class ShelfStatus(Enum):
    IDLE = 1        # clean and ready to use
    NOT_FULL = 2      # with plants 
    FULL = 3       # empty but not clean 
# Other status could be added later 
# light control 
# water control 

class Shelf:
    all_shelf = {} 
    def __init__(self, id):
        self._id = id
        self._status = ShelfStatus.IDLE
        self._rack =  -1
        # Set tray status of the rack. if has, it shall be tray number 
        self._trays = {}
        self._lights = {}
        self._valves = {}

    @staticmethod 
    def get_shelf(id):
        return Shelf.all_self[id]
        
    def add_tray(self, tray_id): 
        if tray_id not in self._trays: 
            self._trays[tray_id] = Tray.get_tray(tray_id)

    def remove_tray(self, tray_id): 
        if tray_id in self._trays: 
            del self._trays[tray_id]
    
    def add_light(self, light_id):
        if light_id not in self._trays: 
            self._trays[light_id] = LightControl.get_light(light_id)
           
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
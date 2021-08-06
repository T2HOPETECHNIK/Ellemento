# shelf 
# pum;p 
# each shelf has 9 trays maximum 
# Each shelf has light and water control 
from enum import Enum

from ellemento.model.shelf import Shelf 
from ellemento.model.pump_control import PumpControl  

class RackStatus(Enum):
    IDLE = 1        # clean and ready to use
    NOT_FULL = 2      # with plants 
    FULL = 3       # empty but not clean 
# Other status could be added later 
# light control 
# water control 

class Rack:
    def __init__(self, id):
        self._id = id
        self._status = Rack.IDLE
        self._shelves = {} 
        # Set tray status of the rack. if has, it shall be tray number 
        self._pumps = {}
        self._enable = True 

    @property 
    def enable(self):
        return self._enable 

    @enable.setter
    def enable(self, value): 
        self._enable = value   

    # Add a shelf to the rack 
    def add_shelf(self, shelf_id): 
        if shelf_id not in self._shelves: 
            self._shelves[shelf_id] = Shelf.get_shelf(shelf_id)

    # Add a pump control to the rack 
    def add_pumps(self, pump_id): 
        if pump_id not in self._pumps: 
            self._pumps[pump_id] = PumpControl.get_pump(pump_id)

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
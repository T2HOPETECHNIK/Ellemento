# each shelf has 9 trays maximum 
# Each shelf has light and water control 
from enum import Enum

class ShelfStatus(Enum):
    IDLE = 1        # clean and ready to use
    NOT_FULL = 2      # with plants 
    FULL = 3       # empty but not clean 
# Other status could be added later 
# light control 
# water control 

class Shelf:
    def __init__(self, id):
        self._id = id
        self._status = ShelfStatus.IDLE
        self._rack =  -1
        # Set tray status of the rack. if has, it shall be tray number 
        self._trays = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self._lights = [0, 0, 0]
        self._valves = [0, 0 ,0]

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
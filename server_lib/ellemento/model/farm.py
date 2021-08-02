# shelf 
# pum;p 
# each shelf has 9 trays maximum 
# Each shelf has light and water control 
from enum import Enum

class FarmStatus(Enum):
    IDLE = 1        # clean and ready to use
    NOT_FULL = 2      # with plants 
    FULL = 3       # empty but not clean 
# Other status could be added later 
# light control 
# water control 

class Farm:
    def __init__(self, id):
        self._id = id
        self._status = FarmStatus.IDLE
        self._racks = []  
    
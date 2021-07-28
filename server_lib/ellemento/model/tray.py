from enum import Enum

class TrayStatus(Enum):
    IDLE = 1        # clean and ready to use
    IN_USE = 2      # with plants 
    DIRTY = 3       # empty but not clean 
# Other status could be added later 

class Tray:
    def __init__(self, id):
        self._id = id
        self._status = TrayStatus.IDLE
        self._has_veg = False   
        self._has_foam = False
        self._row_pots = 0 
        self._col_pots = 0
        self._phase = "" # Initial location is not sure 

    @property
    def id(self): 
        return self._id

    @id.setter
    def id(self, value): 
        self._id = value;  

    # Fill an empty tray with pots 
    def fill_pots(self, row=10, col=12): 
        pass

    # fill an tray with pots foams 
    def fill_foam(self): 
        pass
    
    # transfer an try to new location 
    def transfer(self, destination): 
        pass

    def transplant(self):
        pass 

    def wash(self):
        pass
    
    


    





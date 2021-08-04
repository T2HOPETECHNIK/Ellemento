#*
#  Tray class to define  the basic tray properties and operations 
#* 

from enum import Enum

class TrayStatus(Enum):
    IDLE = 1        # clean and ready to use
    IN_USE = 2      # with plants 
    DIRTY = 3       # empty but not clean 
# Other status could be added later 

class Tray:
    all_trays = {} 
    
    @staticmethod
    def get_tray(id):
        return Tray.all_trays[id]
    
    def __init__(self, id):
        self._id = id
        self._status = TrayStatus.IDLE
        self._has_veg = False   
        self._has_foam = False
        self._dimension = {}
        self._pots= {}
        self._location = "" # Initial location is not sure 

    

    @property
    def id(self): 
        return self._id

    @id.setter
    def id(self, value): 
        self._id = value 

    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value): 
        if (not isinstance(value, TrayStatus)):
            raise(ValueError("Status is not in the predefined list"))
        self._status = value 

    @property
    def has_veg(self): 
        return self._has_veg 
    
    @has_veg.setter
    def has_veg(self, value):
        self._has_veg = value

    @property
    def has_foam(self):
        return self._has_foam

    @ property
    def dimension(self): 
        return self._dimension
    
    @dimension.setter
    def dimension(self, row, col) : 
        self._dimension = [row, col]

    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, value) : 
        self._location = value 

    # transfer from current location to another location 
    def transfer(self, destination):
        self.location = destination    

    # Fill an empty tray with pots 
    def fill_pots(self):
        for row in self._pots:
            for col in row:
                self._pots[row][col] = 1

    def discard_pots(self):
        for row in self._pots:
            for col in row:
                self._pots[row][col] = o
  
    

    
    


    





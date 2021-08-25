# shelf 
# pum;p 
# each shelf has 9 trays maximum 
# Each shelf has light and water control 
from enum import Enum
from ellemento.model.tray import Tray

class BufferStatus(Enum):
    IDLE = 1            # clean and ready to use
    NOT_FULL = 2        # with plants 
    FULL = 3            # empty but not clean

    # Other status could be added later 
    # light control 
    # water control 

class Buffer:
    

    @staticmethod 
    def get_farm(id): 
        pass

    @staticmethod 
    def add_farm(farm_new): 
        pass

    @staticmethod 
    def print():
        pass

    def __init__(self, id = -1, type_name = "Default"):
        self.trays = []  
        pass

    @property
    def id(self): 
        return self._id 

    @id.setter
    def id(self, value):
        self._id = value 

    def load(self, tray):
        if len(self.trays) >= 9: 
            raise Exception("Not able to load, buffer is full")
        if len(self.trays) < 3:
            self.trays.append(tray) 
            return 
        if len(self.trays) >= 3: 
            self.trays.insert(2, tray)

    def unload(self):
        if len(self.trays) == 0: 
            raise Exception("Not able to unload,  buffer is empty")
        return self.trays.pop()
    
    def print_trays(self):
        for tray_x in self.trays: 
           print(tray_x)
        

    def __repr__(self):
        return "<object: %s, id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)

    def __str__(self):
        return "<object: %s, id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)
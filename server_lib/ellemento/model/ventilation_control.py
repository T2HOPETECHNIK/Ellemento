from enum import Enum

class VentilationStatus(Enum):
    OFF = 1        # clean and ready to use
    ON = 2      # with plants 
     
# Other status could be added later 

class VentilationControl:
    all_fans = {}
    @staticmethod
    def add_fan(fan):
        VentilationControl.all_fans[fan.id] = fan 
        pass 

    @staticmethod 
    def get_fan(id):
        return  VentilationControl.all_fans[id]  

    @staticmethod 
    def print():
        for val_x in VentilationControl.all_fans:
            print(VentilationControl.all_fans[val_x])

    def __init__(self, id = -1, type_name = "Default"):
        self._id = id
        self._percent = 0
        self._type_name = type_name
        self._status = VentilationStatus.OFF

    @property
    def id(self): 
        return self._id 
    
    @id.setter
    def id(self, value):
        self._id = value 

    def on(self, percent = 100): 
        self._status = VentilationStatus.ON
        self._percent = percent

    def off(self):
        self._status = VentilationStatus.OFF

    def adjust(self, percent):
        self._percent = percent
    
    
    def __repr__(self):
        return "<object: %s, id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)

    def __str__(self):
        return "<object: %s, id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)

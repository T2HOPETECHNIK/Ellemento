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
    all_racks = {}
    
    @staticmethod 
    def add_rack(rack):
        Rack.all_racks[rack.id] = rack;  
        pass 

    @staticmethod
    def get_rack(id):
        return Rack.all_racks[id] 

    @staticmethod 
    def print(): 
        for rack_x in Rack.all_racks:
            print(Rack.all_racks[rack_x])

    def __init__(self, id = -1, type_name = "Default"):
        self._id = id
        self._type_name = type_name
        self._status = RackStatus.IDLE
        self._shelves = [] 
        # Set tray status of the rack. if has, it shall be tray number 
        self._pumps = {}
        self._enable = True 
    
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
    def add_shelf(self, shelf): 
        if shelf == None: 
            raise Exception("Shelf is None")
        self._shelves.append(shelf)
        shelf.rack = self
        

    # Add a pump control to the rack 
    def add_pumps(self, pump_id): 
        if pump_id not in self._pumps: 
            self._pumps[pump_id] = PumpControl.get_pump(pump_id)

    def __repr__(self):
        return "<object: %s, id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)

    def __str__(self):
        return "<object: %s, id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)
    

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
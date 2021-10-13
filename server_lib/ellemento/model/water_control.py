from enum import Enum

from ellemento.bridge.bridge_factory import ModelPlcBridgeFactory

class ValveStatus(Enum):
    OFF = 1        # clean and ready to use
    ON = 2      # with plants 
     
# Other status could be added later 

class WaterControl:
    all_valves = {} 

    @staticmethod 
    def get_valve(id): 
        return WaterControl.all_valves[id]

    # put all values in the system
    @staticmethod
    def add_valve(val): 
        WaterControl.all_valves[val.id] = val 

    
    @staticmethod 
    def print(): 
        for val_x in WaterControl.all_valves:
            print(WaterControl.all_valves[val_x])

    @property 
    def id(self):
        return self._id

    @id.setter
    def id (self, value):
        self._id = value   

    def __init__(self, id = -1, type_name = "Default"):
        self._id = id
        self._percent = 0
        self._status = ValveStatus.OFF
        self._type_name = type_name 
        self.mod_bus = ModelPlcBridgeFactory.get_bridge(type = 'Valve', id = self._id)

    def on(self, percent = 100): 
        self._status = ValveStatus.ON
        res, error = self.mod_bus.on_valve() 
        self._percent = percent
        return res, error

    def off(self):
        self._status = ValveStatus.OFF
        res, error = self.mod_bus.off_valve() 
        return res, error 
        
    def adjust(self, percent):
        self._percent = percent
        res, error = self.mod_bus.set_percentage(percent)
        return res, error

    def get_percent(self): 
        res, error = self.mod_bus.get_percentage() 
        return res, error

    def __repr__(self):
        return "<object: %s, id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)

    def __str__(self):
        return "<object: %s, id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)

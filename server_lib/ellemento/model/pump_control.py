# 12 shelf --> 1 pump
# 14 shelves --> 2 pump 

from enum import Enum

class PumpValveStatus(Enum):
    OFF = 1        # clean and ready to use
    ON = 2      # with plants 


class PumpMode(Enum): 
    PUMP_FLOW_MODE = 1
    PUMP_RPM_MODE = 2
        
# Other status could be added later 

class PumpControl:
    all_pumps = {}

    @staticmethod
    def get_pump(id): 
        return PumpControl.all_pumps[id]
    
    @staticmethod 
    def add_pump(pump): 
        PumpControl.all_pumps[pump.id] = pump 

    @staticmethod 
    def print(): 
        for shelf_x in PumpControl.all_pumps:
            print(PumpControl.all_pumps[shelf_x])

    def __init__(self, id = -1, type_name = 'Default'):
        self._id = id
        self._flowrate = 0
        self._status = PumpValveStatus.OFF
        self._rpm = 0
        self._type_name = type_name 
        self._mode = PumpMode.PUMP_FLOW_MODE 

    @property
    def id(self):
        return self._id 
     
    @id.setter
    def id(self, value): 
        self._id = value 

    def on(self, flowrate = 100, rpm = 3600): 
        self._status = PumpValveStatus.ON
        self._flowrate = flowrate
        self._rpm = rpm 

    def off(self):
        self._status = PumpValveStatus.OFF
        self._flowrate = 0
        self._rpm = 0 
    
    def set_mode(self, mode): 
        self_mode = mode 

    def adjust(self, flowrate):
        
        # to do link to the PLC  
        # set the rate 
        # update the rate 
        self._flowrate = flowrate

    def __repr__(self):
        return "<object: %s, id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)

    def __str__(self):
        return "<object: %s, id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)


        

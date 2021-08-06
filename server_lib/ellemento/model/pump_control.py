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
    
    def __init__(self, id):
        self._id = id
        self._flowrate = 0
        self._status = PumpValveStatus.OFF
        self._rpm = 0
        self._mode = PumpMode.PUMP_FLOW_MODE 

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

        


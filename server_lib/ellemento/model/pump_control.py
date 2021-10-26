# 12 shelf --> 1 pump
# 14 shelves --> 2 pump 

from enum import Enum

from ellemento.bridge.bridge_factory import ModelPlcBridgeFactory 

class PumpValveStatus(Enum):
    OFF = 1        # clean and ready to use
    ON = 2      # with plants 


class PumpMode(Enum): 
    PUMP_AUTO_MODE = 0
    PUMP_FLOW_MODE = 2
    PUMP_RPM_MODE = 3
    
        
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
        self.mod_bus = ModelPlcBridgeFactory.get_bridge(type = 'Pump', id = self._id)
        

    @property
    def id(self):
        return self._id 
     
    @id.setter
    def id(self, value): 
        self._id = value 

    def on(self, flowrate = 100, rpm = 3600): 
        self._status = PumpValveStatus.ON
        ret, error = self.mod_bus.pump_on() 
        self._flowrate = flowrate
        self._rpm = rpm 
        return ret, error 

    def off(self):
        self._status = PumpValveStatus.OFF
        ret, error = self.mod_bus.pump_off() 
        self._flowrate = 0
        self._rpm = 0 
        return ret, error 
    
    def set_mode(self, mode = PumpMode.PUMP_AUTO_MODE): 
        ret, error = self.mod_bus.set_mode(mode) 
        self_mode = mode 
        return ret, error 

    def set_flowrate(self, flowrate):
        ret, error = self.mod_bus.set_flowrate(flowrate)
        # to do link to the PLC  
        # set the rate 
        # update the rate 
        self._flowrate = flowrate
        return ret, error 


    def set_rpm(self, rpm):
        ret, error = self.mod_bus.set_rpm(rpm)
        # to do link to the PLC  
        # set the rate 
        # update the rate 
        self._flowrate = rpm
        return ret, error 


    def __repr__(self):
        return "<object: %s, id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)

    def __str__(self):
        return "<object: %s, id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)


        


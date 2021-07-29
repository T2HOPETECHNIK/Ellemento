# 12 shelf --> 1 pump
# 14 shelves --> 2 pump 

from enum import Enum

class PumpValveStatus(Enum):
    OFF = 1        # clean and ready to use
    ON = 2      # with plants 
     
# Other status could be added later 

class LightControl:
    def __init__(self, id):
        self._id = id
        self._percent = 0
        self._status = PumpValveStatus.OFF
        self.rpm = 0

    def on(self, percent = 100): 
        self._status = PumpValveStatus.ON
        self._percent = percent

    def off(self):
        self._status = PumpValveStatus.OFF

    def adjust(self, percent):
        self._percent = percent

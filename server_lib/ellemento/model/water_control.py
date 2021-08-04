from enum import Enum

class ValveStatus(Enum):
    OFF = 1        # clean and ready to use
    ON = 2      # with plants 
     
# Other status could be added later 

class WaterControl:
    all_valves = {} 

    @staticmethod 
    def get_valve(id): 
        return WaterControl.all_valves[id]

    def __init__(self, id):
        self._id = id
        self._percent = 0
        self._status = ValveStatus.OFF

    def on(self, percent = 100): 
        self._status = ValveStatus.ON
        self._percent = percent

    def off(self):
        self._status = ValveStatus.OFF

    def adjust(self, percent):
        self._percent = percent

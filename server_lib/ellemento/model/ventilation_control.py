from enum import Enum

class VentilationStatus(Enum):
    OFF = 1        # clean and ready to use
    ON = 2      # with plants 
     
# Other status could be added later 

class VentilationControl:
    def __init__(self, id):
        self._id = id
        self._percent = 0
        self._status = VentilationStatus.OFF

    def on(self, percent = 100): 
        self._status = VentilationStatus.ON
        self._percent = percent

    def off(self):
        self._status = VentilationStatus.OFF

    def adjust(self, percent):
        self._percent = percent

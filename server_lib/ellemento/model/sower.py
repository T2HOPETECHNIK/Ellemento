# shelf 
# pum;p 
# each shelf has 9 trays maximum 
# Each shelf has light and water control 
from enum import Enum
from ellemento.model.tray_phase_1_3 import TrayPhase13
from lib.logging.logger_initialiser import EllementoLogger

logger = EllementoLogger.__call__().logger

class Sower:
    all_sowers = {}

    @staticmethod 
    def create_sower(): 
        sower_new = Sower(id = 1, type_name="Sower")
        Sower.all_sowers[sower_new.id] = sower_new

    @staticmethod 
    def get_sower(): 
        if len(Sower.all_sowers) == 0: 
            Sower.create_sower()
        return Sower.all_sowers[1]

    def __init__(self, id = -1, type_name = "Default"):
        self._id = id
        self._type_name = type_name
        self._trays = []
        
    @property
    def id(self): 
        return self._id 

    @id.setter
    def id(self, value):
        self._id = value

    def load_tray(self, tray): 
        if len(self._trays) == 0: 
            self._trays.append(TrayPhase13(tray)) 
        else: 
            raise Exception("Sower is not empty, not able to load tray ") 

    def sow(self): 
        if len(self._trays) == 0: 
            raise Exception("No tray is available at lower")
        self._trays[0].sow() 
    
    def ready_to_unload(self): 
        if len(self._trays) == 0: 
            logger.info("No trays in the sower")
            return False 
        # if tray has veg planted, then ready to unload from the sower to empty shelf 
        return self._trays[0].has_veg 

    def ready_to_load(self): 
        if len(self._trays) == 0: 
            return True 
        return False

    def unload_tray(self): 
        if len(self._trays) == 0: 
            raise Exception("No tray is available at sower")
        if not self._trays[0].has_veg: 
            raise Exception("Sowing is not done ")
        return self._trays.pop(0) 

    def __repr__(self):
        return "<object: %s, id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)

    def __str__(self):
        return "<object: %s, id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)
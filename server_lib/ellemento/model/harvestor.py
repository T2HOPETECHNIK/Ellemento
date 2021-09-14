# shelf 
# pum;p 
# each shelf has 9 trays maximum 
# Each shelf has light and water control 
from enum import Enum

from ellemento.model.tray_phase_5 import TrayPhase5

class Harvestor:
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


    # load a tray to the harvestoer 
    def load_tray(self, tray): 
        self._trays.insert(0, tray)

    # unload tray if harvesting is done 
    def unload_tray(self):
        if len(self._trays == 0): 
            raise Exception("No trays available for unloading")  
        return self._trays.pop()   

    def harvest(self): 
        tray_ph5 = TrayPhase5(self._trays(-1))
        tray_ph5.harvest() 


    def __repr__(self):
        return "<object: %s, id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)

    def __str__(self):
        return "<object: %s, id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)
    

    all_Harvestor = {}
    
    @staticmethod
    def create_harvestor():
        harvestor_new = Harvestor(id = 1, type_name= "harvestor")    
        Harvestor.all_Harvestor[harvestor_new.id] = harvestor_new

    @staticmethod
    def get_harvestor():
        if len (Harvestor.all_Harvestor) == 0:
            Harvestor.create_harvestor()
        return Harvestor.all_Harvestor[1] 
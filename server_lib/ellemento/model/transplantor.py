# shelf 
# pum;p 
# each shelf has 9 trays maximum 
# Each shelf has light and water control 
from enum import Enum

class TransplantorType(Enum):
    PHASE_3_4_TRANSPLANTOR  = 1
    PHASE_4_5_TRANSPLANTOR  = 2
 
class Transplantor:
    def __init__(self, id = -1, type_name = "Default"):
        self._id = id
        self._type_name = type_name
        self._tray_source = None
        self._tray_destination = None
        
    @property
    def id(self): 
        return self._id 

    @id.setter
    def id(self, value):
        self._id = value 

    def set_src_tray(self, src_tray):
        self._tray_source = src_tray
        pass 

    def set_dest_tray(self, dst_tray): 
        self._tray_destination = dst_tray 
        pass 
        
    def remove_src_tray(self): 
        # to do ,,, set src try station 
        self._tray_source = None 

    def remove_dst_tray(self):
        # Update status of the destination tray 
        self._tray_destination = None 

    def __repr__(self):
        return "<object: %s, id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)

    def __str__(self):
        return "<object: %s, id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)
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
    
    def ready_to_move_in_src_tray(self): 
        if self._tray_source == None: 
            return True 
        return False 

    def ready_to_transplant(self): 
        # check source tray and destination tray need to be present
        if self._tray_source == None or self._tray_destination == None: 
            return False  
        
        # check source tray still has plants avilable 
        if not self._tray_source.has_veg: 
            return False

        # check destination tray is empty 
        if self._tray_destination.has_veg: 
            return False 
        return True 

    def ready_to_move_out_src_tray(self): 
        if self._tray_source == None: 
            return False 
        if self._tray_source.has_veg == False: 
            return True
        return False  

    def ready_to_move_in_dst_tray(self): 
        if self._tray_destination == None: 
            return True 
        return False 

    def ready_to_move_out_dst_tray(self): 
        if self._tray_destination == None: 
            return False
        return self._tray_destination.has_veg 

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
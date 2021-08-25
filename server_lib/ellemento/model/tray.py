#*
#  Tray class to define  the basic tray properties and operations 
#* 

from enum import Enum
import datetime

from lib.logging.logger_initialiser import EllementoLogger

logger = EllementoLogger.__call__().logger; 

class TrayStatus(Enum):
    CREATED             = 1
    IDLE                = 2        # clean and ready to use
    SOWER               = 3
    SOWER_TO_PHASE1     = 4
    PHASE1              = 5
    PHASE1_TO_PHASE2    = 6 
    PHASE2              = 7
    PHASE2_TO_PHASE3    = 8
    PHASE3              = 9
    PHASE3_TO_TRANPLANT = 10
    TRANSPLANT_TO_PHASE4        = 11
    PHASE4                      = 12
    PHASE4_TO_TRANSPLANT        = 13
    TRANSPLANT_TO_PHASE5        = 14
    PHASE5_TO_TRANSPLANT        = 15 
    DIRTY                       = 16       # empty but not clean 

# Other status could be added later 

class Tray:
    all_trays = {} 
    
    @staticmethod
    def get_tray(id):
        return Tray.all_trays[id]
    
    @staticmethod 
    def add_tray(tray): 
        Tray.all_trays[tray.id] = tray
    
    @staticmethod 
    def print(): 
        for tray_x in Tray.all_trays:
            print(Tray.all_trays[tray_x])
    
    def __init__(self, id = 0, dimensions = [12, 10], type_name="Unknown" ):
        self._id = id
        self._has_veg = False   
        self._has_foam = False
        self._dimensions = dimensions
        self._pots= {}
        self._location = None
        self._type_name = type_name
        # Initial location is not sure 
        self._enable = True 
        #str_log = "Created object " + self._type_name + " " + str(self._id); 
        #logger.info(str_log)
        self._set_status(TrayStatus.CREATED)


    def _set_status(self, status):
        self._status = status 
        self._status_time = datetime.datetime.now()

    @property 
    def type_name(self):
        return self._type_name 

    @type_name.setter
    def type_name(self, value): 
        self._type_name = value 

    def transplant_out(self): 
        self._set_status(TrayStatus.DIRTY)
        pass 

    def transplant_in(self): 
        pass 
    
    def __repr__(self):
        return "<object:%s id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)

    def __str__(self):
        return "<object:%s, id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)

    @property 
    def enable(self):
        return self._enable 

    @enable.setter
    def enable(self, value): 
        self._enable = value   

    @property
    def id(self): 
        return self._id

    @id.setter
    def id(self, value): 
        self._id = value 

    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value): 
        if (not isinstance(value, TrayStatus)):
            raise(ValueError("Status is not in the predefined list"))
        self._status = value 

    @property
    def has_veg(self): 
        return self._has_veg 
    
    @has_veg.setter
    def has_veg(self, value):
        self._has_veg = value

    @property
    def has_foam(self):
        return self._has_foam

    @ property
    def dimension(self): 
        return self._dimension
    
    @dimension.setter
    def dimension(self, row, col) : 
        self._dimension = [row, col]

    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, value) : 
        self._location = value 

    # Fill an empty tray with pots 
    def fill_pots(self):
        for row in self._pots:
            for col in row:
                self._pots[row][col] = 1

    def discard_pots(self):
        for row in self._pots:
            for col in row:
                self._pots[row][col] = 0

    # def fill_foams(self): 
    #     self.has_foam = True

    # def fill_seeds(self): 
    #     self.has_veg = True 
  
    

    
    


    





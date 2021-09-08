# shelf 
# pum;p 
# each shelf has 9 trays maximum 
# Each shelf has light and water control 
from enum import Enum

class FarmStatus(Enum):
    IDLE = 1            # clean and ready to use
    NOT_FULL = 2        # with plants 
    FULL = 3            # empty but not clean

    # Other status could be added later 
    # light control 
    # water control 

class Farm:
    all_farms = {}

    @staticmethod 
    def get_farm(id): 
        return Farm.all_farms[id]

    @staticmethod 
    def add_farm(farm_new): 
        Farm.all_farms[farm_new.id] = farm_new

    @staticmethod 
    def print():
        for farm_x in Farm.all_farms:
            print(Farm.all_farms[farm_x])

    def __init__(self, id = -1, type_name = "Default"):
        self._id = id
        self._type_name = type_name
        self._status = FarmStatus.IDLE
        self._racks = []
        self._fans = []

    @property
    def id(self): 
        return self._id 

    @id.setter
    def id(self, value):
        self._id = value 

    def add_rack(self, rack_id ): 
        self._racks.append(rack_id)

    def add_fans(self, fan_id): 
        self._fans.append(id)

    def __repr__(self):
        return "<object: %s, id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)

    def __str__(self):
        return "<object: %s, id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)
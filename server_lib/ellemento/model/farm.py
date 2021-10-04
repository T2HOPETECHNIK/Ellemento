# shelf 
# pum;p 
# each shelf has 9 trays maximum 
# Each shelf has light and water control 
from enum import Enum
from logging import Logger
from ellemento.model import tray_factory


from ellemento.model.rack_factory import RackFactory
from ellemento.model.shelf_factory import ShelfFactory
from ellemento.model.tray_factory import TrayFactory
from lib.logging.logger_initialiser import EllementoLogger

logger = EllementoLogger.__call__().logger

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
    def create_farm(id = -1, type_name = None):
        logger.info("start to create farm")
        farm = Farm(id = id, type_name= type)
        logger.info("Create farm DONE")
        TrayFactory.create_phase123_trays()
        logger.info("Creaste phase 123 trays done") 
        TrayFactory.create_phase4_trays()
        #TrayFactory.print()
        logger.info("Creaste phase 4 trays done")
        TrayFactory.create_phase5_trays()
        logger.info("Creaste phase 5 trays done")
     
        ShelfFactory.create_phase1_shelves()
        logger.info("Creaste phase 1 shelves done")
        ShelfFactory.create_phase2_shelves() 
        logger.info("Creaste phase 2 shelves done")
        ShelfFactory.create_phase3_shelves()
        logger.info("Creaste phase 3 shelves done") 
        ShelfFactory.create_phase4_shelves()
        logger.info("Creaste phase 4 shelves done")
        ShelfFactory.create_phase5_shelves()
        #ShelfFactory.print()
        logger.info("Creaste phase 5 shelves done")
        RackFactory.create_rack_A1()
        #RackFactory.print()
        
        logger.info("Create rack A1 DONE")
        RackFactory.create_rack_A2()
        #RackFactory.print()
        logger.info("Create rack A2 DONE")
        RackFactory.create_rack_B2()
        #RackFactory.print()
        logger.info("Create rack B2 DONE")
        #RackFactory.print()
        
        
        for rack in RackFactory.all_B2_racks: 
            farm.add_rack(rack)
        for rack in RackFactory.all_A1_racks: 
            farm.add_rack(rack)
        for rack in RackFactory.all_A2_racks: 
            farm.add_rack(rack)

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
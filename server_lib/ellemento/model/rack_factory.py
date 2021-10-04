from ellemento.model.shelf import Phase
from ellemento.model.rack import Rack
from ellemento.model import constants

from ellemento.model.rack import Rack 
from ellemento.model.shelf_factory import ShelfFactory
from lib.logging.logger_initialiser import EllementoLogger

logger = EllementoLogger.__call__().logger

class RackFactory:
    all_B2_racks = []
    all_A1_racks = [] 
    all_A2_racks = [] 
    max_idx_used = 0 

    @staticmethod # A1 has 8 phase 4 shelves, and 4 phase 5 shelves
    def create_rack_A1(): 
        # print("Length ", len(ShelfFactory.stage_4_shelves))
        # print("Stage 1 shelf " , len(ShelfFactory.stage_1_shelves))
        # print("Stage 2 shelf " , len(ShelfFactory.stage_2_shelves))
        # print("Stage 3 shelf " , len(ShelfFactory.stage_3_shelves))
        # print("Stage 4 shelf " , len(ShelfFactory.stage_4_shelves))
        # print("Stage 5 shelf " , len(ShelfFactory.stage_5_shelves))
        for idx in range (1, constants.NO_A1_RACKS + 1): 
            rack = Rack(RackFactory.create_rack(type_name="A1"))
            for i in range (1, constants.A1_RACKS_PH4 + 1):  # add 2 stage 3 shelf 
                ShelfFactory.assign_shelf_to_rack(rack = rack, phase = Phase.PHASE4)

            for i in range (1, constants.A1_RACKS_PH5 + 1):  # add 2 stage 3 shelf 
                ShelfFactory.assign_shelf_to_rack(rack = rack, phase = Phase.PHASE5)
            RackFactory.all_A1_racks.append(rack)
        pass 

    # A2 has only 12 phase 5 racks
    @staticmethod 
    def create_rack_A2(): 
        for idx in range (1, constants.NO_A2_RACKS + 1): 
            rack = Rack(RackFactory.create_rack(type_name="A2"))
            for i in range (1, constants.A2_RACKS_PH5 + 1):  # add 2 stage 3 shelf 
               ShelfFactory.assign_shelf_to_rack(rack = rack, phase = Phase.PHASE5)
            RackFactory.all_A2_racks.append(rack)
        pass 

    @staticmethod 
    def create_rack_B2(): # total 3 x 4 phase 5 shelves
        for idx in range (1, constants.NO_B2_RACKS +1): 
            rack = Rack(RackFactory.create_rack(type_name="B2"))
            # For each rack add shelf 

            for i in range (1, constants.B2_RACKS_PH1 + 1):  # add 2 stage 1 shelf 
                ShelfFactory.assign_shelf_to_rack(rack = rack, phase = Phase.PHASE1)
            for i in range (1, constants.B2_RACKS_PH2 + 1):  # add 2 stage 2 shelf 
                ShelfFactory.assign_shelf_to_rack(rack = rack, phase = Phase.PHASE2)
            for i in range (1, constants.B2_RACKS_PH3 + 1):  # add 2 stage 3 shelf 
                ShelfFactory.assign_shelf_to_rack(rack = rack, phase = Phase.PHASE3)
            for i in range (1, constants.B2_RACKS_PH5 + 1):  # add 2 stage 3 shelf 
                ShelfFactory.assign_shelf_to_rack(rack = rack, phase = Phase.PHASE5)
            RackFactory.all_B2_racks.append(rack)
        pass 
    
    @staticmethod  
    def create_rack(type_name = "default", id = -1):
        if (id == -1): 
            RackFactory.max_idx_used = RackFactory.max_idx_used + 1 
            id = RackFactory.max_idx_used
        rack_new = None
        #Tray.add_tray(tray_new)
        rack_new = Rack(id = id, type_name = type_name)
        # add shelves 
        # add pumps 

        Rack.add_rack(rack_new)
        return Rack.get_rack(id)

    @staticmethod 
    def print():
        Rack.print() 
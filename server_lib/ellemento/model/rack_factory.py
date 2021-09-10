from ellemento.model import shelf_factory
from ellemento.model.rack import Rack
from ellemento.model import constants

from ellemento.model.rack_factory import RackFactory
from ellemento.model.rack import Rack 
from ellemento.model.shelf_factory import ShelfFactory


class RackFactory:
    all_B2_racks = {}
    all_A1_racks = {} 
    all_A2_racks = {} 
    
    @staticmethod # A1 has 8 phase 4 shelves, and 4 phase 5 shelves
    def create_rack_A1(): 
        for idx in range (1, constants.NO_A1_RACKS): 
            rack = Rack(RackFactory.create_rack(type_name="A1", id = idx))
            for i in range (1, constants.A1_RACKS_PH4 + 1):  # add 2 stage 3 shelf 
                ShelfFactory.max_stage_4_used = ShelfFactory.max_stage_4_used + 1 
                stage_4_shelf = ShelfFactory.stage_4_shelves[ShelfFactory.max_stage_4_used]
                rack.add_shelf(stage_4_shelf)

            for i in range (1, constants.A1_RACKS_PH5 + 1):  # add 2 stage 3 shelf 
                ShelfFactory.max_stage_5_used = ShelfFactory.max_stage_5_used + 1 
                stage_5_shelf = ShelfFactory.stage_5_shelves[ShelfFactory.max_stage_5_used]
                rack.add_shelf(stage_5_shelf)
            RackFactory.all_A1_racks[rack.id] = rack
        pass 

    # A2 has only 12 phase 5 racks
    @staticmethod 
    def create_rack_A2(): 
        for idx in range (1, constants.NO_A2_RACKS): 
            rack = Rack(RackFactory.create_rack(type_name="A2", id = idx))
            for i in range (1, constants.A2_RACKS_PH5 + 1):  # add 2 stage 3 shelf 
                ShelfFactory.max_stage_5_used = ShelfFactory.max_stage_5_used + 1 
                stage_5_shelf = ShelfFactory.stage_5_shelves[ShelfFactory.max_stage_5_used]
                rack.add_shelf(stage_5_shelf)
            RackFactory.all_A2_racks[rack.id] = rack
        pass 

    @staticmethod 
    def create_rack_B2(): # total 3 x 4 phase 5 shelves
        for idx in range (1, constants.NO_B2_RACKS): 
            rack = Rack(RackFactory.create_rack(type_name="B2", id = idx))
            # For each rack add shelf 
            for i in range (1, constants.B2_RACKS_PH1 + 1):  # add 2 stage 1 shelf 
                ShelfFactory.max_stage_1_used = ShelfFactory.max_stage_1_used + 1 
                stage_1_shelf = ShelfFactory.stage_1_shelves[ShelfFactory.max_stage_1_used]
                rack.add_shelf(stage_1_shelf)
            for i in range (1, constants.B2_RACKS_PH2 + 1):  # add 2 stage 2 shelf 
                ShelfFactory.max_stage_2_used = ShelfFactory.max_stage_2_used + 1 
                stage_2_shelf = ShelfFactory.stage_2_shelves[ShelfFactory.max_stage_2_used]
                rack.add_shelf(stage_2_shelf)
            for i in range (1, constants.B2_RACKS_PH3 + 1):  # add 2 stage 3 shelf 
                ShelfFactory.max_stage_3_used = ShelfFactory.max_stage_3_used + 1 
                stage_3_shelf = ShelfFactory.stage_3_shelves[ShelfFactory.max_stage_3_used]
                rack.add_shelf(stage_3_shelf)
            for i in range (1, constants.B2_RACKS_PH5 + 1):  # add 2 stage 3 shelf 
                ShelfFactory.max_stage_5_used = ShelfFactory.max_stage_5_used + 1 
                stage_5_shelf = ShelfFactory.stage_5_shelves[ShelfFactory.max_stage_5_used]
                rack.add_shelf(stage_5_shelf)
            RackFactory.all_B2_racks[rack.id] = rack
        pass 
    
    @staticmethod  
    def create_rack(type_name = "default", id = -1):
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
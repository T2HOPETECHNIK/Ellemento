from ellemento.model.shelf import Shelf, Phase, ShelfStatus
from ellemento.model import constants 
from ellemento.model.tray_factory import TrayFactory

class ShelfFactory:
    max_shelf_id = 0 
    stage_1_shelves = {} #3
    stage_2_shelves = {} #4
    stage_3_shelves = {} #7 
    stage_4_shelves = {} #28 
    stage_5_shelves = {} #112   

    @staticmethod 
    def create_phase1_shelves(): 
        if len(ShelfFactory.stage_1_shelves) != 0: 
            return ShelfFactory.stage_1_shelves 
        for index in range (1, constants.TOTAL_PHASE1_SHELF + 1): 
            ShelfFactory.max_shelf_id = ShelfFactory.max_shelf_id + 1
            shelf_new = ShelfFactory.create_shelf(id = ShelfFactory.max_shelf_id)
            ShelfFactory.stage_1_shelves[shelf_new.id] = shelf_new
        # to do add trays inside the shelf 
        total_phase_1_tray = constants.TOTAL_PHASE1_SHELF * constants.TRAY_PER_SHELF
        for index in range(1, total_phase_1_tray+1): 
            pass 
        trays = TrayFactory.create_phase123_trays()

        return ShelfFactory.stage_1_shelves

    @staticmethod
    def create_phase2_shelves():   
        if len(ShelfFactory.stage_2_shelves) != 0: 
            return ShelfFactory.stage_2_shelves
        for index in range (1, constants.TOTAL_PHASE2_SHELF + 1): 
            ShelfFactory.max_shelf_id = ShelfFactory.max_shelf_id + 1
            shelf_new = ShelfFactory.create_shelf(id = ShelfFactory.max_shelf_id)
            ShelfFactory.stage_2_shelves[shelf_new.id] = shelf_new
        # to do add trays inside the shelf 
        return ShelfFactory.stage_2_shelves       

    @staticmethod 
    def create_phase3_shelves():
        if len(ShelfFactory.stage_3_shelves) != 0: 
            return ShelfFactory.stage_3_shelves 
        for index in range (1, constants.TOTAL_PHASE3_SHELF + 1): 
            ShelfFactory.max_shelf_id = ShelfFactory.max_shelf_id + 1
            shelf_new = ShelfFactory.create_shelf(id = ShelfFactory.max_shelf_id)
            ShelfFactory.stage_3_shelves[shelf_new.id] = shelf_new
        # to do add trays inside the shelf 
        return ShelfFactory.stage_3_shelves        


    @staticmethod
    def create_phase4_shelves():   
        if len(ShelfFactory.stage_4_shelves) != 0:
            return ShelfFactory.stage_4_shelves 
        for index in range (1, constants.TOTAL_PHASE4_SHELF + 1): 
            ShelfFactory.max_shelf_id = ShelfFactory.max_shelf_id + 1
            shelf_new = ShelfFactory.create_shelf(id = ShelfFactory.max_shelf_id)
            ShelfFactory.stage_4_shelves[shelf_new.id] = shelf_new
        # to do add trays inside the shelf 
        return ShelfFactory.stage_4_shelves       

    @staticmethod
    def create_phase5_shelves():  
        if len(ShelfFactory.stage_5_shelves) != 0:
            return ShelfFactory.stage_5_shelves 
        for index in range (1, constants.TOTAL_PHASE4_SHELF + 1): 
            ShelfFactory.max_shelf_id = ShelfFactory.max_shelf_id + 1
            shelf_new = ShelfFactory.create_shelf(id = ShelfFactory.max_shelf_id)
            ShelfFactory.stage_4_shelves[shelf_new.id] = shelf_new
        if len(ShelfFactory.stage_5_shelves) != 0:
            return ShelfFactory.stage_5_shelves 
        # to do add trays inside the shelf                   

    @staticmethod  
    def create_shelf(type_name = "default", id = -1):
        shelf_new = None
        #Tray.add_tray(tray_new)
        shelf_new = Shelf(id = id, type_name = type_name, max_tray = ShelfFactory.tray_per_shelf)
        # add trays, 
        # add water controls
        # add lights 
        Shelf.add_shelf(shelf_new)
        
        return Shelf.get_shelf(id)

    @staticmethod 
    def print():
        Shelf.print() 

    @staticmethod
    def get_empty_shelf_of_phase(phase = Phase.PHASE1): 
        lst_empty_shelf = [] 
        for shelf_x in Shelf.all_shelves:
            shelf_of_idx = Shelf.all_shelves[shelf_x]; 
            if shelf_of_idx.status == ShelfStatus.IDLE and shelf_of_idx.phase == phase: 
                lst_empty_shelf.append(shelf_of_idx)
        return lst_empty_shelf
import time 
from ellemento.model.tray import TrayStatus
from ellemento.model import tray_factory
from ellemento.model.shelf import Shelf, Phase, ShelfStatus
from ellemento.model import constants 
from ellemento.model.tray_factory import TrayFactory
from ellemento.model.tray_phase_1_3 import TrayPhase13
from ellemento.model.tray_phase_4 import TrayPhase4
from ellemento.model.tray_phase_5 import TrayPhase5
from lib.logging.logger_initialiser import EllementoLogger

logger = EllementoLogger.__call__().logger
class ShelfFactory:
    max_shelf_id = 0 
    stage_1_shelves = [] #3
    stage_2_shelves = [] #4
    stage_3_shelves = [] #7 
    stage_4_shelves = [] #28 
    stage_5_shelves = [] #112   
    max_stage_1_used = 0 
    max_stage_2_used = 0 
    max_stage_3_used = 0
    max_stage_4_used = 0
    max_stage_5_used = 0

    @staticmethod
    def reset_status_time_1(unit = 'second', duration = 3):
        if unit == 'second': 
            duration = duration
        elif unit == 'minute': 
            duration = duration * 60
        elif unit == 'hour':
            duration = duration * 3600
        elif unit == 'day':
            duration = duration *3600 * 24 
            
        for i in range (0, 3): 
            ShelfFactory.reset_status_time_phase1(index = i)
            logger.info("Phase 1 Sleeping ", duration, i + 1)
            time.sleep(duration)

        pass 

    @staticmethod
    def reset_status_time_2(unit = 'second', duration = 4):
        if unit == 'second': 
            duration = duration
        elif unit == 'minute': 
            duration = duration * 60
        elif unit == 'hour':
            duration = duration * 3600
        elif unit == 'day':
            duration = duration *3600 * 24 
            
        for i in range (0, 4): 
            ShelfFactory.reset_status_time_phase2(index = i)
            logger.info("Phase 2 Sleeping ", duration, i+1)
            time.sleep(duration)

        pass 
    
    @staticmethod
    def reset_status_time_3(unit = 'second', duration = 7):
        if unit == 'second': 
            duration = duration
        elif unit == 'minute': 
            duration = duration * 60
        elif unit == 'hour':
            duration = duration * 3600
        elif unit == 'day':
            duration = duration *3600 * 24 
            
        for i in range (0, 7): 
            ShelfFactory.reset_status_time_phase3(index = i)
            logger.info("Phase 3 Sleeping ", duration, i  + 1)
            time.sleep(duration)
        pass 

    @staticmethod
    def reset_status_time_4(unit = 'second', duration = 7):
        if unit == 'second': 
            duration = duration
        elif unit == 'minute': 
            duration = duration * 60
        elif unit == 'hour':
            duration = duration * 3600
        elif unit == 'day':
            duration = duration *3600 * 24 
            
        for i in range (0, 7):
            start_idx = i * 4
            end_index = i * 4 + 4 
            for j in range(start_idx, end_index):  
                logger.info("Shelf growing ", j)
                ShelfFactory.reset_status_time_phase4(index = j)
            logger.info("Phase 4 Sleeping ", duration, i + 1)
            time.sleep(duration)
        pass 

    @staticmethod
    def reset_status_time_5(unit = 'second', duration = 7):
        if unit == 'second': 
            duration = duration
        elif unit == 'minute': 
            duration = duration * 60
        elif unit == 'hour':
            duration = duration * 3600
        elif unit == 'day':
            duration = duration *3600 * 24 
            
        for i in range (0, 4): 
            start_idx = i * 16
            end_index = i * 16 + 16 
            for j in range(start_idx, end_index):  
                ShelfFactory.reset_status_time_phase5(index = j)
            logger.info("Phase 5 Sleeping ", duration, i + 1)
            time.sleep(duration)
        pass 

    @classmethod 
    def reset_status_time_phase1(self, index = 0):
        self.stage_1_shelves[index].reset_status_time()

    @classmethod 
    def reset_status_time_phase2(self, index = 0):
        self.stage_2_shelves[index].reset_status_time()

    @classmethod 
    def reset_status_time_phase3(self, index = 0):
        self.stage_3_shelves[index].reset_status_time()

    @classmethod 
    def reset_status_time_phase4(self, index = 0):
        self.stage_4_shelves[index].reset_status_time()

    @classmethod 
    def reset_status_time_phase5(self, index = 0):
        self.stage_5_shelves[index].reset_status_time()
    
    @staticmethod 
    def phase1_shelf_to_transfer(): 
        retList = [] 
        for shelf in ShelfFactory.stage_1_shelves: 
            if shelf.ready_to_transfer(): 
                retList.append(shelf)
        return retList

    @staticmethod 
    def phase2_shelf_to_transfer(): 
        retList = [] 
        for shelf in ShelfFactory.stage_2_shelves: 
            if shelf.ready_to_transfer(): 
                retList.append(shelf)
        return retList
    
    @staticmethod 
    def phase3_shelf_to_transfer(): 
        retList = [] 
        for shelf in ShelfFactory.stage_3_shelves: 
            if shelf.ready_to_transfer(): 
                retList.append(shelf)
        return retList

    @staticmethod 
    def phase4_shelf_to_transfer(): 
        retList = [] 
        for shelf in ShelfFactory.stage_4_shelves: 
            if shelf.ready_to_transfer(): 
                retList.append(shelf)
        return retList

    @staticmethod 
    def phase5_ready_to_transfer(): 
        retList = [] 
        for shelf in ShelfFactory.stage_5_shelves: 
            if shelf.ready_to_transfer(): 
                retList.append(shelf)
        return retList

    @staticmethod 
    def assign_shelf_to_rack(rack = None, phase = Phase.PHASE1): 
        if phase == Phase.PHASE1:
            if len(ShelfFactory.stage_1_shelves) > ShelfFactory.max_stage_1_used:
                stage_1_shelf = ShelfFactory.stage_1_shelves[ShelfFactory.max_stage_1_used]
                ShelfFactory.max_stage_1_used = ShelfFactory.max_stage_1_used + 1 
                rack.add_shelf(stage_1_shelf)
            else: 
                logger.error("Not enouch phase 1 shelf for the rack")
        if phase == Phase.PHASE2:
            if len(ShelfFactory.stage_2_shelves) > ShelfFactory.max_stage_2_used:
                stage_2_shelf = ShelfFactory.stage_2_shelves[ShelfFactory.max_stage_2_used]
                ShelfFactory.max_stage_2_used = ShelfFactory.max_stage_2_used + 1 
                rack.add_shelf(stage_2_shelf)
            else: 
                logger.error("Not enouch phase 2 shelf for the rack")
        if phase == Phase.PHASE3:
            if len(ShelfFactory.stage_3_shelves) > ShelfFactory.max_stage_3_used:
                stage_3_shelf = ShelfFactory.stage_3_shelves[ShelfFactory.max_stage_3_used]
                ShelfFactory.max_stage_3_used = ShelfFactory.max_stage_3_used + 1 
                rack.add_shelf(stage_3_shelf)
            else: 
                logger.error("Not enouch phase 3 shelf for the rack")
        if phase == Phase.PHASE4:
            if len(ShelfFactory.stage_4_shelves) > ShelfFactory.max_stage_4_used:
                stage_4_shelf = ShelfFactory.stage_4_shelves[ShelfFactory.max_stage_4_used]
                ShelfFactory.max_stage_4_used = ShelfFactory.max_stage_4_used + 1 
                rack.add_shelf(stage_4_shelf)
            else: 
                logger.error("Not enouch phase 4 shelf for the rack")
        if phase == Phase.PHASE5:
            if len(ShelfFactory.stage_5_shelves) > ShelfFactory.max_stage_5_used:
                stage_5_shelf = ShelfFactory.stage_5_shelves[ShelfFactory.max_stage_5_used]
                ShelfFactory.max_stage_5_used = ShelfFactory.max_stage_5_used + 1 
                rack.add_shelf(stage_5_shelf)
            else: 
                logger.error("Not enouch phase 5 shelf for the rack")

    @staticmethod 
    def create_phase1_shelves(): 
        if len(ShelfFactory.stage_1_shelves) != 0: 
            return ShelfFactory.stage_1_shelves 
        logger.info("Phase 1-2-3 trays creating")
        TrayFactory.create_phase123_trays()
        logger.info("Phase 1-2-3 trays created")
        for index in range (1, constants.TOTAL_PHASE1_SHELF + 1): 
            ShelfFactory.max_shelf_id = ShelfFactory.max_shelf_id + 1

            shelf_new = ShelfFactory.create_shelf(id = ShelfFactory.max_shelf_id, type_name="phase1")
              # hard coded to add tray 
            start_idx = (ShelfFactory.max_shelf_id - 1) * 9 + 1
            end_idx = ShelfFactory.max_shelf_id * 9 + 1
            for idx in range (start_idx, end_idx): 
                TrayFactory.all_phase123_trays[idx].status = TrayStatus.PHASE1
                tray = TrayFactory.all_phase123_trays[idx]
                #print("Add tray")
                tray.status = TrayStatus.PHASE1
                shelf_new.add_tray(tray)
                #print("Added tray")
            ShelfFactory.stage_1_shelves.append(shelf_new)
        # to do add trays inside the shelf 
        return ShelfFactory.stage_1_shelves

    @staticmethod
    def create_phase2_shelves():
        TrayFactory.create_phase123_trays()   
        if len(ShelfFactory.stage_2_shelves) != 0: 
            return ShelfFactory.stage_2_shelves
        for index in range (1, constants.TOTAL_PHASE2_SHELF + 1): 
            ShelfFactory.max_shelf_id = ShelfFactory.max_shelf_id + 1
            shelf_new = ShelfFactory.create_shelf(id = ShelfFactory.max_shelf_id, type_name="phase2")
            start_idx = (ShelfFactory.max_shelf_id - 1) * 9 + 1
            end_idx = ShelfFactory.max_shelf_id * 9 + 1
            for idx in range (start_idx, end_idx): 
                TrayFactory.all_phase123_trays[idx].status = TrayStatus.PHASE2
                tray = TrayFactory.all_phase123_trays[idx]
                shelf_new.add_tray(tray)
            ShelfFactory.stage_2_shelves.append(shelf_new)
        # to do add trays inside the shelf 
        return ShelfFactory.stage_2_shelves       

    @staticmethod 
    def create_phase3_shelves():
        TrayFactory.create_phase123_trays()
        if len(ShelfFactory.stage_3_shelves) != 0: 
            return ShelfFactory.stage_3_shelves 
        for index in range (1, constants.TOTAL_PHASE3_SHELF + 1): 
            ShelfFactory.max_shelf_id = ShelfFactory.max_shelf_id + 1
            shelf_new = ShelfFactory.create_shelf(id = ShelfFactory.max_shelf_id, type_name="phase3")
            start_idx = (ShelfFactory.max_shelf_id - 1) * 9 + 1
            end_idx = ShelfFactory.max_shelf_id * 9 + 1
            for idx in range (start_idx, end_idx): 
                TrayFactory.all_phase123_trays[idx].status = TrayStatus.PHASE3
                tray = TrayFactory.all_phase123_trays[idx]
                shelf_new.add_tray(tray)
            ShelfFactory.stage_3_shelves.append(shelf_new)
        # to do add trays inside the shelf 
        return ShelfFactory.stage_3_shelves        


    @staticmethod
    def create_phase4_shelves():   
        lists = TrayFactory.create_phase4_trays()
        #print("-------------------------------")
        #TrayFactory.print()
        #print(len(lists))
        if len(ShelfFactory.stage_4_shelves) != 0:
            return ShelfFactory.stage_4_shelves 
        for index in range (1, constants.TOTAL_PHASE4_SHELF + 1): 
            ShelfFactory.max_shelf_id = ShelfFactory.max_shelf_id + 1
            #print(ShelfFactory.max_shelf_id)
            shelf_new = ShelfFactory.create_shelf(id = ShelfFactory.max_shelf_id, type_name="phase4")
            start_idx = (ShelfFactory.max_shelf_id - 1) * 9 + 1
            end_idx = ShelfFactory.max_shelf_id * 9 + 1
            #print("Start idx", start_idx, end_idx)
            #print(len(TrayFactory.all_phase_4_trays))
            # for obj in TrayFactory.all_phase_4_trays: 
            #     TrayFactory.all_phase_4_trays[obj].print()
            for idx in range (start_idx, end_idx): 
                TrayFactory.all_phase_4_trays[idx].status = TrayStatus.PHASE4
                tray = TrayFactory.all_phase_4_trays[idx]
                shelf_new.add_tray(tray)
            ShelfFactory.stage_4_shelves.append(shelf_new)
        # to do add trays icnside the shelf 
        return ShelfFactory.stage_4_shelves       

    @staticmethod
    def create_phase5_shelves():  
        TrayFactory.create_phase5_trays()
        if len(ShelfFactory.stage_5_shelves) != 0:
            return ShelfFactory.stage_5_shelves 
        for index in range (1, constants.TOTAL_PHASE5_SHELF + 1): 
            ShelfFactory.max_shelf_id = ShelfFactory.max_shelf_id + 1
            shelf_new = ShelfFactory.create_shelf(id = ShelfFactory.max_shelf_id, type_name="phase5")
            start_idx = (ShelfFactory.max_shelf_id - 1) * 9 + 1
            end_idx = ShelfFactory.max_shelf_id * 9 + 1
            for idx in range (start_idx, end_idx): 
                TrayFactory.all_phase_5_trays[idx].status = TrayStatus.PHASE5
                tray = TrayFactory.all_phase_5_trays[idx]
                shelf_new.add_tray(tray)
            ShelfFactory.stage_5_shelves.append(shelf_new)
        if len(ShelfFactory.stage_5_shelves) != 0:
            return ShelfFactory.stage_5_shelves 
        # to do add trays inside the shelf                   

    @staticmethod  
    def create_shelf(type_name = "default", id = -1):
        shelf_new = None
        #Tray.add_tray(tray_new)
        shelf_new = Shelf(id = id, type_name = type_name, max_tray = constants.TRAY_PER_SHELF)
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
                if not shelf_of_idx not in lst_empty_shelf: 
                    lst_empty_shelf.append(shelf_of_idx)
        return lst_empty_shelf
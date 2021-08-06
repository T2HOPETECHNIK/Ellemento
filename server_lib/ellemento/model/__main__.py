from ellemento.model.tray_factory import TrayFactory
from ellemento.model.shelf_factory import ShelfFactory
from lib.logging.logger_initialiser import EllementoLogger

phase_1_shelves = 4
phase_2_shelves = 10 
phase_3_shelves = 14
phase_4_shelves = 56
phase_5_shelves = 224

logger = EllementoLogger.initialize_logger(); 



def init_trays(): 
    
    phase_1_2_3_trays = (phase_1_shelves + phase_2_shelves + phase_3_shelves) * 9 
    logger.info("Initializing phase 1, 2, 3, trays: %d", phase_1_2_3_trays)
    for i in range (1, phase_1_2_3_trays+1): 
        tray_new = TrayFactory.create_tray(id = i, type_name = "phase1-3")
    
    phase_4_trays = phase_4_shelves * 9
    logger.info("Initializing phase 4 trays : %d" , phase_4_shelves)
    for i in range (1, phase_4_trays + 1): 
        tray_new =  TrayFactory.create_tray(id = phase_1_2_3_trays + i, type_name = "phase4")
    
    phase_5_trays = phase_5_shelves * 9
    logger.info("Initializing phase 5 trays: %d ", phase_5_trays)
    for i in range (1, phase_5_trays + 1): 
        tray_new =  TrayFactory.create_tray(id = phase_1_2_3_trays + phase_4_trays + i, type_name = "phase5")

def init_shelves(): 
    for i in range (1, phase_1_shelves + 1):
         ShelfFactory.create_shelf(id = i, type_name="Phase 1 Shelf")


    for i in range (1, phase_2_shelves + 1):
         ShelfFactory.create_shelf(id = i + phase_1_shelves, type_name="Phase 2 Shelf")

    for i in range (1, phase_3_shelves + 1):
         ShelfFactory.create_shelf(id = i + phase_1_shelves + phase_2_shelves, type_name="Phase 3 Shelf")

    for i in range(1, phase_4_shelves + 1): 
         ShelfFactory.create_shelf(id = i + phase_1_shelves + phase_2_shelves + phase_3_shelves, type_name="Phase 4 Shelf")

    for i in range(1, phase_5_shelves + 1): 
        ShelfFactory.create_shelf(id = i + phase_1_shelves + phase_2_shelves + phase_3_shelves + phase_4_shelves, type_name="Phase 5 Shelf")


    pass 


if __name__ == '__main__':
    init_trays()
    init_shelves()
    ShelfFactory.print()
    #tray_new = TrayFactory.create_tray(id = 1, name = "phase1-3")
    TrayFactory.print()
    pass



def init_ventilation(): 
    pass 

def init_lights():
    pass

def init_water_controls(): 
    pass 




def init_racks(): 
    pass 

    
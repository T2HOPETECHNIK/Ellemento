from ellemento.model.tray_factory import TrayFactory
from ellemento.model.shelf_factory import ShelfFactory
from ellemento.model.light_factory import LightFactory
from ellemento.model.water_control_factory import WaterControlFactory
from ellemento.model.pump_control_factory import PumpControlFactory 
from ellemento.model.rack_factory import RackFactory
from ellemento.model.ventilation_control_factory import VentilationControlFactory
from lib.logging.logger_initialiser import EllementoLogger

phase_1_shelves = 4
phase_2_shelves = 10 
phase_3_shelves = 14
phase_4_shelves = 56
phase_5_shelves = 224
total_pumps = 10
total_racks = 16
total_fans = 5 

logger = EllementoLogger.initialize_logger(); 


def init_fans():
    logger.info("Initialize racks")
    for i in range (1, total_fans + 1): 
        VentilationControlFactory.create_fan(id = i)
    pass

def init_racks():
    logger.info("Initialize racks")
    for i in range (1, total_racks + 1): 
        RackFactory.create_rack(id = i)
    pass

def init_pumps():
    logger.info("Initialize pumps")
    for i in range (1, total_pumps + 1): 
        PumpControlFactory.create_valve(id = i)

# For initialization test 

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

def init_lights(): 
    total_lights = phase_1_shelves + phase_2_shelves + phase_3_shelves + phase_4_shelves + phase_3_shelves
    for i in range (1, total_lights + 1): 
        LightFactory.create_light(id = i)
    pass 

def init_water_controls(): 
    total_valves = phase_1_shelves + phase_2_shelves + phase_3_shelves + phase_4_shelves + phase_3_shelves
    for i in range (1, total_valves + 1): 
        WaterControlFactory.create_valve(id = i)
    pass 
    

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


def init_ventilation(): 
    pass 

if __name__ == '__main__':
    init_trays()
    init_lights() 
    init_water_controls()
    init_shelves()
    init_pumps()
    init_racks()
    init_fans()

    ShelfFactory.print()
    #tray_new = TrayFactory.create_tray(id = 1, name = "phase1-3")
    TrayFactory.print()
    LightFactory.print()
    WaterControlFactory.print()
    PumpControlFactory.print()
    RackFactory.print()
    VentilationControlFactory.print()

    pass





    
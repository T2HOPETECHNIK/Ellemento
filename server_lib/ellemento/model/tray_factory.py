from ellemento.model.tray import Tray
from ellemento.model.tray_phase_1_3 import TrayPhase13
from ellemento.model.tray_phase_4 import TrayPhase4
from ellemento.model.tray_phase_5 import TrayPhase5

class TrayFactory:
    @staticmethod  
    def create_tray(type_name = "Unknown", id = -1):
        tray_new = None
        if type_name in ["phase1", "phase 1", "phase 2", "phase2", "phase3", "phase 3", "phase1-3", "phase1-2-3"]: 
            tray_new = TrayPhase13(id = id, type_name = "phase1-3")
        elif type_name in ["phase4", "phase 4"]:
            tray_new = TrayPhase4(id = id, type_name = "phase4")
        elif type_name in ["phase5", "phase 5"]:
            tray_new = TrayPhase5(id = id, type_name = "phase5")
        else:
            raise TypeError("Invalid type of trays created: "+ type_name)
        Tray.add_tray(tray_new)
        return Tray.get_tray(id)

    @staticmethod 
    def print():
        Tray.print_tray() 
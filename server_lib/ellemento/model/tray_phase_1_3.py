from ellemento.model.tray import TrayStatus, Tray

class TrayPhase13(Tray):
    def __init__(self, id = 0, dimensions = [12, 10], type_name="Unknown"):
        super().__init__(id, dimensions, type_name)

    def sow(self):
        self.has_veg = True 
    
    # fill an tray with pots foams 
    def fill_foam(self): 
        self.has_foam = True

    # Transfer from sower -> phase1 rack -> phase 2 rack -> phase 3 rack -> 3-4 transplantor 

    # vegetabal is transplanted to phase 4 trays 
    def transplant_out(self): 
        self.has_veg = False 
    
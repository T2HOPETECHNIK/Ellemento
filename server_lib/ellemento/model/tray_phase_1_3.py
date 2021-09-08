from ellemento.model.tray import TrayStatus, Tray


class TrayPhase13(Tray):
    MAX_TRANSPLANT_OUT = 4 

    def __init__(self, id = 0, dimensions = [12, 10], type_name="Unknown"):
        super().__init__(id, dimensions, type_name)
        self._count_transplant_out = 0

    def sow(self):
        self.has_veg = True 
        self._count_transplant_out = 0
    
    # fill an tray with pots foams 
    def fill_foam(self): 
        self.has_foam = True

    # Transfer from sower -> phase1 rack -> phase 2 rack -> phase 3 rack -> 3-4 transplantor 

    # vegetabal is transplanted to phase 4 trays 
    def transplant_out(self): 
        if self._count_transplant_out >= self.MAX_TRANSPLANT_OUT: 
            raise Exception("The tray is empty, not able to transplant")
        
        self._count_transplant_out = self._count_transplant_out + 1 
        if self._count_transplant_out == self.MAX_TRANSPLANT_OUT: 
            self.has_veg = False 
from ellemento.model.tray import TrayStatus, Tray

class TrayPhase5(Tray):
    def __init__(self, id = 0, dimensions = [12, 10], type_name="Unknown"):
        super().__init__(id, dimensions, type_name)

    def transfer(self):
        self.has_veg = True 

    def transplant_in(self):
        self.has_veg = True 
    
    def harvest(self):
        self.has_veg = False 
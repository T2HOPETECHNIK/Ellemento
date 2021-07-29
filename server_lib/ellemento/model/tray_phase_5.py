from ellemento.model.tray import TrayStatus, Tray

class TrayPhase5(Tray):
    def __init__(self, id):
        super().__init__(id)

    def transfer(self):
        self.has_veg = True 

    def transplant_in(self):
        self.has_veg = True 
    
    def harvest(self):
        self.has_veg = False 
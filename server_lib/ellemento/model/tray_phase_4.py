from ellemento.model.tray import TrayStatus, Tray

class TrayPhase4(Tray):
    def __init__(self, id = 0, dimensions = [12, 10], type_name="Unknown"):
        super().__init__(id, dimensions, type_name)
    
    def transfer(self):
        self.has_veg = True 

    def transplant_out(self):
        super().transplant()
        self.has_veg = False

    def transplant_in(self):
        self.has_veg = True
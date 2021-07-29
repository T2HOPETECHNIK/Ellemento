from ellemento.model.tray import TrayStatus, Tray

class TrayPhase4(Tray):
    def __init__(self, id):
        super().__init__(id)

    def transfer(self):
        self.has_veg = True 

    def transplant_in(self):
        super().transplant()
        self.has_veg = False

    def transplant_in(self):
        self.has_veg = False
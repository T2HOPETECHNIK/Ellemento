from ellemento.model.tray import TrayStatus, Tray


class TrayPhase4(Tray):
    MAX_TRANSPLANT_OUT = 4

    def __init__(self, id=0, dimensions=None, type_name="Unknown"):
        super().__init__(id, dimensions, type_name)
        if dimensions is None:
            dimensions = [12, 10]
        self._count_transplant_out = 0

    def transfer(self):
        self.has_veg = True

    def transplant_out(self):
        super().transplant()
        if self._count_transplant_out >= self.MAX_TRANSPLANT_OUT:
            raise Exception("Tray is empty, not able to transplant")

        self._count_transplant_out = self._count_transplant_out + 1
        if self._count_transplant_out == self.MAX_TRANSPLANT_OUT:
            self.has_veg = False

    def transplant_in(self):
        self.has_veg = True
        self._count_transplant_out = 0

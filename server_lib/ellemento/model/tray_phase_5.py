from ellemento.model.tray import TransferStatus, TrayStatus, Tray

class TrayPhase5(Tray):
    def __init__(self, id = 0, dimensions = [12, 10], type_name="Unknown"):
        super().__init__(id, dimensions, type_name)

    def transfer(self):
        self.has_veg = True 

    def transplant_in(self):
        self.has_veg = True 
    
    def harvest(self):
        self.reset_status_time()
        self.status = TrayStatus.DIRTY
        self.set_transfer_status(TransferStatus.IDLE)
        self.has_veg = False 

    def __repr__(self):
        return "<object:%s id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)

    def __str__(self):
        return "<object:%s, id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)

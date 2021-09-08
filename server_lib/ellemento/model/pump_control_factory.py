from ellemento.model.pump_control import PumpControl

class PumpControlFactory:
    @staticmethod  
    def create_valve(type_name = "Default", id = -1):
        pump_new = None
        #Tray.add_tray(tray_new)
        pump_new = PumpControl(id = id, type_name = type_name)
        PumpControl.add_pump(pump_new)
        return PumpControl.get_pump(id)

    @staticmethod 
    def print():
        PumpControl.print() 
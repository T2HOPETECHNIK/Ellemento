from ellemento.model.water_control import WaterControl

class WaterControlFactory:
    @staticmethod  
    def create_valve(type_name = "Default", id = -1):
        valve = None
        #Tray.add_tray(tray_new)
        valve = WaterControl(id = id, type_name = type_name)
        WaterControl.add_valve(valve)
        return WaterControl.get_valve(id)

    @staticmethod 
    def print():
        WaterControl.print() 
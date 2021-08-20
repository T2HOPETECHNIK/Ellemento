from ellemento.model.ventilation_control import VentilationControl

class VentilationControlFactory:
    @staticmethod  
    def create_fan(type_name = "Default", id = -1):
        fan = None
        #Tray.add_tray(tray_new)
        fan = VentilationControl(id = id, type_name = type_name)
        VentilationControl.add_fan(fan)
        return VentilationControl.get_fan(id)

    @staticmethod 
    def print():
        VentilationControl.print() 
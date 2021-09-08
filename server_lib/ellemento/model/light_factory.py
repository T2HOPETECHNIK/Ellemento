from ellemento.model.light_control import LightControl

class LightFactory:
    @staticmethod  
    def create_light(type_name = "Default", id = -1):
        light_new = None
        #Tray.add_tray(tray_new)
        light_new = LightControl(id = id, type_name = type_name)
        LightControl.add_light(light_new)
        return LightControl.get_light(id)

    @staticmethod 
    def print():
        LightControl.print() 
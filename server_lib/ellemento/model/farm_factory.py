from ellemento.model.farm import Farm

class FarmFactory:
    @staticmethod  
    def create_farm(type_name = "Default", id = -1):
        farm_new = None
        #Tray.add_tray(tray_new)
        farm_new = Farm(id = id, type_name = type_name)
        # Add fans 
        # Add racks 
        #   
        Farm.add_farm(farm_new)
   
        return Farm.get_farm(id)

    @staticmethod 
    def print():
        Farm.print() 
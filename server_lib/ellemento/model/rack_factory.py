from ellemento.model.rack import Rack


class RackFactory:
    @staticmethod 
    def create_rack_A1(): 
        pass 

    @staticmethod 
    def create_rack_A2(): 
        pass 

    @staticmethod 
    def create_rack_B2(): 
        pass 
    

    @staticmethod  
    def create_rack(type_name = "default", id = -1):
        rack_new = None
        #Tray.add_tray(tray_new)
        rack_new = Rack(id = id, type_name = type_name)
        # add shelves 
        # add pumps 

        Rack.add_rack(rack_new)
        return Rack.get_rack(id)

    @staticmethod 
    def print():
        Rack.print() 
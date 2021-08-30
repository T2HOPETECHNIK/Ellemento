from ellemento.model.buffer import Buffer

class FarmFactory:
    @staticmethod  
    def create_buffer(type_name = "Default", id = -1):
        buffer_new = None
        #Tray.add_tray(tray_new)
        buffer_new = Buffer(id = id, type_name = type_name)
        # Add fans 
        # Add racks 
        #   
        Buffer.add_buffer(buffer_new)
   
        return Buffer.get_buffer(id)

    @staticmethod 
    def print():
        Buffer.print() 

from ellemento.plc.modbus_io import PLCManager


# Used to hold all the modbus io 
class ModbusIOManager(object):  
    modbus_io_dict = [[]]; 
    def __init__ (self):
        super().__init__()
        

    @staticmethod
    def create_modbus_io(): 
        # to do - Load all mod bus from init file 
        # read json file 
        # Create PLCS
        # add to the dict 
        pass  
    
    def __add_modbus_io(self, plc):
        # add pic to the master list 
        ModbusIOManager.create_modbus_io[plc.id] = plc; 

    def __get_modbus_io(self, id): 
        return ModbusIOManager.create_modbus_io[id]


import json, os
# Local library import
from ellemento.bridge.plc_bridge import ModelPlcBridge
from ellemento.bridge.light_bridge import LightModelPlcBridge 
from ellemento.bridge.valve_bridge import ValveModelPlcBridge
from ellemento.bridge.pump_bridge import PumpModelPlcBridge
from ellemento.bridge.shelf_bridge import ShelfModelPlcBridge
from ellemento.bridge.rack_bridge import RackModelPlcBridge
from lib.logging.logger_initialiser import EllementoLogger
logger = EllementoLogger.__call__().logger

class ModelPlcBridgeFactory: 
    
    light_plc_bridge_dict = {}
    valve_plc_bridge_dict = {} 
    pump_plc_bridge_dict = {}
    shelf_plc_bridge_dict = {}  
    rack_plc_bridge_dict = {} 

    @classmethod 
    def get_bridge(self, type = None, id = -1):
        if  len(self.light_plc_bridge_dict) == 0: 
            self.build_bridge()
        if type == "Light": 
            if id in  self.light_plc_bridge_dict:
                return self.light_plc_bridge_dict[id]
            else:  
                return None 
        elif type == "Valve":
            if id in self.valve_plc_bridge_dict: 
                return self.valve_plc_bridge_dict[id]
            else: 
                return None 
        elif type == "Pump": 
            if id in self.pump_plc_bridge_dict: 
                return self.pump_plc_bridge_dict[id] 
            else: 
                return None 
        elif type == "Shelf":
            if id in  self.shelf_plc_bridge_dict:  
                return self.shelf_plc_bridge_dict[id]
            else: 
                return None 
        elif type == "Rack": 
            if id in self.rack_plc_bridge_dict: 
                return self.rack_plc_bridge_dict[id]
            else: 
                return None

    @classmethod
    def build_bridge(self): 
        #  step 1 load cfg file 
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        init_file = script_dir + "\\" + "model_plc_mapping.json"
        logger.info(init_file)
        json_file = open(init_file)
        self.cfg = json.load(json_file)
        self.build_light_bridge(self.cfg['Light'])
        self.build_valve_bridge(self.cfg['valve'])
        pass 

    @classmethod
    def build_light_bridge(self, light_cfg): 
        for light_brg in light_cfg:
            light_id = light_brg['id']
            mod_bus_id = light_brg['address']['modbus_id'] 
            lt_bridge = LightModelPlcBridge(light_id = light_id, plc_id=mod_bus_id, address = light_brg['address'])
            self.light_plc_bridge_dict[light_id ] = lt_bridge

    @classmethod
    def build_valve_bridge(self, valve_cfg): 
        print(valve_cfg)
        for valve_brg in valve_cfg:
            valve_id = valve_brg['id']
            mod_bus_id = valve_brg['address']['modbus_id'] 
            valve_bridge = ValveModelPlcBridge(valve_id = valve_id, plc_id=mod_bus_id, address = valve_brg['address'])
            print(",,,,,,,,,,,,,,,", valve_id)
            self.valve_plc_bridge_dict[valve_id ] = valve_bridge

    @classmethod
    def build_pump_bridge(self, pump_cfg): 
        print(pump_cfg)
        for pump_brg in pump_cfg:
            pump_id = pump_brg['id']
            mod_bus_id = pump_brg['address']['modbus_id'] 
            pump_bridge = PumpModelPlcBridge(valve_id = pump_id, plc_id=mod_bus_id, address = pump_brg['address'])
            print(",,,,,,,,,,,,,,,", pump_id)
            self.pump_plc_bridge_dict[pump_id ] = pump_bridge

    @classmethod
    def build_shelf_bridge(self, shelf_cfg): 
        print(shelf_cfg)
        for shelf_brg in shelf_cfg:
            shelf_id = shelf_brg['id']
            mod_bus_id = shelf_brg['address']['modbus_id'] 
            shelf_bridge = ShelfModelPlcBridge(shelf_id = shelf_id, plc_id=mod_bus_id, address = shelf_brg['address'])
            print(",,,,,,,,,,,,,,,", shelf_id)
            self.shelf_plc_bridge_dict[shelf_id ] = shelf_bridge
    

    @classmethod
    def build_rack_bridge(self, rack_cfg): 
        print(rack_cfg)
        for rack_brg in rack_cfg:
            rack_id = rack_cfg['id']
            mod_bus_id = rack_cfg['address']['modbus_id'] 
            rack_bridge = RackModelPlcBridge(rack_id = rack_id, plc_id=mod_bus_id, address = rack_brg['address'])
            print(",,,,,,,,,,,,,,,", rack_id)
            self.rack_plc_bridge_dict[rack_id ] = rack_bridge
    

    def __init__(self):
        pass

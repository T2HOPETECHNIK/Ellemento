import json, os
# Local library import
from ellemento.bridge.plc_bridge import ModelPlcBridge
from ellemento.bridge.light_bridge import LightModelPlcBridge 
from ellemento.bridge.valve_bridge import ValveModelPlcBridge 
from lib.logging.logger_initialiser import EllementoLogger
logger = EllementoLogger.__call__().logger

class ModelPlcBridgeFactory: 
    
    light_plc_bridge_dict = {}
    valve_plc_bridge_dict = {} 
    pump_plc_bridge_dict = {} 

    @classmethod 
    def get_bridge(self, type = None, id = -1):
        if  len(self.light_plc_bridge_dict) == 0: 
            self.build_bridge()
        
        if type == "Light": 
            return self.light_plc_bridge_dict[id]
        elif type == "Valve":
            return self.valve_plc_bridge_dict[id]
        elif type == "Pump": 
            return self.pump_plc_bridge_dict[id] 

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
            pump_bridge = ValveModelPlcBridge(valve_id = pump_id, plc_id=mod_bus_id, address = pump_brg['address'])
            print(",,,,,,,,,,,,,,,", pump_id)
            self.pump_plc_bridge_dict[pump_id ] = pump_bridge
    
    def __init__(self):
        pass

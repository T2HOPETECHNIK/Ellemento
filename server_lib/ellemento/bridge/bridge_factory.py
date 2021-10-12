import json, os
# Local library import
from ellemento.bridge.plc_bridge import ModelPlcBridge
from ellemento.bridge.light_bridge import LightModelPlcBridge 
from lib.logging.logger_initialiser import EllementoLogger
logger = EllementoLogger.__call__().logger

class ModelPlcBridgeFactory: 
    
    light_plc_bridge_dict = {}
    @classmethod 
    def get_bridge(self, type = None, id = -1):
        if  len(self.light_plc_bridge_dict) == 0: 
            self.build_bridge()
        
        if type == "Light": 
            return self.light_plc_bridge_dict[id]

    @classmethod
    def build_bridge(self): 
        #  step 1 load cfg file 
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        init_file = script_dir + "\\" + "model_plc_mapping.json"
        logger.info(init_file)
        json_file = open(init_file)
        self.cfg = json.load(json_file)
        self.build_light_bridge(self.cfg['Light'])
        pass 

    @classmethod
    def build_light_bridge(self, light_cfg): 
        print(light_cfg)
        for light_brg in light_cfg:
            light_id = light_brg['id']
            mod_bus_id = light_brg['address']['modbus_id'] 
            lt_bridge = LightModelPlcBridge(light_id = light_id, plc_id=mod_bus_id, address = light_brg['address'])
            print(",,,,,,,,,,,,,,,", light_id)
            self.light_plc_bridge_dict[light_id ] = lt_bridge
    
    def __init__(self):
        pass

# The code here is to bridge plc and 
# Global libary import 
import json 
import os
import sys 

# Local library import 
from lib.logging.logger_initialiser import EllementoLogger
logger = EllementoLogger.__call__().logger

class ModelPlcBridge:

    
    def __init__(self, id = -1, type_name = "Default"): 
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        init_file = script_dir + "\\" + "model_plc_mapping.json"
        logger.info(init_file)
        json_file = open(init_file)
        self.cfg = json.load(json_file)
        for key in self.cfg: 
            print(key)
            value_list = self.cfg[key]
            if type(value_list) is list:
                
                for obj in value_list: 
                    print(obj['id'])
                    
                    #ModelPlcBridge.ModelPlcDict[key] = 
                    

    
    def print_model(self, type = "Light", id = 1): 
        print(self.cfg[type])
        #all_lights = json.load(self.cfg[type])
        #print(all_lights)

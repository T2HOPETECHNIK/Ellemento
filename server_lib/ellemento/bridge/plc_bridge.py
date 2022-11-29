import json
import os
# Local library import 
from lib.logging.logger_initialiser import EllementoLogger

logger = EllementoLogger.__call__().logger


class ModelPlcBridge:

    def __init__(self):
        script_dir = os.path.dirname(__file__)
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

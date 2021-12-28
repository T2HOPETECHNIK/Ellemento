import json
import os
import sys
from ellemento.plc.plc_io import PLCManager
from lib.logging.logger_initialiser import EllementoLogger

logger = EllementoLogger.__call__().logger


# Used to hold all the modbus io
class PlcIOManager(object):
    plc_io_dict = {}

    def __init__(self):
        super().__init__()

    @classmethod
    def get_plc_io(self, **kwargs):
        if len(self.plc_io_dict) == 0:
            # create modbus io if not defined
            self.create_plc_io()

        for key, value in kwargs.items():
            if key == 'name':
                return PlcIOManager.plc_io_dict[value]
            if key == "id":
                return PlcIOManager.plc_io_dict[value]
            if key == 'ip':
                return PlcIOManager.plc_io_dict[value]
            if key == 'ads':
                return PlcIOManager.plc_io_dict[value]

    @staticmethod
    def print_modbus_io():
        for key, value in PlcIOManager.plc_io_dict.items():
            print(key, ':')
            print(value)

    @staticmethod
    def create_plc_io():
        try:
            script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
            init_file = script_dir + "\\" + "plc_address.json"
            logger.info(init_file)
            json_file = open(init_file)
            cfg = json.load(json_file)
            json_file.close()
            for x in cfg['PlcAddress']:
                plc_from_json = PLCManager(cfg=x)
                print(x['ip'])
                PlcIOManager.plc_io_dict[x['name']] = plc_from_json
                PlcIOManager.plc_io_dict[x['id']] = plc_from_json
                PlcIOManager.plc_io_dict[x['ip']] = plc_from_json
                PlcIOManager.plc_io_dict[x['ads']] = plc_from_json
                #print('hell',x['name'])
            return len(cfg['PlcAddress'])
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise

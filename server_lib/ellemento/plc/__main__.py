from ellemento.plc.plc_io_manager import PlcIOManager
from lib.logging.logger_initialiser import EllementoLogger
logger = EllementoLogger.__call__().logger
var = 0
if __name__ == '__main__':
    mod1 = PlcIOManager.get_plc_io(id=1)
    res, err = mod1.read_address_json(1001, 1)
    mod1.write_address_json(4085, 100)
    print(res.registers)
    '''while True:
        #time.sleep(1)
        var = var + 10
        mod1.write_register(4085, var)
        res,err = mod1.read_register(4085,1)
        print(res.registers)'''

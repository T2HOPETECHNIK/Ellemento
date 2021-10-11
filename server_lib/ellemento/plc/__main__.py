from ellemento.plc.modbus_io_manager import ModbusIOManager
from lib.logging.logger_initialiser import EllementoLogger
from ellemento.plc.modbus_io import PLCManager

logger = EllementoLogger.__call__().logger

if __name__ == '__main__': 
    num_modbus = ModbusIOManager.create_modbus_io()
    logger.debug("Number of modbus %d " , ( num_modbus))
    mod1 = ModbusIOManager.get_modbus_io(id=1)
    #ModbusIOManager.print_modbus_io()
   
    res, err = mod1.read_register(1001, 3)
    res, err = mod1.read_register(4022, 3)
    mod1.read_register(4020, 3)
    mod1.write_register(4022, 100)

    print(res)
    print(err)

    #print(mod1)
    # print(mod1.name)
    # print(mod1.ip)
    # print(mod1.id)
    # print(mod1.address['modeAddress'])
    #ModbusIOManager.print_modbus_io()
    
from ellemento.plc.modbus_io_manager import ModbusIOManager
from lib.logging.logger_initialiser import EllementoLogger

if __name__ == '__main__':
    logger = EllementoLogger.initialize_logger(); 
    num_modbus = ModbusIOManager.create_modbus_io()
    logger.debug("Number of modbus %d " , ( num_modbus))
    mod1 = ModbusIOManager.get_modbus_io(id=1)
    #print(mod1)
    print(mod1.name)
    print(mod1.ip)
    print(mod1.id)
    print(mod1.address['modeAddress'])
    #ModbusIOManager.print_modbus_io()
    
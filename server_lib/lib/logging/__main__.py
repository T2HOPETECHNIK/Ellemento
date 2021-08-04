from logging import log
from lib.logging.logger_initialiser import EllemengtoLogger
from ellemento.plc.modbus_io_manager import ModbusIOManager

if __name__ == '__main__':
    logger = EllemengtoLogger.initialize_logger()
    ModbusIOManager.create_modbus_io()
    logger.info("test") 
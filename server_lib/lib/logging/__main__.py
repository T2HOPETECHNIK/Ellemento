from lib.logging.logger_initialiser import EllementoLogger
from ellemento.plc.modbus_io_manager import ModbusIOManager

if __name__ == '__main__':
    logger = EllementoLogger.initialize_logger()
    logger.info("test") 
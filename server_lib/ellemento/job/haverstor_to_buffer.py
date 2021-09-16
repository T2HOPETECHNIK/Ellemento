# Interfacing with ASRS to execute transfer job
from logging import Logger
import threading
import time
from multiprocessing import Process
import os

from ellemento.model.tray import Tray
from ellemento.model.tray_phase_1_3 import TrayPhase13
from ellemento.model.tray_phase_4 import TrayPhase4
from ellemento.model.harvestor import Harvestor 
from ellemento.model.bufffer_factory import BufferFactory, BufferType
from ellemento.model.buffer import Buffer 

from lib.logging.logger_initialiser import EllementoLogger


logger = EllementoLogger.__call__().logger

class HarvestorToBuffer:   
    harvestor_to_buffer_job = None 
    terminate_job = False 

    @staticmethod 
    def create_job():
        while not HarvestorToBuffer.terminate_job:
            harvestor = Harvestor(Harvestor.get_harvestor())
            buffer_5 = Buffer(BufferFactory.get_buffer(BufferType.BUFFER_5))

            if not harvestor.ready_to_unload: 
                logger.info("Harvestor is not ready")
                time.sleep(2)
                continue 

            if buffer_5.full: 
                logger.info("Buffer is full, not ready to load the tray")
                time.sleep(2)
                continue           
            job = HarvestorToBuffer(1)
            job.set_source(harvestor)
            job.set_destination(buffer_5)
            HarvestorToBuffer.harvestor_to_buffer_job = job
            time.sleep(2)

    def __init__(self, id = -1, type_name = 'Default'):
        self._source = None
        self._id = id 
        self._type_name = type_name
        self._destination = None 
        pass

    def set_source(self, harvestor):
        if harvestor == None: 
            raise Exception("Source harvestor shall not be none")
        self._source = harvestor  
        pass 

    def set_destination(self, buffer):
        if buffer == None: 
            raise Exception("Destination buffer shall not be none")
        self._destination = buffer 
        pass

    def execute(self): 
        # 
        pass 
   
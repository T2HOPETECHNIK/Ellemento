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

    @classmethod
    def execute_job(cls):
        # execute harvestor to buffer
        while not cls.terminate_job:
            print("Executing harvestor job")
            if cls.harvestor_to_buffer_job is None:
                print("Not having harvestor to buffer job")
                time.sleep(2)
                continue
            ret = cls.harvestor_to_buffer_job.execute()
            if ret:
                cls.harvestor_to_buffer_job = None
            else:
                print("Not able to execute harvestor job")
            time.sleep(2)
            continue
        pass

    @staticmethod 
    def create_job():
        while not HarvestorToBuffer.terminate_job:
            harvestor = Harvestor(Harvestor.get_harvestor())
            buffer_5 = Buffer(BufferFactory.get_buffer(BufferType.BUFFER_5))

            if not harvestor.ready_to_unload: 
                print("Harvestor is not ready")
                logger.info("Harvestor is not ready")
                time.sleep(2)
                continue 

            if buffer_5.full: 
                print("Buffer is full, not ready to load the tray")
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
        self._source.harvest()
        tray = self._source.unload_tray()
        if tray is None:
            print("Failed to unload tray from harvestor")
            return False
        tray.harvest()
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        self._destination.load(tray)
        return True
   
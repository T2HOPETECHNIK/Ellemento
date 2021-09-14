# Interfacing with ASRS to execute transfer job
from ellemento.model.tray import Tray
from ellemento.model.tray_phase_1_3 import TrayPhase13
from ellemento.model.tray_phase_4 import TrayPhase4
from ellemento.model.harvestor import Harvestor 
from ellemento.model.bufffer_factory import BufferFactory, BufferType
import threading
import time
from multiprocessing import Process
import os

class HarvestorToBuffer:   
    harvestor_to_buffer_job = None 

    @staticmethod 
    def create_job():
        job = HarvestorToBuffer(1)
        harvestor = Harvestor.get_harvestor()
        buffer_5 = BufferFactory.get_buffer(BufferType.BUFFER_5)
        job.set_source(harvestor)
        job.set_destination(buffer_5)
        HarvestorToBuffer.harvestor_to_buffer_job = job
        return HarvestorToBuffer.harvestor_to_buffer_job 

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
   
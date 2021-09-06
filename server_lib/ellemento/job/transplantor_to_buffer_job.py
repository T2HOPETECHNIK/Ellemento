# Interfacing with ASRS to execute transfer job
from ellemento.model.transplantor_factory import TransplantorFactory
import threading
import time
from multiprocessing import Process
import os

from ellemento.model.transplantor_factory import TransplantorFactory
from ellemento.model.tray import Tray
from ellemento.model.tray_phase_1_3 import TrayPhase13
from ellemento.model.tray_phase_4 import TrayPhase4
from ellemento.model.bufffer_factory import BufferFactory, BufferType



class TransplantorToBufferJob:
    tranplantor_to_buffer_jobs = {} 

    @staticmethod 
    def create_jobs(): 
        
        transplantor_3_4 = TransplantorFactory.get_transplator_3_4() 
        buffer_3_in = BufferFactory.get_buffer(BufferType.BUFFER_3_IN)
        TransplantorToBufferJob.create_Job(id = 1, src_transplantor =  transplantor_3_4, dst_buffer =  buffer_3_in)


    @staticmethod 
    def create_Job(id = -1, src_transplantor = None, dst_buffer = None): 
        job = TransplantorToBufferJob(id = id)
        job.set_source(src_transplantor)
        job.set_destination(dst_buffer)
        TransplantorToBufferJob.tranplantor_to_buffer_jobs[id] = job  
        return job        

    def __init__(self, id = -1, type_name = 'Default'):
        if id <= -1: 
            raise Exception("Invalid id -1")
        self._source  = None
        self._id = id 
        self._type_name = type_name
        self._destination = None 
        pass

    def set_source(self, transplantor):
        if transplantor == None: 
            raise Exception("Source transplantor cannot be None")
        self._source = transplantor  
        pass 

    def set_destination(self, buffer):
        if buffer == None: 
            raise Exception("Destination buffer cannot be None")
        self._destination = buffer  
        pass

    def execute(self): 
        # 
        pass 
   
from ellemento.model import transplantor
from multiprocessing.context import BufferTooShort
import threading
import time
from multiprocessing import Process
import os

# Interfacing with ASRS to execute transfer job
from ellemento.model.tray import Tray
from ellemento.model.tray_phase_1_3 import TrayPhase13
from ellemento.model.tray_phase_4 import TrayPhase4
from ellemento.model.bufffer_factory import BufferFactory, BufferType
from ellemento.model.transplantor_factory import TransplantorFactory
from lib.logging.logger_initialiser import EllementoLogger

logger = EllementoLogger.__call__().logger


class BufferToTransplantorJob:
    buffer_to_transplantor_jobs = {}   
    @staticmethod 
    def create_jobs():
        # create jobs for 
        buffer_3_in = BufferFactory.get_buffer(BufferType.BUFFER_3_IN)
        transplantor_3_4 = TransplantorFactory.get_transplator_3_4() 
        BufferToTransplantorJob.create_job(id = 1, src_buffer=buffer_3_in, dst_tranplantor=transplantor_3_4)
        pass 

    @staticmethod 
    def create_job(id = -1, src_buffer = None, dst_tranplantor = None ): 
        if src_buffer == None or dst_tranplantor == None: 
            logger.info("Source or destination not ready")
            return None 
        job = BufferToTransplantorJob(id = id)
        job.set_source(src_buffer)
        job.set_destination(dst_tranplantor)
        BufferToTransplantorJob.buffer_to_transplantor_jobs[id] = job 
        pass 

    def __init__(self, id = -1, type_name = 'Default'):
        self._source_buffer = None
        self._id = id 
        self._type_name = type_name
        self._destination_trans = None 
        pass

    def set_source(self, buffer):
        if buffer == None: 
            raise Exception("Source buffer can not be None")
        self._source_buffer = buffer 
        pass 

    def set_destination(self, transplantor): 
        if transplantor == None: 
            raise Exception("Destination transplantor can not be None")

        self._destination_trans = transplantor
        pass

    def execute(self): 
        # 
        pass 
   
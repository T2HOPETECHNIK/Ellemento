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
from ellemento.model.sower import Sower
from ellemento.model.transplantor import Transplantor 

from lib.logging.logger_initialiser import EllementoLogger

logger = EllementoLogger.__call__().logger

class TransplantorToSower:
    transplantor_to_sower_jobs = {}   
    termninate_job = False 
    @staticmethod 
    def create_jobs():
        # create jobs for 
        while not TransplantorToSower.termninate_job: 
            transplantor_3_4 = Transplantor(TransplantorFactory.get_transplantor_3_4()) 
            sower = Sower(Sower.get_sower())
            if not transplantor_3_4.ready_to_move_out_src_tray():
                logger.info("Not able to move out since transplantor 3-4 not ready")
                time.sleep(2)
                continue  
            if not sower.ready_to_unload():
                logger.info("Not able to load since sower is not empty")
                time.sleep(2)
                continue 
            TransplantorToSower.create_job(id = 1, src =transplantor_3_4, dst=sower)
            time.sleep(2) 
        pass 

    @staticmethod 
    def create_job(id = -1, src = None, dst = None ): 
        if src == None or dst == None: 
            logger.info("Created job failed, sorce or destination is None")
            return None 
        job = TransplantorToSower(id = id)
        job.set_source(src)
        job.set_destination(dst)
        TransplantorToSower.transplantor_to_sower_jobs[id] = job 
        pass 

    def __init__(self, id = -1, type_name = 'Default'):
        self._source_buffer = None
        self._id = id 
        self._type_name = type_name
        self._destination_trans = None 
        pass

    def set_source(self, transplantor):
        if transplantor == None: 
            raise Exception("Source buffer can not be None")
        self._source_buffer = transplantor 
        pass 

    def set_destination(self, sower): 
        if sower == None: 
            raise Exception("Destination transplantor can not be None")

        self._destination_trans = sower
        pass

    def execute(self): 
        # 
        pass 
   
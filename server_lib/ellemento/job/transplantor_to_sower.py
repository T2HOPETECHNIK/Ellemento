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


class TransplantorToSower:
    transplantor_to_sower_jobs = {}   
    @staticmethod 
    def create_jobs():
        # create jobs for 
        transplantor_3_4 = TransplantorFactory.get_transplator_3_4() 
        sower = Sower.get_sower()
      
        TransplantorToSower.create_job(id = 1, src =transplantor_3_4, dst_tranplantor=sower)
        pass 

    @staticmethod 
    def create_job(id = -1, src = None, dst = None ): 
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
   
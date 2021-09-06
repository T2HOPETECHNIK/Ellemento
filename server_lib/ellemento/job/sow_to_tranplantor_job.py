# Interfacing with ASRS to execute transfer job
import threading
import time
from multiprocessing import Process
import os

from ellemento.model.tray import Tray
from ellemento.model.tray_phase_1_3 import TrayPhase13
from ellemento.model.tray_phase_4 import TrayPhase4
from ellemento.model.sower import Sower
from ellemento.model.transplantor_factory import TransplantorFactory


class SowerToTransplantor:
    @staticmethod 
    def create_job(): 
        sower  = Sower.create_sower()
        TransplantorFactory.
        pass 


    def __init__(self, id = -1, type_name = 'Default'):
        self._source  = None
        self._id = id 
        self._type_name = type_name
        self._destination = None 
        pass

    def set_source(self, sower):
        self._source = sower  
        pass 

    def set_destination(self, transplantor):
        self._destination = transplantor  
        pass

    def execute(self): 
        # 
        pass 
   
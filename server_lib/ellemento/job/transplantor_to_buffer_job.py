# Interfacing with ASRS to execute transfer job
from ellemento.model.tray import Tray
from ellemento.model.tray_phase_1_3 import TrayPhase13
from ellemento.model.tray_phase_4 import TrayPhase4
import threading
import time
from multiprocessing import Process
import os

class TransplantorToBufferJob:   
    def __init__(self, id = -1, type_name = 'Default'):
        self._source  = None
        self._id = id 
        self._type_name = type_name
        self._destination = None 
        pass

    def set_source(self, transplantor):
        self._source = transplantor  
        pass 

    def set_destination(self, buffer):
        self._destination = buffer  
        pass

    def execute(self): 
        # 
        pass 
   
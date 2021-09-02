# Interfacing with ASRS to execute transfer job
from ellemento.model.tray import Tray
from ellemento.model.tray_phase_1_3 import TrayPhase13
from ellemento.model.tray_phase_4 import TrayPhase4
import threading
import time
from multiprocessing import Process
import os

class BufferToTransplantorJob:  
    def __init__(self, id = -1, type_name = 'Default'):
        self._source_buffer = None
        self._id = id 
        self._type_name = type_name
        self._destination_trans = None 
        pass

    def set_source(self, buffer):
        self._source_buffer = buffer 
        pass 

    def set_destination(self, transplantor): 
        self._destination_trans = transplantor
        pass

    def execute(self): 
        # 
        pass 
   
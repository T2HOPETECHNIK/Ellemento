# Interfacing with ASRS to execute transfer job
from ellemento.model.tray import Tray
from ellemento.model.tray_phase_1_3 import TrayPhase13
from ellemento.model.tray_phase_4 import TrayPhase4
import threading
import time
from multiprocessing import Process
import os

class TransplantJob:
    @staticmethod
    def execute_transplant(source, destinations):
        #
        # To do, get a global value of tansplanting 
        #
        time.sleep(2)

        source_tray = TrayPhase13( source )
        source_tray.transplant_out()
        for tay_x in destinations:
            dest = TrayPhase4(tay_x)
            dest.transplant_in()
            tay_x = dest
            print(tay_x.has_veg)
    

        print('Transplanting', destinations)
    
    def __init__(self, id = -1, type_name = 'Default'):
        self._source_tray = None
        self._destination_trays = [] 
        self._transplantor = None 
        pass

    def set_tansplantor(self, transplantor): 
        self._transplantor =  transplantor

    def set_source_tray(self, tray):
        self._source_tray = tray 

    def set_destination_tray(self, trays): 
        self._destination_trays = trays 

    def transplant(self): 
        if self._source_tray == None:
            raise Exception("Source tray not specified")
        if len(self._destination_trays) == 0: 
            raise Exception("Destinations trays not specified")

        p = Process(target=TransplantJob.execute_transplant, args=(self._source_tray, self._destination_trays))
        p.start()
        p.join()
   
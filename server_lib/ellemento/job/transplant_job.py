import threading
import time
from multiprocessing import Process
import os
from ellemento.model import transplantor_factory

# Interfacing with ASRS to execute transfer job
from ellemento.model.tray import Tray
from ellemento.model.tray_phase_1_3 import TrayPhase13
from ellemento.model.tray_phase_4 import TrayPhase4
from ellemento.model.transplantor_factory import TransplantorFactory
from ellemento.model.transplantor import  Transplantor, TransplantorType


class TransplantJob:
    transplantor_job_list = {} 
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

    @staticmethod 
    def create_transplant_jobs(): 
        if len(TransplantJob.transplantor_job_list) == 0:
            TransplantJob.create_transplant_job(trans_type = TransplantorType.PHASE_3_4_TRANSPLANTOR)
            TransplantJob.create_transplant_job(trans_type = TransplantorType.PHASE_3_4_TRANSPLANTOR)
        return TransplantJob.transplantor_job_list

    @staticmethod 
    def create_transplant_job(trans_type = TransplantorType.PHASE_3_4_TRANSPLANTOR):
        transplantor_found = None  
        if trans_type == TransplantorType.PHASE_3_4_TRANSPLANTOR: 
            transplantor_found = TransplantorFactory.get_transplator_3_4()
            trans_job_1 = TransplantJob(id = 1)
            trans_job_1.set_tansplantor(transplantor_found) 
            TransplantJob.transplantor_job_list[1] = trans_job_1
        elif  trans_type == TransplantorType.PHASE_4_5_TRANSPLANTOR:
            transplantor_found = TransplantorFactory.get_transplator_4_5()
            trans_job_2 = TransplantJob(id = 2)
            trans_job_2.set_tansplantor(transplantor_found) 
            TransplantJob.transplantor_job_list[2] = trans_job_2
        if transplantor_found == None: 
            raise Exception("Invalid transplantor")
       

    
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
   
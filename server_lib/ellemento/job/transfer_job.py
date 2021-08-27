# Interfacing with ASRS to execute transfer job
from ellemento.model.tray_factory import TrayFactory
from ellemento.model.tray import Tray
from ellemento.model.tray import TrayStatus, TransferStatus
import threading
import time
from multiprocessing import Process
import os

import ellemento.model.tray 

class TransferJob:
    all_transfer_jobs = {}


    # check all trays in the 5 phases shelf to determine which ones needs to be transferred  
    @classmethod 
    def prepare_transfer_job_shelf(): 
        #      
        # check whether any transfer jobs
        #      
        def get_list_phase(status = TrayStatus.PHASE1, list_key = "phase1"):
            ret_list_phase = TrayFactory.check_duration(Tray.all_trays, status = status, duration = 3, unit='second')
            TransferJob.all_transfer_jobs[list_key] = TransferJob.all_transfer_jobs['phase1'] + ret_list_phase
            for obj in ret_list_phase: 
                Tray.all_trays[obj.id].TransferStatus = TransferStatus.TRANSFER_QUEUED

        get_list_phase(status = TrayStatus.PHASE1, list_key = "phase1")
        get_list_phase(status = TrayStatus.PHASE2, list_key = "phase2")
        get_list_phase(status = TrayStatus.PHASE3, list_key = "phase3")
        get_list_phase(status = TrayStatus.PHASE4, list_key = "phase4")
        get_list_phase(status = TrayStatus.PHASE5, list_key = "phase5")

    @staticmethod
    def execute_transfer(tray, source, destination):
        time.sleep(2)
        # Behavior of the transfer job 
        print('Transfering', tray)
    
    def __init__(self, id = -1, type_name = 'Default'):
        pass

    def set_tray(self, tray):
        self._tray = tray 

    def set_source(self, source): 
        self._destination = source

    def set_destination(self, destination): 
        self._destination = destination

    def transfer(self, tray, source, destination): 
        if (tray.location != source):
            raise Exception("Tray not in source location")
        
        p = Process(target=TransferJob.execute_transfer, args=(tray, source, destination,))
        p.start()
        p.join()
        tray.location = destination
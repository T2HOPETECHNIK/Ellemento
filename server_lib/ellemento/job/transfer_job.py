# Interfacing with ASRS to execute transfer job
from ellemento.model.tray import Tray
import threading
import time
from multiprocessing import Process
import os

class TransferJob:
    
    @classmethod 
    def prepare_transfer_job(): 
        



    @staticmethod
    def execute_transfer(tray, source, destination):
        time.sleep(2)
        # Behavor of the transfer job 
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
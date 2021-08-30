# Interfacing with ASRS to execute transfer job
from ellemento.model.shelf import Phase
from ellemento.model.tray_factory import TrayFactory
from ellemento.model.shelf_factory import ShelfFactory
from ellemento.model.tray import Tray
from ellemento.model.tray import TrayStatus, TransferStatus
import threading
import time
from multiprocessing import Process
import os
from lib.logging.logger_initialiser import EllementoLogger
import ellemento.model.tray 

logger = EllementoLogger.initialize_logger(); 

class TransferJob:
    all_transfer_jobs = {}


    # check all trays in the 5 phases shelf to determine which ones needs to be transferred  
    @classmethod 
    def prepare_transfer_job_shelf(): 
        #      
        # check whether the status of the tray in each phase is ready to schedule another transfer 
        #      
        def get_list_phase(status = TrayStatus.PHASE1, list_key = "phase1"):
            ret_list_phase = TrayFactory.check_duration(Tray.all_trays, status = status, duration = 3, unit='second')
            TransferJob.all_transfer_jobs[list_key] = TransferJob.all_transfer_jobs[list_key] + ret_list_phase
            for obj in ret_list_phase: 
                Tray.all_trays[obj.id].TransferStatus = TransferStatus.TRANSFER_QUEUED

        get_list_phase(status = TrayStatus.PHASE1, list_key = "phase1")
        get_list_phase(status = TrayStatus.PHASE2, list_key = "phase2")
        get_list_phase(status = TrayStatus.PHASE3, list_key = "phase3")
        get_list_phase(status = TrayStatus.PHASE4, list_key = "phase4")
        get_list_phase(status = TrayStatus.PHASE5, list_key = "phase5")

    @classmethod 
    def plan_destination_phase1():
        # Get phase 2 emptry shelvies 
        lst_shelf = ShelfFactory.get_empty_shelf_of_phase(phase = Phase.PHASE2)
        if len(lst_shelf) == 0: 
            logger.info("No free tray available phase 1")
            return 

        lst_jobs_phase1 = TransferJob.all_transfer_jobs['phase1']
        nIndex = 0; 
        while len(lst_shelf) != 0:
            shelf = lst_shelf.pop() 
            # choose 9 trays and put it inside the shelf 
            for i in range (0, ShelfFactory.tray_per_shelf): 
                TransferJob.all_transfer_jobs['phase1'][nIndex].set_destination(shelf)

    @classmethod 
    def plan_destination_phase1():
        # Get phase 2 emptry shelves 
        lst_shelf = ShelfFactory.get_empty_shelf_of_phase(phase = Phase.PHASE2)
        if len(lst_shelf) == 0: 
            logger.info("No free tray available phase 1")
            return 

        lst_jobs_phase1 = TransferJob.all_transfer_jobs['phase1']
        nIndex = 0; 
        while len(lst_shelf) != 0:
            shelf = lst_shelf.pop() 
            # choose 9 trays and put it inside the shelf 
            for i in range (0, ShelfFactory.tray_per_shelf): 
                TransferJob.all_transfer_jobs['phase1'][nIndex].set_destination(shelf)

    @classmethod 
    def plan_destination_phase2():
        # Get phase 2 emptry shelves 
        lst_shelf = ShelfFactory.get_empty_shelf_of_phase(phase = Phase.PHASE3)
        if len(lst_shelf) == 0: 
            logger.info("No free tray available phase 1")
            return 

        lst_jobs_phase1 = TransferJob.all_transfer_jobs['phase2']
        nIndex = 0; 
        while len(lst_shelf) != 0:
            shelf = lst_shelf.pop() 
            # choose 9 trays and put it inside the shelf 
            for i in range (0, ShelfFactory.tray_per_shelf): 
                TransferJob.all_transfer_jobs['phase2'][nIndex].set_destination(shelf)

    
    @classmethod 
    def plan_destination_phase3():
        # Only if the buffer still have places 
        #  3 in buffer 
        # 
        
        pass 

    @classmethod 
    def plan_destination_phase4(): 
        # only if the buffer still have places
        # 4 in buffer 
        pass 

    #call
    @classmethod 
    def plan_destination_phase5(): 
        # Harvester ..? 
        pass 







    


    @classmethod 
    def check_destination_available():
        # find the destination of the available shelves now 

        # For all phase 1 trays, need to find another phase 2 shelf which is empty 
        plan_destination_phase1()

        plan_destination_phase2()

        plan_destination_phase3() 

        plan_destination_phase4() 

        plan_destination_phase5() 

        pass 

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
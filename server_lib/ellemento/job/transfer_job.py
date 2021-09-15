# Interfacing with ASRS to execute transfer job
import time
from multiprocessing import Process
import os
import threading
from ellemento.model import bufffer_factory


from lib.logging.logger_initialiser import EllementoLogger
import ellemento.model.tray 
from ellemento.model.shelf import Phase, ShelfStatus
from ellemento.model.tray_factory import TrayFactory
from ellemento.model.shelf_factory import ShelfFactory
from ellemento.model.shelf import Shelf 
from ellemento.model.tray import Tray
from ellemento.model.tray import TrayStatus, TransferStatus
from ellemento.model.bufffer_factory import BufferFactory, BufferType
from ellemento.model.harvestor import Harvestor
from ellemento.model.sower import Sower 


logger = EllementoLogger.__call__().logger


class TransferJob:
    all_transfer_jobs = {}
    id_cur = 0
    terminate_job = False 

    # check all trays in the 5 phases shelf to determine which ones needs to be transferred  
    @staticmethod 
    def prepare_transfer_job_shelf(): 
        #      
        # check whether the status of the tray in each phase is ready to schedule another transfer 
        #      
        def get_list_phase(status = TrayStatus.PHASE1, list_key = Phase.PHASE1):
            ret_list_phase = TrayFactory.check_duration(Tray.all_trays, status = status, duration = 3, unit='second')
            TransferJob.all_transfer_jobs[list_key] = TransferJob.all_transfer_jobs[list_key] + ret_list_phase
            for obj in ret_list_phase: 
                Tray.all_trays[obj.id].TransferStatus = TransferStatus.TRANSFER_QUEUED

        get_list_phase(status = TrayStatus.PHASE1, list_key = Phase.PHASE1)
        get_list_phase(status = TrayStatus.PHASE2, list_key = Phase.PHASE2)
        get_list_phase(status = TrayStatus.PHASE3, list_key = Phase.PHASE3)
        get_list_phase(status = TrayStatus.PHASE4, list_key = Phase.PHASE4)
        get_list_phase(status = TrayStatus.PHASE5, list_key = Phase.PHASE5)

    # prepare job for sower to phase 1 shelf 
    @staticmethod 
    def plan_destination_phase1_in():
        def get_shelf_from_lst(lst_shelf_in): 
            shelf_ret = None 
            shelf = Shelf(lst_shelf_in[0])
            if shelf.status  == ShelfStatus.FULL: 
                lst_shelf_in.pop(0) 
            shelf_ret = Shelf(lst_shelf_in[0])
            return shelf_ret 
        try:
            while not TransferJob.terminate_job:  
                lst_shelf = ShelfFactory.get_empty_shelf_of_phase(phase = Phase.PHASE1)
                if len(lst_shelf) == 0: 
                    logger.info("Not any empty shelf avilable")
                    time.sleep(2)
                    continue 
                ret_shelf = get_shelf_from_lst(lst_shelf)
                sower_one = Sower(Sower.get_sower()) 
                if not sower_one.ready_to_unload(): 
                    time.sleep(2)
                    logger.info("Sower is not ready to unload - plants not ready")
                    continue 
                new_job = TransferJob()
                new_job.set_source(sower_one)
                new_job.set_destination(ret_shelf)
                time.sleep(2)
        except:
            logger.error("plan_destination_phase1_in gets error")
            return 
       
    @staticmethod 
    def plan_destination_phase1():
        # Get phase 2 empty shelves 
        try: 
            while not TransferJob.terminate_job: 
                lst_shelf = ShelfFactory.get_empty_shelf_of_phase(phase = Phase.PHASE2)
                if len(lst_shelf) == 0: 
                    logger.info("No free tray available phase 1")
                    time.sleep(2)
                    continue 

                lst_jobs_phase1 = TransferJob.all_transfer_jobs[Phase.PHASE1]
                nIndex = 0; 
                while len(lst_shelf) != 0:
                    shelf = lst_shelf.pop() 
                    # choose 9 trays and put it inside the shelf 
                    for i in range (0, ShelfFactory.tray_per_shelf): 
                        lst_jobs_phase1[nIndex].set_destination(shelf)
                    nIndex = nIndex + ShelfFactory.tray_per_shelf 
                time.sleep(2)
        except: 
            logger.error("Error occured in plan_destination_phase1")

    @staticmethod 
    def plan_destination_phase2():
        # Get phase 2 emptry shelves 
        try: 
            while not TransferJob.terminate_job: 
                lst_shelf = ShelfFactory.get_empty_shelf_of_phase(phase = Phase.PHASE3)
                if len(lst_shelf) == 0: 
                    logger.info("No free tray available phase 2")
                    time.sleep(2)
                    continue

                lst_jobs_phase2 = TransferJob.all_transfer_jobs[Phase.PHASE2]
                nIndex = 0; 
                while len(lst_shelf) != 0:
                    shelf = lst_shelf.pop() 
                    # choose 9 trays and put it inside the shelf 
                    for i in range (0, ShelfFactory.tray_per_shelf): 
                        lst_jobs_phase2[nIndex].set_destination(shelf)
                    nIndex = nIndex + ShelfFactory.tray_per_shelf 
                time.sleep(2)
        except: 
            logger.error("Exception in plan_destination_phase2")

    
    @staticmethod 
    def plan_destination_phase3():
        # Only if the buffer still have places 
        #  3 in buffer 
        # 
        try: 
            while not TransferJob.terminate_job: 
                if Phase.PHASE3 in TransferJob.all_transfer_jobs:
                    lst_jobs_phase3 = TransferJob.all_transfer_jobs[Phase.PHASE3]
                    buffer_3_in =  BufferFactory.get_buffer(BufferType.BUFFER_3_IN)
                    if buffer_3_in.has_tray(): 
                        for job in lst_jobs_phase3:
                            job.set_destination(buffer_3_in)
                    else:
                        logger.info("3-in buffer not having any trays")
                else: 
                    logger.info("Not having any phase 3 jobs")
                time.sleep(2)
        except: 
            logger.error("Get exception at plan_destination_phase3")
        # If buffer is available 

        pass 

    @staticmethod 
    def plan_destination_phase4_out(): 
        # only if the buffer still have places
        # 4 in buffer
        if Phase.PHASE4 in TransferJob.all_transfer_jobs:  
            lst_jobs_phase4 = TransferJob.all_transfer_jobs[Phase.PHASE4]
            buffer_4_in = BufferFactory.get_buffer(BufferType.BUFFER_4_IN)
            for job in lst_jobs_phase4:
                job.set_destination(buffer_4_in) 
        else: 
            logger.info("Not haveing any phase 4 transfer jobs")

    
    @staticmethod
    def plan_destination_phase4_in(): 
        def get_shelf_from_lst(lst_shelf_in): 
            shelf_ret = None 
            shelf = Shelf(lst_shelf_in[0])
            if shelf.status  == ShelfStatus.FULL: 
                lst_shelf_in.pop(0) 
            shelf_ret = Shelf(lst_shelf_in[0])
            return shelf_ret 
            
        # if buffer 4-out has something, then can plan transfer 
        buffer_4_out =  BufferFactory.get_buffer(BufferType.BUFFER_4_OUT)
        lst_shelf = ShelfFactory.get_empty_shelf_of_phase(phase = Phase.PHASE4)
        if not buffer_4_out.empty(): 
            new_job = TransferJob()
            new_job.set_source(buffer_4_out)
            shelf_dst = get_shelf_from_lst(lst_shelf)
            new_job.set_destination(shelf_dst)
            TransferJob.all_transfer_jobs[Phase.TRANSPLANT_2_PHASE4].append(new_job)


    @staticmethod
    def plan_destination_phase5_out(): 
        # only if the buffer still have places
        # if harvester is ready ..
        if Phase.PHASE5 in TransferJob.all_transfer_jobs:  
            lst_jobs_phase5  = TransferJob.all_transfer_jobs[Phase.PHASE5]
            harvestor = Harvestor.get_harvestor()
            for job in lst_jobs_phase5:
                job_transfer = TransferJob(job) 
                job_transfer.set_destination(harvestor)
        else: 
            logger.info("Not any phase 5 jobs availale")
        pass

    @staticmethod 
    def plan_destination_phase5_in(): 
        # only if the buffer still have places
        # 4 in buffer
        if Phase.PHASE5 in TransferJob.all_transfer_jobs:  
            lst_jobs_phase5 = TransferJob.all_transfer_jobs[Phase.PHASE5]
            harvestor = Harvestor.get_harvestor() 

            # destincaiton shall be harvester 
            for job in lst_jobs_phase5:
                job.set_destination(harvestor) 
        else: 
            logger.info("No any phase 5 transfer jobs")

    @classmethod 
    def check_destination_available():
        # find the destination of the available shelves now 

        # For all phase 1 trays, need to find another phase 2 shelf which is empty 
        #plan_destination_phase1()

        #plan_destination_phase2()

        #plan_destination_phase3() 

        #plan_destination_phase4() 

        #plan_destination_phase5() 

        pass 

    @staticmethod
    def execute_transfer(tray, source, destination):
        time.sleep(2)
        # Behavior of the transfer job 
        print('Transfering', tray)
    
    def __init__(self, id = -1, type_name = 'Default'):
        if id == -1: 
            TransferJob.id_cur =   TransferJob.id_cur + 1
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
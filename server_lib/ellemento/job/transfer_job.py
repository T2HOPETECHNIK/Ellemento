# Interfacing with ASRS to execute transfer job
from logging import log
from ellemento.job.transplant_job import TransplantJob
from ellemento.model.transplantor_factory import TransplantorFactory
import time
from multiprocessing import Process
import os
import threading

from ellemento.model import bufffer_factory, transplantor
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
from ellemento.model.buffer import Buffer 

logger = EllementoLogger.__call__().logger

class TransferJob:
    all_transfer_jobs = {}
    id_cur = 0
    terminate_job = False 

    # check all trays in the 5 phases shelf to determine which ones needs to be transferred  

    @staticmethod
    def get_list_full_grown_trays(status = TrayStatus.PHASE1):
        return TrayFactory.get_full_grown_trays(status= status)

    # @staticmethod 
    # def prepare_transfer_job_shelf(): 
    #     #      
    #     # check whether the status of the tray in each phase is ready to schedule another transfer 
    #     #      
    #     def get_list_phase(status = TrayStatus.PHASE1, list_key = Phase.PHASE1):
    #         try: 
    #             TransferJob.all_transfer_jobs[list_key] = TransferJob.all_transfer_jobs[list_key] + ret_list_phase
    #             for obj in ret_list_phase: 
    #                 Tray.all_trays[obj.id].TransferStatus = TransferStatus.TRANSFER_QUEUED
    #         except: 
    #             logger.error("prepare_transfer_job_shelf failed")
    #     try: 
    #         print("1")
    #         get_list_phase(status = TrayStatus.PHASE1, list_key = Phase.PHASE1)
    #         print("2")
    #         get_list_phase(status = TrayStatus.PHASE2, list_key = Phase.PHASE2)
    #         print("3")
    #         get_list_phase(status = TrayStatus.PHASE3, list_key = Phase.PHASE3)
    #         print("4")
    #         get_list_phase(status = TrayStatus.PHASE4, list_key = Phase.PHASE4)
    #         print("5")
    #         get_list_phase(status = TrayStatus.PHASE5, list_key = Phase.PHASE5)
    #         print("6")
    #     except: 
    #         logger.info("Error in prepare_transfer_job_shelf")

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
    def create_between_shelf_jobs(src_ls, dst_ls):
        nMin = min(len(src_ls), len(dst_ls))
        lst_jobs = [] 
        for idx in range(0, nMin): 
            src = src_ls[idx]
            src.set_transfer_status(TransferStatus.TRANSFER_QUEUED)
            dst = dst_ls[idx]
            dst.set_transfer_status(TransferStatus.TRANSFER_QUEUED) 
            new_job = TransferJob(source=src, destination=dst)
            lst_jobs.append[new_job]
        return lst_jobs 

    @staticmethod 
    def plan_phase2_move_out():
        # Get phase 2 empty shelves 
        try: 
            while not TransferJob.terminate_job: 
                shelf_phase_2 = ShelfFactory.phase2_shelf_to_transfer()
                nNumOfSrc = len(shelf_phase_2)
                if nNumOfSrc == 0: 
                    logger.info("Not any fully grown shelf to transfer")
                    time.sleep(2)
                    continue 
                else: 
                    logger.info("%d of fully grown phase 2 shelves", len(shelf_phase_2))

                lst_shelf = ShelfFactory.get_empty_shelf_of_phase(phase = Phase.PHASE3)
                nNumOfDst = len(lst_shelf)
                if nNumOfDst == 0: 
                    logger.info("No empty shelf available phase 3 -> Not able to move in")
                    time.sleep(2)
                    continue 
                else: 
                    logger.info("%d of empty phase 3 shelf found", len(lst_shelf))
                
                lst_jobs = TransferJob.create_between_shelf_jobs(shelf_phase_2, lst_shelf)             
                TransferJob.all_transfer_jobs[Phase.PHASE2] = TransferJob.all_transfer_jobs[Phase.PHASE2] + lst_jobs 
                time.sleep(2)
        except: 
            logger.error("Error occured in plan_destination_phase 2")

    @staticmethod 
    def plan_phase1_move_out():
        # Get phase 2 emptry shelves 
        try: 
            while not TransferJob.terminate_job: 
                shelf_phase_1 = ShelfFactory.phase1_shelf_to_transfer()
                if len(shelf_phase_1) == 0: 
                    logger.info("Not any shelf fully grown for phase 1")
                    time.sleep(2)
                    continue
                else:  
                    logger.info("%d numer of fully grown phase1 shelv found", len(shelf_phase_1))
              
                lst_shelf = ShelfFactory.get_empty_shelf_of_phase(phase = Phase.PHASE2)
                if len(lst_shelf) == 0: 
                    logger.info("No emptry shelf available phase 2 -> not able to move in")
                    time.sleep(2)
                    continue
       
                # add shelf to shelf transfer jobs in the jobs list 
                lst_jobs = TransferJob.create_between_shelf_jobs(shelf_phase_1, lst_shelf)       
                TransferJob.all_transfer_jobs[Phase.PHASE1] = TransferJob.all_transfer_jobs[Phase.PHASE1] + lst_jobs 
    
                time.sleep(2)
        except: 
            logger.error("Exception in plan_destination_phase 1")

    
    @staticmethod 
    def plan_phase3_move_out():
        # Only if the buffer still have places 
        #  3 in buffer 
        # 
        try: 
            while not TransferJob.terminate_job: 
                shelf_phase_3 = ShelfFactory.phase3_shelf_to_transfer()
                if len(shelf_phase_3) ==0:
                    logger.info("Not any fully grown phase 3 shelf") 
                    time.sleep(2)
                    continue
                else: 
                    logger.info("%d phase 3 shelves is fully grown", len(shelf_phase_3))
                
                buffer_3_in =  BufferFactory.get_buffer(BufferType.BUFFER_3_IN)
                if not buffer_3_in.empty(): 
                    logger.info("3-in buffer is not empty, not ready to load trays")
                    time.sleep(2)
                    continue
                
                logger.info("Create jobs")
                time.sleep(2)
                continue

                src = shelf_phase_3.pop() 
                new_job = TransferJob(source=src, destination=buffer_3_in) 
                lst_jobs = [] 
                lst_jobs.append(new_job)
                TransferJob.all_transfer_jobs[Phase.PHASE3] = TransferJob.all_transfer_jobs[Phase.PHASE3] + lst_jobs 
        except: 
            logger.error("Get exception at plan_destination_phase3")
        # If buffer is available 

        pass 

    @staticmethod 
    def plan_destination_phase4_out(): 
        # only if the buffer still have places
        # 4 in buffer
        while not TransferJob.terminate_job: 
            buffer_4_in = Buffer(BufferFactory.get_buffer(BufferType.BUFFER_4_IN))
            if buffer_4_in.full():
                logger.info("Destination buffer is full")
                time.sleep(2)
                continue 

            if Phase.PHASE4 in TransferJob.all_transfer_jobs:  
                lst_jobs_phase4 = TransferJob.all_transfer_jobs[Phase.PHASE4]
                for job in lst_jobs_phase4:
                    job.set_destination(buffer_4_in) 
            else: 
                logger.info("Not haveing any phase 4 transfer jobs")
            time.sleep(2)

    @staticmethod
    def plan_destination_phase4_in(): 
        def get_shelf_from_lst(lst_shelf_in): 
            shelf_ret = None 
            shelf = Shelf(lst_shelf_in[0])
            if shelf.status  == ShelfStatus.FULL: 
                lst_shelf_in.pop(0) 
            shelf_ret = Shelf(lst_shelf_in[0])
            return shelf_ret 

        while not TransferJob.terminate_job: 
            # if buffer 4-out has something, then can plan transfer 
            buffer_4_out = Buffer (BufferFactory.get_buffer(BufferType.BUFFER_4_OUT))
            lst_shelf = ShelfFactory.get_empty_shelf_of_phase(phase = Phase.PHASE4)
            if len(lst_shelf) == 0: 
                logger.info("Not any empty shelf in phase 4")
                time.sleep(2)
                continue 
            if not buffer_4_out.empty(): 
                new_job = TransferJob()
                new_job.set_source(buffer_4_out)
                shelf_dst = get_shelf_from_lst(lst_shelf)
                new_job.set_destination(shelf_dst)
                TransferJob.all_transfer_jobs[Phase.TRANSPLANT_2_PHASE4].append(new_job)
            else: 
                logger.info("Buffer 4 has no trays")
            time.sleep(2)

    @staticmethod
    def plan_destination_phase5_in(): 
        # only if the buffer still have places
        # if harvester is ready ..
        while not TransferJob.terminate_job: 
            transplantor_4_5 =  transplantor.Transplantor( TransplantorFactory.get_transplantor_4_5())
            lst_shelf = ShelfFactory.get_empty_shelf_of_phase(phase = Phase.PHASE5)
            if not transplantor_4_5.ready_to_move_out_dst_tray():
                logger.info("Transplantor is not ready")
                time.sleep(2)
                continue 
            
            shelf = lst_shelf.pop()
            if len(lst_shelf) == 0: 
                logger.info("Phase 5 shelf is not ready")
                time.sleep(2)
                continue 

            new_job = TransferJob()
            new_job.set_source(transplantor_4_5)
            new_job.set_destination(lst_shelf)
            TransferJob.all_transfer_jobs[Phase.TRANSPLANT_2_PHASE5].append(new_job)
            pass

    @staticmethod 
    def plan_destination_phase5_out(): 
        # only if the buffer still have places
        # 4 in buffer
        while not TransferJob.terminate_job: 
            if Phase.PHASE5 in TransferJob.all_transfer_jobs:  
                lst_jobs_phase5 = TransferJob.all_transfer_jobs[Phase.PHASE5]
                harvestor = Harvestor(Harvestor.get_harvestor()) 
                if not harvestor.ready_to_load(): 
                    logger.info("Harvestor is not ready")
                    time.sleep(2)
                    continue
                # destincaiton shall be harvester
                job = lst_jobs_phase5.pop(0)
                job.set_destination(harvestor) 
            else: 
                logger.info("No any phase 5 transfer jobs")
            time.sleep(2)

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
    
    def __init__(self, id = -1, type_name = 'Default', source = None, destination = None):
        if id == -1: 
            TransferJob.id_cur =   TransferJob.id_cur + 1
        self._source = source
        self._destination = destination
        pass

    def set_tray(self, tray):
        self._tray = tray 

    def set_source(self, source): 
        self._source = source

    def set_destination(self, destination): 
        self._destination = destination

    def transfer(self, tray, source, destination): 
        if (tray.location != source):
            raise Exception("Tray not in source location")
        
        p = Process(target=TransferJob.execute_transfer, args=(tray, source, destination,))
        p.start()
        p.join()
        tray.location = destination
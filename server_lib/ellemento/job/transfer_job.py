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
    job_queue = [] 


    # check all trays in the 5 phases shelf to determine which ones needs to be transferred  

    @staticmethod 
    def add_jobs(status = TrayStatus.PHASE1, lst_jobs = []):
        if status in TransferJob.all_transfer_jobs:
            TransferJob.all_transfer_jobs[status] = TransferJob.all_transfer_jobs[status] + lst_jobs
        else:
            TransferJob.all_transfer_jobs[status] = lst_jobs
        return TransferJob.all_transfer_jobs[status] 

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
                else: 
                    logger.info("%d of empty shelves are availble", len(lst_shelf))

                shelf_empty = get_shelf_from_lst(lst_shelf)
                shelf_empty.set_transfer_status(TransferStatus.TRANSFER_QUEUED)
                sower_one = Sower(Sower.get_sower()) 
                if not sower_one.ready_to_unload(): 
                    time.sleep(2)
                    logger.info("Sower is not ready to unload - plants not ready")
                    continue 
                if sower_one.transfer_planned: 
                    time.sleep(2)
                    logger.info("Sower is planned ")
                    continue
                sower_one.transfer_planned = True 
                new_job = TransferJob()
                new_job.set_source(sower_one)
                new_job.set_destination(shelf_empty)
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
                TransferJob.add_jobs(status = Phase.PHASE2, lst_jobs = lst_jobs)
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
                TransferJob.add_jobs(status = Phase.PHASE1, lst_jobs = lst_jobs)
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
                if buffer_3_in.booked_transfer: 
                    logger.info("3-in buffer is planned for transfer")
                    time.sleep(2)
                    continue

                buffer_3_in.booked_transfer = True
                shelf_grown = shelf_phase_3.pop()
                shelf_grown.set_transfer_status(TransferStatus.TRANSFER_QUEUED)
                new_job = TransferJob(source=shelf_grown, destination=buffer_3_in)
                lst_jobs = []
                lst_jobs.append(new_job)
                TransferJob.add_jobs(status = Phase.PHASE3, lst_jobs = lst_jobs)
                time.sleep(2)
                continue
        except: 
            logger.error("Get exception at plan_destination_phase3")
        # If buffer is available 

        pass 

    @staticmethod 
    def plan_phase4_move_out(): 
        # only if the buffer still have places
        # 4 in buffer
        while not TransferJob.terminate_job: 
            shelf_phase_4 = ShelfFactory.phase4_shelf_to_transfer()
            if len(shelf_phase_4) ==0:
                logger.info("Not any fully grown phase 4 shelf") 
                time.sleep(2)
                continue
            else: 
                logger.info("%d phase 4 shelves is fully grown", len(shelf_phase_4))

            buffer_4_in = BufferFactory.get_buffer(BufferType.BUFFER_4_IN)
            if not buffer_4_in.empty():
                logger.info("Destination buffer is full")
                time.sleep(2)
                continue 
            if buffer_4_in.booked_transfer: 
                logger.info("Buffer 4 in has booked for transfer")
                time.sleep(2)
                continue 

            buffer_4_in.booked_transfer = True
            shelf_grown = shelf_phase_4.pop()
            shelf_grown.set_transfer_status(TransferStatus.TRANSFER_QUEUED)
            new_job = TransferJob(source=shelf_grown, destination=buffer_4_in)
            lst_jobs = []
            lst_jobs.append(new_job)
            TransferJob.add_jobs(status = Phase.PHASE4, lst_jobs = lst_jobs)
            time.sleep(2)

    # from 4 out buffer 
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
            buffer_4_out = BufferFactory.get_buffer(BufferType.BUFFER_4_OUT)
            lst_shelf = ShelfFactory.get_empty_shelf_of_phase(phase = Phase.PHASE4)
            if len(lst_shelf) == 0: 
                logger.info("Not any empty shelf in phase 4")
                time.sleep(2)
                continue 
            else:
                logger.info("%d shelves is empty") 

            if buffer_4_out.empty(): 
                logger.info("Buffer 4 has no trays")
                time.sleep(2)
                continue
            if buffer_4_out.planned_transfer: 
                logger.info("buffer_4_out has planned transfer")
                time.sleep(2)
                continue

            buffer_4_out.planned_transfer = True 
            new_job = TransferJob()
            new_job.set_source(buffer_4_out)
            shelf_dst = get_shelf_from_lst(lst_shelf)
            new_job.set_destination(shelf_dst)
            TransferJob.all_transfer_jobs[Phase.TRANSPLANT_2_PHASE4].append(new_job)
    
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
            
            if transplantor_4_5.planned_transfer: 
                logger.info("Transplator 4-5 has planned for transfer")
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
            shelf_phase_5 = ShelfFactory.phase5_ready_to_transfer()
            if len(shelf_phase_5) == 0:
                logger.info("Not any fully grown phase 5 shelf") 
                time.sleep(2)
                continue
            else: 
                logger.info("%d phase 5 shelves is fully grown", len(shelf_phase_5))

            harvestor = Harvestor.get_harvestor()
            if not harvestor.ready_to_load():
                logger.info("Harvestor is not ready to load any trays") 
                time.sleep(2)
                continue
            
            if harvestor.planned_transfer: 
                logger.info("Transfer planned for the harvestor") 
                time.sleep(2)
                continue

            shelf_ready = shelf_phase_5.pop()
            shelf_ready.set_transfer_status(TransferStatus.TRANSFER_QUEUED)
            harvestor.planned_transfer = True 
            new_job = TransferJob()
            new_job.set_source(shelf_ready)
            new_job.set_destination(harvestor)
            lst_jobs = []
            lst_jobs.append(new_job)
            TransferJob.add_jobs(status = Phase.PHASE5, lst_jobs = lst_jobs)
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

    # Take transfer job one by one from job queue 
    @classmethod
    def execute_transfer(self):
        while not self.job_queue.count == 0:
            # pop front of the queue 
            job = self.job_queue.pop(0)
            job.transfer() 


        # Execute transfer ,, get source, get destination

        # update status .. 

    @classmethod
    def generate_job_queue(self):
        time.sleep(2)
        # Behavior of the transfer job 
        # Get the list of jobs,,
        print("All jobs", len(TransferJob.all_transfer_jobs))
        logger.info("Number of jobs %d", len(TransferJob.all_transfer_jobs))

        for key in TransferJob.all_transfer_jobs: 
          
            lst_jobs = TransferJob.all_transfer_jobs[key]
            print("Job type:", key, len(lst_jobs))
            if len(lst_jobs) == 0: 
                continue 
            while len(lst_jobs) > 0:
                job = lst_jobs[-1]
                print("Source:", job.source, type(job.source).__name__)
                print("Destination:", job.destination, type(job.destination).__name__)
                self.job_queue.append(job)

                #jobDone = job.transfer()
                #if jobDone: 
                #    lst_jobs.pop()
        # Execute transfer ,, get source, get destination
        pass    
    
    def __init__(self, id = -1, type_name = 'Default', source = None, destination = None):
        if id == -1: 
            TransferJob.id_cur =   TransferJob.id_cur + 1
        self._source = source
        self._destination = destination
        pass
    
    @property
    def source(self):
        return self._source

    @property 
    def destination(self):
        return self._destination 

    def set_tray(self, tray):
        self._tray = tray 

    def set_source(self, source): 
        self._source = source

    def set_destination(self, destination): 
        self._destination = destination
    

    def transfer(self):
        print(type(self).__name__)
        ret = False 
        if type(self._source).__name__ == 'Shelf' and type(self._destination).__name__ == 'Harvestor':
            print("............................................................")
            while self.source.status is not ShelfStatus.IDLE:
                tray = self._source.remove_tray() 
                if tray == None: 
                    logger.error("Harvesting of shelf is done")
                    # job is done time to remove it from the list 
                else: 
                    print(tray)
                    print(tray.id)
                    print("Unload a tray from shelf")
                    time.sleep(5)
                    print("Load a tray to harvestor")
                    self._destination.load_tray(tray)
                    tray.harvest()
                    print("Tay is harvested, hurray")
            ret = True 
        else: 
            time.sleep(5)
            print("Not yet implemented")
        return ret

    # def transfer(self): 
    #     if (tray.location != source):
    #         raise Exception("Tray not in source location")
        
    #     p = Process(target=TransferJob.execute_transfer)
    #     p.start()
    #     p.join()
    #     tray.location = destination
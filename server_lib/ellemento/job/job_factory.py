import threading
import time
from ellemento.job import transfer_job 

from ellemento.job.transfer_job import TransferJob
from ellemento.job.haverstor_to_buffer import HarvestorToBuffer 
from ellemento.job.transplant_job import TransplantJob
from ellemento.job.transplantor_to_buffer_job import TransplantorToBufferJob
from ellemento.job.buffer_to_transplantor_job import BufferToTransplantorJob 
from ellemento.job.transplantor_to_sower import TransplantorToSower

from lib.logging.logger_initialiser import EllementoLogger


logger = EllementoLogger.__call__().logger

class JobFactory:
    lst_all_trans_jobs = {}

    @staticmethod 
    def create_thead_jobs(): 
        # 1. xxx 
        transfer_job_1_in = threading.Thread(target=TransferJob.plan_destination_phase1_in)
        transfer_job_1_in.start()  
        transfer_job_phase_1 = threading.Thread(target = TransferJob.plan_destination_phase1)
        transfer_job_phase_1.start()
        transfer_job_phase_2 = threading.Thread(target = TransferJob.plan_destination_phase2)
        transfer_job_phase_2.start()
        transfer_job_phase_3 = threading.Thread(target = TransferJob.plan_destination_phase3)
        transfer_job_phase_3.start()

        buffer_to_transplantor_job = threading.Thread(target = BufferToTransplantorJob.create_jobs)
        buffer_to_transplantor_job.start() 

        transplant_jobs = threading.Thread(target = TransplantJob.create_transplant_jobs)
        transplant_jobs.start()

        # transplantor_to_sower_job = threading.Thread(target = TransplantorToSower.create_jobs)
        # transplantor_to_sower_job.start() 

    @staticmethod 
    def terminate_jobs(): 
         TransferJob.terminate_job = True
         BufferToTransplantorJob.terminate_job = True 
    
    @staticmethod
    def create_jobs_phase123(type_name = "Default", id = -1):
        #********************************************************
        #   *** Jobs for phase 1, 2, 3 loop 
        # create sower to phase1 jobs 
        # Create phase 1 -> phase 2 transfer jobs
        # create phase 2 -> phase 3 transfer jobs
        # create phase 3 -> 3 buffer jobs
        # create 3 buffer -> transplantor jobs
        # create transplating jobs 
        # create transplator to sower jobs 
        #*********************************************************
        # 1 Create transplantor jobs phase 1 
        # 1.1 from sower to phase 1 shelf 
        TransferJob.plan_destination_phase1_in() 
        # 1.2 from phase 1 shelf to phase 2 shelf  
        TransferJob.plan_destination_phase1()
        logger.info("TransferJob.plan_destination_phase1 is done")
        # 1.3 from phase 2 shelf to phase 3 shelf 
        TransferJob.plan_destination_phase2()
        logger.info("TransferJob.plan_destination_phase2 is done")
        # 1.4 from phase 3 shelf to buffer
        TransferJob.plan_destination_phase3()
        logger.info("TransferJob.plan_destination_phase3 is done")
        #2 create buffer to transplantor 
        BufferToTransplantorJob.create_jobs() 
        logger.info("Buffer to transplantor job is done")

        #3 create transplant jobs 
        TransplantJob.create_transplant_jobs()
        logger.info("Transplant jobs is done")

        #4 create transplantor to sower jobs 
        TransplantorToSower.create_jobs()

        logger.info("Transplantor to sower job is done")

        pass


    def create_jobs_phase4(): 
        #*********************************************************
        # *** Create jobs for phase 4 loop 
        # create tansplantor to 4 out buffer job 
        # create 4 out buffer to phase 4 shelf job 
        # create phase 4 shelf to 4 in buffer job 
        # create 4 in buffer to tansplantor job 
        # Transplanting job 
        # From tansplantor to 4 buffer 
        # From 4 buffer to transplantor 
        #*********************************************************
        #5 create jobs from transplantor to buffer 
        TransplantorToBufferJob.create_jobs()

        #6 from 4 out buffer to phase 4 shelf
        TransferJob.plan_destination_phase4_out() 
        
        #6 from phase 4 shelf to 4 in buffer 
        TransferJob.plan_destination_phase4_in() 
        
        pass


    def create_jobs_phase5(): 
        #*********************************************************
        # *** Create jobs for phase 5 loop 
        # create transfer job from transplator to phase 5 shelf job 
        # create phase 5 shelf to harvestor  
        # create 4 in buffer to tansplantor job 
        # Transplanting job 
        # From tansplantor to 5 buffer 
        # From 5 buffer to tansplantor 
        #*********************************************************
        TransferJob.plan_destination_phase5_in()
        
        TransferJob.plan_destination_phase5_out()

        HarvestorToBuffer.create_job() 
        
        pass 

    

    @staticmethod 
    def print():
        pass  
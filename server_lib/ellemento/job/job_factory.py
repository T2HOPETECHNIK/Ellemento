from ellemento.job.transfer_job import TransferJob
from ellemento.job.haverstor_to_buffer import HarvestorToBuffer 
from ellemento.job.transplant_job import TransplantJob
from ellemento.job.transplantor_to_buffer_job import TransplantorToBufferJob
from ellemento.job.buffer_to_transplantor_job import BufferToTransplantorJob 
from ellemento.job.sow_to_tranplantor_job import SowerToTransplantor


class JobFactory:
    lst_all_trans_jobs = {}
    
    @staticmethod
    def create_jobs_phase123(type_name = "Default", id = -1):
        #********************************************************
        #   *** Jobs for phase 1, 2, 3 loop 
        # create sower to phase1 jobs 
        # Create phase 1 -> phase 2 transfer jobs
        # create phase 2 -> phase 3 transfer jobs
        # create phase 3 -> 3 buffer jobs
        # create 3 buffer -> transplator jobs
        # create transplating jobs 
        # create transplator to sower jobs 
        #*********************************************************
        # 1 Create sower to transplantor jobs 

        

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
        pass 

    

    @staticmethod 
    def print():
        pass  
from datetime import date
import datetime
import time
from ellemento.job import job_factory 

from ellemento.model.farm_factory import FarmFactory
from ellemento.job import job_main
from ellemento.job import light_job
from ellemento.model.light_control import LightControl
from ellemento.job.transfer_job import TransferJob
from ellemento.model.tray_factory import Tray 
from ellemento.job.test1 import Foo
from ellemento.model.bufffer_factory import BufferFactory
from ellemento.job.job_factory import JobFactory 



if __name__ == '__main__':
    try:
        today = date.today()
        now = datetime.datetime.now()
        print("Today's date:", now)
        FarmFactory.create_farm()
        print("-------------------------------------------")
        BufferFactory.create_all_buffers()
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        JobFactory.create_thead_jobs()
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        JobFactory.grow_plants_jobs() 
        print("###########################################")
        JobFactory.execute_jobs()
        while True: 
            time.sleep(2); 
    except KeyboardInterrupt:
        JobFactory.terminate_jobs()
        print("Bye bye ellemento")
        
    #JobFactory.create_jobs_phase123()
    #JobFactory.create_jobs_phase4()
    #JobFactory.create_jobs_phase5()
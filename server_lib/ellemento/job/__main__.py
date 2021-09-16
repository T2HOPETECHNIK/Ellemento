from datetime import date
import datetime
import time 

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
    #job_main.r
    # print("...........................")
    # #light_job.on_lights()
    # print("xxx")
    # #LightControl.print()
    # tr_job = TransferJob()
    # tray = Tray(id = 1, type_name= "Phase1-3")
    # tray.location = "sower"
    # print("Tansfer job")
    # tr_job.transfer(tray, "sower", "shelf_10")  
    # print(tray.location)
    try:
        today = date.today()
        now = datetime.datetime.now()
        print("Today's date:", now)
        FarmFactory.create_farm()
        BufferFactory.create_all_buffers()
        JobFactory.create_thead_jobs()
        JobFactory.grow_plants_jobs() 
        while True: 
            time.sleep(10); 
            print("... waiting")
    except KeyboardInterrupt:
        JobFactory.terminate_jobs()
        print("Bye bye ellemento")
        
    #JobFactory.create_jobs_phase123()
    #JobFactory.create_jobs_phase4()
    #JobFactory.create_jobs_phase5()
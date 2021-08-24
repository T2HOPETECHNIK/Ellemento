from ellemento.job import job_main
from ellemento.job import light_job
from ellemento.model.light_control import LightControl
from ellemento.job.transfer_job import TransferJob
from ellemento.model.tray_factory import Tray 

if __name__ == '__main__':
    #job_main.r
    print("...........................")
    #light_job.on_lights()
    print("xxx")
    #LightControl.print()
    tr_job = TransferJob()
    tray = Tray(id = 1, type_name= "Phase1-3")
    tray.location = "sower"
    print("Tansfer job")
    tr_job.transfer(tray, "sower", "shelf_10")  
    print(tray.location)
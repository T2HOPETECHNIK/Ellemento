from ellemento.job import job_main
from ellemento.job import light_job
from ellemento.model.light_control import LightControl

if __name__ == '__main__':
    #job_main.r
    print("...........................")
    light_job.on_lights()
    print("xxx")
    LightControl.print()
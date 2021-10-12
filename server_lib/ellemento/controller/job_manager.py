
import threading
import logging
import time
from queue import Queue

class JobManager:

    job_number = 0
    job_thread = 0
    
    
    def __init__(self, jobnumber, jobtype, params):
        self.job_number = jobnumber
        self.jobtype = jobtype
        self.q = Queue()

        self.setup(self.job_number, self.jobtype, params)

    def __del__(self):
        self.cleanup()

    def cleanup(self):
        print("Job:",self.job_number," done")

    def setup(self, jobnumber, jobtype, job_params):
        print("Setup:", jobnumber)
        self.job_thread = jobThread.CJobThread(jobnumber, "jobaction", jobtype, job_params, self.q)
        self.job_thread.start()


    def isJobDone(self):
        if self.job_thread.isRunning():
            return False
        else:
            return True

    def waitForJobDone(self):
        while self.job_thread.isRunning():
            time.sleep(constants.STATUS_CHECK_INTERVAL_SEC)

    def getRunningTask(self):
        return self.q.get()     #self.job_object.running_task




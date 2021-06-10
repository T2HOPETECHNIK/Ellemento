
import threading
import logging
import jobThread
import time
import constants

class JobManager:

    job_thread = 0
    jobnumber = 0;

    
    def __init__(self, jobnumber, jobtype):
        self.jobnumber = jobnumber
        self.setup(self.jobnumber, jobtype)

    def __del__(self):
        self.cleanup()

    def cleanup(self):
        print("Job:",self.jobnumber," done")

    def setup(self, jobnumber, jobtype):
        print("Setup:", jobnumber)
        self.job_thread = jobThread.CJobThread(jobnumber, "jobaction", jobtype)
        self.job_thread.start()


    def isJobDone(self):
        if self.job_thread.isRunning():
            return False
        else:
            return True

    def waitForJobDone(self):
        while self.job_thread.isRunning():
            time.sleep(constants.STATUS_CHECK_INTERVAL_SEC)





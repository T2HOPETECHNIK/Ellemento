
import logging
import constants
import job_manager

if __name__ == "__main__":
    print("Started")

    # Example usage
    x = job_manager.JobManager(1, constants.JOB_PHASE_1_1)
    y = job_manager.JobManager(2, constants.JOB_PHASE_1_2)
    z = job_manager.JobManager(3, constants.JOB_TRANSPLANT_1)

    AllDone = False
    while (AllDone == False):
        AllDone = True
        if (x.isJobDone() == False):
            AllDone = False
        if (y.isJobDone() == False):
            AllDone = False
        if (z.isJobDone() == False):
            AllDone = False

    print("All done")
    
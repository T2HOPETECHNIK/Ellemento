import threading
import constants
import time
import logging
import task

class CJobThread (threading.Thread):

    logging.basicConfig(level = logging.INFO)


    def __init__(self, threadID, name, jobtype, job_params, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.jobtype = jobtype
        self.job_params = job_params
        self.q = q

        self.gRunning = True
        

    # Run timer loop that triggers the update status
    def run(self):
        print("Job name:", self.name, " jobtype: ", self.jobtype)    #jobtype
        
        self.seq = self.getSequence(self.jobtype)

        filteredSeq = self.filterSequence(self.seq)

        opResult = True

        for op in filteredSeq:
            print("Task to perform: ", op)

            # update status with op
            self.q.put(op)

            opResult = False

            if self.checkPreCondition(op) == False:
                print("Precondition failed")
                break

            res = self.perform(op, self.job_params)
            if res == False:
                print("Operation failed")
                break

            if self.checkPostCondition(op) == False:
                print("Post condition failed")
                break
            
            opResult = True

            # Clear running task
            self.q.put("")

            print("Task: ", op, " Done Okay")


        self.unsetFlag()
        print("<< run. ", self.jobtype, " complete")


    # This function gets the action from DB
    def getSequence(self, jobtype):
        print(">> Get sequence of action from DB")

        #==============================
        # *** TO DO ***
        # Read from DB state_workflow
        #==============================

        # simulate sequence read from DB
        if jobtype == constants.JOB_PHASE_1_1:
            return ["sower_to_1_rack_move","1_rack_to_2_rack_move","2_rack_to_3_rack_move","3_rack_to_3_4_move","3_in_buffer"]
        elif jobtype == constants.JOB_PHASE_1_2:
            return ["transplanter_to_washer", "wash_tray", "washer_to_sower", "foam_inserter"]
        elif jobtype == constants.JOB_TRANSPLANT_1:
            return ["transplant_3_to_4"]
        elif jobtype == constants.JOB_PLANTING:
            return ["water_on","light_on"]
        else:
            return ["quit"]


    # Counter check with DB where in the sequence we previously left-off (eg. from last interruption)
    # For new operation, the sequence is returned as is.
    def filterSequence(self, sequence):
        #
        # TO DO: Filter out the part of the sequence that has already been performed
        #

        #===============================
        # simulate actual filtering
        newlist = []
        for op in sequence:
            if op != "donothing":
                newlist.append(op)
        #===============================

        return newlist


    def checkPreCondition(self, op):
        #
        # TO DO: add more checks
        #
        print("Precondition check")
        return True


    def checkPostCondition(self, op):
        #
        # TO DO: add more checks
        #
        print("Postcondition check")
        return True


    # Perform specific operation
    def perform(self, op, params):
        #
        # TO DO: Perform the actual action
        #
        #print("Thread ID:", self.threadID, " Operation:",op)

        itask = task.CTask()
        result = itask.performTask(op, params)
        
        # return status of job
        return result

    def setFlag(self):
        self.gRunning = True

    def unsetFlag(self):
        self.gRunning = False

    def isRunning(self):
        return self.gRunning




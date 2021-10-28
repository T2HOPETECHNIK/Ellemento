#!/bin/bash

#from ellemento_rack import ellemento_rack
import tkinter as tk
import config

from Application import Application

import threading
import time


'''
def test():
    elem1 = ellemento_rack("192.168.1.5")
    
    elem1.toggleLED(1,True)
    elem1.setLEDIntensity(1, 50)
    
    elem1.togglePV(1, False)



if __name__ == "__main__":
    test()
    
'''



class StatusThread (threading.Thread):

    def __init__(self, threadID, name, ui_app):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.ui_interface = ui_app
        self.gRunning = True

    # Run timer loop that triggers the update status
    def run(self):
        print("Status thread running")
        interval = config.UPDATE_INTERVAL_SEC
        while(self.gRunning):
            self.ui_interface.updatePumpStatus()
            self.ui_interface.updateValveStatus()
            self.ui_interface.updateLEDStatus()
            time.sleep(interval)

        print("Terminate status thread")


    def setFlag(self):
        self.gRunning = True

    def unsetFlag(self):
        self.gRunning = False


if __name__ == "__main__":

    print("App started")
    
    root = tk.Tk()
    app = Application(master=root)

    status_thread = StatusThread(1, "TStatus", app)
    status_thread.start()

    app.mainloop()

    status_thread.unsetFlag()
    print("Terminate main thread")

    

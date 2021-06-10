
import time
import constants

class CTask:

    def performTask(self, task):

        print("Task:",task)
        
        if task == constants.task_names[0]:
            self.sower_to_rack_1_move()
        elif task == constants.task_names[1]:
            self.rack_1_to_rack_2_move()
        elif task == constants.task_names[2]:
            self.rack_2_to_rack_3_move()
        elif task == constants.task_names[3]:
            self.rack_3_to_3_4_move()
        elif task == constants.task_names[4]:
            self.transplant_3_to_4()
        elif task == constants.task_names[5]:
            self.buffer_3_in()
        elif task == constants.task_names[6]:
            self.wash_3_tray()
        elif task == constants.task_names[7]:
            self.washer_to_sower()
        elif task == constants.task_names[8]:
            self.foam_inserter()
        elif task == constants.task_names[9]:
            self.buffer_4_out()
        elif task == constants.task_names[10]:
            self.rack_3_4_to_4_move()
        elif task == constants.task_names[11]:
            self.rack_4_to_4_5_move()
        elif task == constants.task_names[12]:
            self.buffer_4_in()
        elif task == constants.task_names[13]:
            self.transplant_4_to_5()
        elif task == constants.task_names[14]:
            self.wash_tray_4()
        elif task == constants.task_names[15]:
            self.lifter_4_to_tray()
        elif task == constants.task_names[16]:
            self.potting()
        elif task == constants.task_names[17]:
            self.lift_tray_pot()
        elif task == constants.task_names[18]:
            self.buffer_4()
        elif task == constants.task_names[19]:
            self.rack_4_5_to_5_move()
        elif task == constants.task_names[20]:
            self.rack_to_harvester_move()
        elif task == constants.task_names[21]:
            self.harvester()
        elif task == constants.task_names[22]:
            self.wash_tray_5()
        elif task == constants.task_names[23]:
            self.washer_to_lifter()
        elif task == constants.task_names[24]:
            self.buffer_5()
        elif task == constants.task_names[25]:
            self.wash_to_pot()
        else:
            time.sleep(10)

        # Call PLC to do something
        return True
        
        
    def sower_to_rack_1_move(self):
        time.sleep(5)

    def rack_1_to_rack_2_move(self):
        time.sleep(5)

    def rack_2_to_rack_3_move(self):
        time.sleep(5)

    def rack_3_to_3_4_move(self):
        time.sleep(5)

    def buffer_3_in(self):
        time.sleep(5)

    def transplant_3_to_4(self):
        time.sleep(5)

    def wash_3_tray(self):
        time.sleep(3)

    def washer_to_sower(self):
        time.sleep(5)

    def foam_inserter(self):
        time.sleep(5)

    def buffer_4_out(self):
        time.sleep(5)    

    def rack_3_4_to_4_move(self):
        time.sleep(5)

    def rack_4_to_4_5_move(self):
        time.sleep(5)

    def buffer_4_in(self):
        time.sleep(5)

    def transplant_4_to_5(self):
        time.sleep(5)

    def wash_tray_4(self):
        time.sleep(5)

    def lifter_4_to_tray(self):
        time.sleep(5)

    def potting(self):
        time.sleep(5)

    def lift_tray_pot(self):
        time.sleep(5)
    
    def buffer_4(self):
        time.sleep(5)

    def rack_4_5_to_5_move(self):
        time.sleep(5)

    def rack_to_harvester_move(self):
        time.sleep(5)

    def harvester(self):
        time.sleep(5)

    def wash_tray_5(self):
        time.sleep(5)

    def washer_to_lifter(self):
        time.sleep(5)

    def buffer_5(self):
        time.sleep(5)

    def wash_to_pot(self):
        time.sleep(5)



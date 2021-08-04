
import time
# Import PLC library
import sys

sys.path.append('../plc')
import ellemento.plc.modbus_io as modbus

from ellemento.job import constants
from ellemento.job import rest_api 


class CTask:

    def performTask(self, task, params):

        print("Task: ", task, " Params: ", params)
        
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
        elif task == constants.task_names[40]:      # Shelf control
            self.water_on(params)
        elif task == constants.task_names[41]:      
            self.water_off(params)
        elif task == constants.task_names[42]:      
            self.light_on(params)
        elif task == constants.task_names[42]:      
            self.light_off(params)
        else:
            time.sleep(10)

        # Call PLC to do something
        return True


    def errorCheck(self, errCode):
        print ("Error:", errCode)
    

    # =====================================================
    #  Task actions: Shelf operation
    # =====================================================

    def getRackIP(self, rackno):
        return constants.RACK_IP[rackno + 1]


    def water_on(self, params):

        if (constants.NO_MODBUS):
            return constants.ERROR_NONE

        mb_S = modbus.plc()
        mb_S.setIP(self.getRackIP(params[0]))

        first = True
        for shelf in params:

            if first == True:
                first = False
                continue

            bres = mb_S.write_coil(constants.ADDR_WATER_ON + (shelf * 9), 1, True)
            if (bres == False):
                return constants.ERROR_MODBUS_WRITE_COIL

        time.sleep(5)

        return True


    def water_off(self, params):
        if (constants.NO_MODBUS):
            return constants.ERROR_NONE

        mb_S = modbus.plc()
        mb_S.setIP(self.getRackIP(params[0]))

        first = True
        for shelf in params:
            
            if first == True:
                first = False
                continue

            bres = mb_S.write_coil(constants.ADDR_WATER_ON + (shelf * 9), 0, True)
            if (bres == False):
                return constants.ERROR_MODBUS_WRITE_COIL

        time.sleep(5)

        return True
        

    def light_on(self, params):
        if (constants.NO_MODBUS):
            return constants.ERROR_NONE

        mb_S = modbus.plc()
        mb_S.setIP(self.getRackIP(params[0]))


        first = True
        for shelf in params:
            
            if first == True:
                first = False
                continue

            bres = mb_S.write_coil(constants.ADDR_LIGHT_ON + (shelf * 9), 1, True)
            if (bres == False):
                return constants.ERROR_MODBUS_WRITE_COIL

        time.sleep(5)

        return True


    def light_off(self, params):
        if (constants.NO_MODBUS):
            return constants.ERROR_NONE

        mb_S = modbus.plc()
        mb_S.setIP(self.getRackIP(params[0]))


        first = True
        for shelf in params:
            
            if first == True:
                first = False
                continue

            bres = mb_S.write_coil(constants.ADDR_LIGHT_ON + (shelf * 9), 0, True)
            if (bres == False):
                return constants.ERROR_MODBUS_WRITE_COIL

        time.sleep(5)

        return True

    # =====================================================
    # Task actions: Tray Movement
    # =====================================================

    def is_mover_done(self):
        # To do: Check mover task completion
        return True


    def wait_for_mover_done(self, timeout_s):

        time_cnt = timeout_s

        while ((self.is_mover_done() == False) and (time_cnt > 0)):
            time.sleep(1)
            time_cnt = time_cnt - 1

        if time_cnt == 0:
            return False
        else:
            return True


    def generic_mover(self, source_location, destination_location):
        print(">> generic mover")

        if (constants.NO_MODBUS):
            return constants.ERROR_NONE

        # Connect to modbus
        mb_RC = modbus.plc()
        mb_RC.setIP(constants.ROBOT_IP)

        mb_MB = modbus.plc()
        mb_MB.setIP(constants.MEGABOT_IP)

        # TO DO: Read from Megabot check whether it's ready to do stuffs

        bres = mb_RC.read_coil(constants.ADDR_RC_L4_READY_TO_RELEASE, 0)
        if (bres == False):
            return constants.ERROR_MODBUS_READ_COIL

        bres = mb_RC.write_coil(constants.ADDR_RC_L4_READY_TO_COLLECT, 0, True)
        if (bres == False):
            return constants.ERROR_MODBUS_WRITE_COIL

        # TO DO: Update DB or logs to indicate that action is requested
        # TO DO: Ask Megabot to collect tray

        # Wait for megabot until task is done or error
        if (self.wait_for_mover_done(constants.MOVE_TIMEOUT_S) == False):
            return constants.ERROR_TIMEOUT

        # TO DO: Update DB or logs to indicate that Megabot action is completed

        bres = mb_RC.read_coil(constants.ADDR_RC_TRAY_RECEIVE, 0)
        if (bres == False):
            return constants.ERROR_MODBUS_READ_COIL

        mb_RC.write_coil(constants.ADDR_RC_TRAY_COLLECTED, True)

        return constants.ERROR_NONE


    #============================================
    # Individual functions
    #============================================

    def sower_to_rack_1_move(self):

        print (">> sower_to_rack_1_move")

        self.generic_mover(constants.LOCATION_SOWER, constants.LOCATION_RACK1)
        
        # Insert entry in history 
        # Insert entry in Tray_Movement table

        # Get tray id, source id, and destination id
        tray_id = 0
        source = 0
        destination = 0
        
        resp = rest_api.add_to_tray_moving(tray_id, source, destination)
        self.errorCheck(resp)
        time.sleep(5)


    def rack_1_to_rack_2_move(self):

        print(">> rack_1_to_rack_2_move")

        self.generic_mover(constants.LOCATION_RACK1, constants.LOCATION_RACK2)

        # Insert entry in history 
        # Insert entry in Tray_Movement table

        time.sleep(5)

    def rack_2_to_rack_3_move(self):

        print(">> rack_2_to_rack_3_move")

        self.generic_mover(constants.LOCATION_RACK2, constants.LOCATION_RACK3)

        # Insert entry in history 
        # Insert entry in Tray_Movement table
        time.sleep(5)


    def rack_3_to_3_4_move(self):
        print(">> rack_3_to_3_4_move")
        # TO DO

        time.sleep(5)


    def buffer_3_in(self):
        print(">> buffer_3_in")
        # TO DO

        time.sleep(5)

    def transplant_3_to_4(self):
        print(">> transplant_3_to_4")
        # TO DO

        time.sleep(5)

    def wash_3_tray(self):
        print(">> wash_3_tray")
        # TO DO
        time.sleep(3)

    def washer_to_sower(self):
        print(">> washer_to_sower")
        # TO DO

        time.sleep(5)

    def foam_inserter(self):
        print(">> foam_inserter")
        # TO DO

        time.sleep(5)

    def buffer_4_out(self):
        print(">> buffer_4_out")
        # TO DO

        time.sleep(5)    

    def rack_3_4_to_4_move(self):
        print(">> rack_3_4_to_4_move")
        # TO DO

        time.sleep(5)

    def rack_4_to_4_5_move(self):
        print(">> rack_4_to_4_5_move")
        # TO DO

        time.sleep(5)

    def buffer_4_in(self):
        print(">> buffer_4_in")
        # TO DO

        time.sleep(5)

    def transplant_4_to_5(self):
        print(">> transplant_4_to_5")
        # TO DO

        time.sleep(5)

    def wash_tray_4(self):
        print(">> wash_tray_4")
        # TO DO

        time.sleep(5)

    def lifter_4_to_tray(self):
        print(">> lifter_4_to_tray")
        # TO DO

        time.sleep(5)

    def potting(self):
        print(">> potting")
        # TO DO

        time.sleep(5)

    def lift_tray_pot(self):
        print(">> lift_tray_pot")
        # TO DO

        time.sleep(5)
    
    def buffer_4(self):
        print(">> buffer_4")
        # TO DO

        time.sleep(5)

    def rack_4_5_to_5_move(self):
        print(">> rack_4_5_to_5_move")
        # TO DO

        time.sleep(5)

    def rack_to_harvester_move(self):
        print(">> rack_to_harvester_move")
        # TO DO

        time.sleep(5)

    def harvester(self):
        print(">> harvester")
        # TO DO

        time.sleep(5)

    def wash_tray_5(self):
        print(">> wash_tray_5")
        # TO DO

        time.sleep(5)

    def washer_to_lifter(self):
        print(">> washer_to_lifter")
        # TO DO

        time.sleep(5)

    def buffer_5(self):
        print(">> buffer_5")
        # TO DO

        time.sleep(5)

    def wash_to_pot(self):
        print(">> wash_to_pot")
        # TO DO

        time.sleep(5)


    # =================================
    # Shelf controls

    def water_on(self, params):
        print(">> water_on")
        # TO DO
        time.sleep(5)

    def water_off(self, params):
        print(">> water_off")
        # TO DO
        time.sleep(5)

    def light_on(self, params):
        print(">> light on")
        # TO DO
        time.sleep(5)

    def light_off(self, params):
        print(">> light off")
        # TO DO
        time.sleep(5)

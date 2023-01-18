
'''
This class will handle the rack: shelf lighting, water, pump, etc.

'''

from logging import error
import address
import utils
import modbus_io
import constants as const

class ellemento_rack(object):

    plc = modbus_io.plc()
    
    def __init__ (self, ip):
        super().__init__()
        self.plc.setIP(ip)
        print ("Ellemento rack client connected")


    def __del__(self):
        print ("Ellemento rack client disconnected")
        #self.client.close()

    '''
    def test(self):
        print ("Odin will cast his lightning bolts upon you.")
        res,err = self.plc.write_register(1000, 1234)   #.write_registers(1000, 1512, unit=1)
        res,err = self.plc.write_register(2000, 888)
        res,err = self.plc.read_register(1000, 1)
        res,err = self.plc.write_coil(5000,1, True)
        data,err = self.plc.read_coil(5000,6)

        if data == True:
            print ("Result: True")
        else:
            print ("Result: False")

    def test2(self):
        print ("Change mode")

        self.changeMode(const.AUTO_MODE)
        self.toggleLED(2,True)
        self.setLEDIntensity(2, 22)
        self.togglePV(1,True)
        self.setShelfPVPosition(1,50)
        self.setPumpMode(1,const.PUMP_FLOW_MODE)
        self.setPumpRPM(1, 100)
        self.setPumpFlowRate(1, 20)
        self.setPumpFlowRatePerShelf(1,23)
        ps = self.getPumpRPMsetting(1)
        print ("Pump setting:",ps)

    '''


    def test_mb(self):
        res,err = self.plc.write_register(4080, 88)
        self.plc.write_coil(4081,0,True)

    
    #===============================================================

    def apply(self):
        applyAddr = address.CTRL_APPLY_UPDATE_ADDR
        res,err = self.plc.write_coil(applyAddr, address.CTRL_APPLY_UPDATE_BITPOS, True)


    def getRackType(self):
        addr = address.REF_RACK_TYPE
        res,err = self.plc.read_register(addr, 1)
        return res, err


    #===============================================================
    #  Section
    #===============================================================

    def changeSectionMode(self, section, mode):
        modeAddress = address.CTRL_SECTION_MODE_ADDR + (section - 1)
        res,err = self.plc.write_register(modeAddress, mode)


    def getSectionMode(self, secno):
        if secno==1:
            addr = address.FEEDBACK_SECTION1_MODE
        else:
            addr = address.FEEDBACK_SECTION2_MODE
        res,err = self.plc.read_register(addr, 1)
        if err > 0:
            return 0,err
        else:
            return res.registers[0], err


    #================================================================
    # Lighting
    #================================================================

    def toggleLED(self, ledNum, bOnOff):
        ledOnAddress = address.CTRL_LIGHT_ON_ADDR   # + (ledNum - 1)
        res,err = self.plc.write_coil(ledOnAddress, address.CTRL_LIGHT_ON_BITPOS + (ledNum-1), bOnOff)

    def setLEDIntensity(self, ledNum, intensity):
        ledIntensityAddress = address.CTRL_LIGHT_INTENSITY_OFFSET_ADDR + (ledNum - 1)
        res,err = self.plc.write_register(ledIntensityAddress, intensity)

    def getLEDSetting(self, lednum):
        res,err = self.plc.read_register(address.FEEDBACK_LED_INTENSITY_ADDR + (lednum - 1), 1)
        if err > 0:
            return 0,err
        else:
            return res.registers[0], err

    #================================================================
    # PV 
    #================================================================

    def togglePV(self, pvNum, bOnOff):
        pvOnAddress = address.CTRL_PV_ON_ADDR
        res,err = self.plc.write_coil(pvOnAddress, address.CTRL_PV_ON_BITPOS + (pvNum - 1), bOnOff)

    # Position is 0-100, PV starts at 1
    def setShelfPVPosition(self, pvNum, pvPos):
        pvPosAddress = address.CTRL_PV_VALUE_OFFSET_ADDR + (pvNum - 1)
        res,err = self.plc.write_register(pvPosAddress,pvPos)

    def getPVSetting(self, PVnum):
        res,err = self.plc.read_register(address.FEEDBACK_PV_OFFSET_ADDR + (PVnum - 1), 1)
        if err > 0:
            return 0,err
        else:
            return res.registers[0], err

    '''
    def setShelfPVLUTPosition(self, pvNum, pvPos):
        pvPosAddress = address.SHELF_PV_LUT_ADDRESS[pvNum]
        res,err = self.plc.write_register(pvPosAddress,pvPos)
    '''

    #================================================================
    # Pump
    #================================================================


    
    def togglePump(self, pumpNum, bOnOff):
        pumpOnAddress = address.CTRL_PUMP_ON_ADDR
        res,err = self.plc.write_coil(pumpOnAddress, address.CTRL_PUMP_ON_BITPOS + (pumpNum - 1), bOnOff)


    # set pump mode: auto, manual flowrate, manual RPM
    def setPumpMode(self, pumpNo, mode):
        
        addr = address.CTRL_PUMP_MODE_ADDR + (pumpNo - 1)
        
        res,err = self.plc.write_register(addr, mode)
        if err != 0:
            return False
        else:
            return True


    # set pump RPM
    def setPumpRPM(self, pumpNo, RPM):
        
        addr = address.CTRL_PUMP_RPM_SETPOINT_ADDR + (pumpNo - 1)

        res,err = self.plc.write_register(addr, RPM)
        if err != 0:
            return False
        else:
            return True


    def setPumpFlowrate(self, pumpNo, flowrate):
        
        addr = address.CTRL_PUMP_FLOWRATE_SETPOINT_ADDR + (pumpNo - 1)

        res,err = self.plc.write_register(addr, flowrate)
        if err != 0:
            return False
        else:
            return True

    def getPumpAbnormalTerminationStatus(self, pumpNo):
        addr = address.FEEDBACK_PUMP_ERROR_ADDR
        bitpos = (pumpNo - 1)
        
        res,err = self.plc.read_coil(addr, bitpos)
        if res == True:
            return True
        else:
            return False



    # get value that was set
    def getPumpRunningRPM(self, pumpNo):
        addr = address.FEEDBACK_PUMP_HZ_ADDR + (pumpNo - 1)
        res,err = self.plc.read_register(addr, 1)
        if err > 0:
            return 0, err
        else:
            return res.registers[0],err


    # get overall flow rate setting
    def  getPumpRunningFlowRate(self, pumpNo):
        addr = address.FEEDBACK_PUMP_FLOWRATE_ADDR + (pumpNo - 1)
        res,err = self.plc.read_register(addr, 1)
        if err > 0:
            return 0, err
        else:
            return res.registers[0], err


    def getPumpSpeed(self, pumpNo):
        addr = address.FEEDBACK_PUMP_HZ_ADDR + (pumpNo - 1)
        res,err = self.plc.read_register(addr, 1)
        if err > 0:
            return 0, err
        else:
            return res.registers[0], err
    

    def getPumpFlowrate(self, pumpNo):
        addr = address.FEEDBACK_PUMP_FLOWRATE_ADDR + (pumpNo - 1)
        res,err = self.plc.read_register(addr, 1)
        if err > 0:
            return 0, err
        else:
            return res.registers[0], err


    def getPumpMode(self, pumpNo):
        if pumpNo == 1:
            addr = address.FEEDBACK_PUMP1_MODE_ADDR
        elif pumpNo == 2:
            addr = address.FEEDBACK_PUMP2_MODE_ADDR

        res,err = self.plc.read_register(addr, 1)

        if err > 0:
            return 0, err
        else:
            return res.registers[0], err

    # =========================================
    # Fill drain mode or normal mode
    def setPumpFillDrainMode(self, pumpNo, bFillMode):
        addr = address.CTRL_PUMP_FILL_DRAIN_MODE_ADDR
        bitpos = address.CTRL_PUMP_FILL_DRAIN_MODE_BITPOS + (pumpNo - 1)
        res,err = self.plc.write_coil(addr, bitpos, bFillMode)
        if err != 0:
            return False
        else:
            return True


    # In fill drain mode, the pump will alternately fill and drain, this function returns whether it is in fill or drain mode
    def bIsPumpFilling(self, pumpNo):
        addr = address.FEEDBACK_FILL_MODE_ADDR
        bitpos = address.PUMP_1_FILLING_FLAG_BITPOS + (pumpNo - 1)
        
        res,err = self.plc.read_coil(addr, bitpos)
        if res == True:
            return True
        else:
            return False

    # Set Fill mode and Drain mode value
    def setFillDrainModeSetpoint(self, pumpNo, wFillValue, wDrainValue):
        addr1 = address.CTRL_PUMP_FILL_MODE_FLOWRATE_ADDR + (pumpNo - 1)
        addr2 = address.CTRL_PUMP_DRAIN_MODE_FLOWRATE + (pumpNo - 1)
        res,err = self.plc.write_register(addr1, wFillValue)
        if err != 0:
            return False

        res,err = self.plc.write_register(addr2, wDrainValue)
        if err != 0:
            return False
        else:
            return True

    # Set Fill and Drain duration in seconds
    def setFillDrainModeDuration_s(self, pumpNo, wFillDuration_s, wDrainDuration_s):
        addr1 = address.CTRL_PUMP_FILL_DURATION_ADDR + (pumpNo - 1)
        addr2 = address.CTRL_PUMP_DRAIN_DURATION_ADDR + (pumpNo - 1)
        res,err = self.plc.write_register(addr1, wFillDuration_s)
        if err != 0:
            return False

        res,err = self.plc.write_register(addr2, wDrainDuration_s)
        if err != 0:
            return False
        else:
            return True


    # Get current Fill Drain action (whether it is filling or draining)
    def getCurrentFillDrainAction(self, pumpNo):

        addr = address.FEEDBACK_FILL_MODE_ADDR + (pumpNo - 1)

        res,err = self.plc.read_register(addr, 1)
        return res.registers[0], err


    # ============================================


    def toggleSched(self, shelfno, state):
        addr = address.CTRL_SHELF_USE_SCHEDULER_ADDR
        bitpos = shelfno - 1
        res,err = self.plc.write_coil(addr, bitpos, state)
        if err != 0:
            return False
        else:
            return True


    def genericSend(self, addr, value):
        res,err = self.plc.write_register(addr, value)
        if err != 0:
            return False
        else:
            return True


    def genericRead(self, addr):
        res,err = self.plc.read_register(addr, 1)
        return res.registers[0], err
            


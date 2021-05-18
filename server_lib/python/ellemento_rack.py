'''
This class will handle the rack: shelf lighting, water, pump, etc.


'''

import address
import utils
import modbus_io

class ellemento_rack(object):

    plc = modbus_io.plc()
    
    def __init__ (self, ip):
        super().__init__()
        self.plc.setIP(ip)
        print ("Ellemento rack client connected")


    def __del__(self):
        print ("Ellemento rack client disconnected")
        #self.client.close()


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



    def changeMode(self, mode):

        modeAddress = address.modeAddress

        if mode == 1:
            # Auto mode
            values = 1
            res,err = self.plc.write_register(modeAddress, values)
            
        elif mode == 2:
            # Semi auto mode
            values = 2
            res,err = self.plc.write_registers(modeAddress, values)

        else:
            # Manual mode
            values = 3
            res,err = self.plc.write_registers(modeAddress, values)

    
    #================================================================
    # Lighting
    #================================================================

    def getShelfLEDOnAddress(self, ledNum):
        ledOnAddress = address.SHELF_LIGHT_ON_ADDRESS[ledNum];
        return ledOnAddress
    

    def toggleLED(self, ledNum, bOnOff):
        ledOnAddress = getShelfLEDOnAddress(ledNum)
        res,err = self.plc.write_coil(ledOnAddress, address.SHELF_LIGHT_ON_BITPOS[ledNum], bOnOff)

    
    def getLEDStatus(self, ledNum):
        ledOnAddress = getShelfLEDOnAddress(ledNum)
        res,err = self.plc.read_coil(ledOnAddress, address.SHELF_LIGHT_ON_BITPOS[ledNum])
        if res == True:
            return True
        else:
            return False

    def getShelfLEDIntensityAddress(self, ledNum):
        ledIntensityAddress = address.SHELF_LIGHT_INTENSITY_ADDRESS[ledNum]
        return ledIntensityAddress

    def setLEDIntensity(self, ledNum, intensity):
        ledIntensityAddress = getShelfLEDIntensityAddress(ledNum)
        res,err = self.plc.write_register(ledIntensityAddress, intensity)

    def getLEDIntensity(self, ledNum):
        ledIntensityAddress = getShelfLEDIntensityAddress(ledNum)
        res,err = self.plc.read_register(ledIntensityAddress, 1)
        if res.registers[0] == 1:
            return True
        else:
            return False


    #================================================================
    # PV
    #================================================================

    def togglePV(self, pvNum, bOnOff):
        pvOnAddress = address.SHELF_PV_ON_ADDRESS[pvNum]
        res,err = self.plc.write_coil(pvOnAddress, address.SHELF_PV_ON_BITPOS[pvNum], bOnOff)

    def setShelfPVPosition(self, pvNum, pvPos):
        pvPosAddress = address.SHELF_PV_POSITION_ADDRESS[pvNum]
        res,err = self.plc.write_register(pvPosAddress,pvPos)

    def setShelfPVLUTPosition(self, pvNum, pvPos):
        pvPosAddress = address.SHELF_PV_LUT_ADDRESS[pvNum]
        res,err = self.plc.write_register(pvPosAddress,pvPos)
    


    #================================================================
    # Pump
    #================================================================

    # set pump mode: auto, manual flowrate, manual RPM
    def setPumpMode(self, pumpNo, mode):
        if pumpNo == 1:
            addr = address.PUMP_0_MODE_ADDRESS
        else:
            addr = address.PUMP_1_MODE_ADDRESS

        res,err = self.plc.write_register(addr, mode)
        if err != 0:
            return False
        else:
            return True

    # get pump mode
    def getPumpMode(self, pumpNo):
        if pumpNo == 1:
            addr = address.PUMP_0_MODE_ADDRESS
        else:
            addr = address.PUMP_1_MODE_ADDRESS

        res,err = self.plc.read_register(addr, 1)
        return res.registers[0],err

    
    # set pump RPM
    def setPumpRPM(self, pumpNo, RPM):
        if pumpNo == 1:
            addr = address.PUMP_0_SET_RPM_ADDRESS
        else:
            addr = address.PUMP_1_SET_RPM_ADDRESS

        res,err = self.plc.write_register(addr, RPM)
        if err != 0:
            return False
        else:
            return True

    # get value that was set
    def getPumpRPMsetting(self, pumpNo):
        if pumpNo == 1:
            addr = address.PUMP_0_SET_RPM_ADDRESS
        else:
            addr = address.PUMP_1_SET_RPM_ADDRESS

        res,err = self.plc.read_register(addr, 1)
        return res.registers[0],err

    # get actual running RPM
    def getPumpRunningRPM(self, pumpNo):
        if pumpNo == 1:
            addr = address.PUMP_0_CURRENT_RPM_ADDRESS
        else:
            addr = address.PUMP_1_CURRENT_RPM_ADDRESS

        res,err = self.plc.read_register(addr, 1)
        return res.registers[0],err


    # Set overall flow rate setting
    def  setPumpFlowRate(self, pumpNo, wFlowrate):
        if pumpNo == 1:
            addr = address.PUMP_0_FLOWRATE_ADDRESS
        else:
            addr = address.PUMP_1_FLOWRATE_ADDRESS

        res,err = self.plc.write_register(addr, wFlowrate)
        if err != 0:
            return False
        else:
            return True


    # get overall flow rate setting
    def  getPumpFlowRate(self, pumpNo):
        if pumpNo == 1:
            addr = address.PUMP_0_FLOWRATE_ADDRESS
        else:
            addr = address.PUMP_1_FLOWRATE_ADDRESS

        res,err = self.plc.read_register(addr, 1)
        return res.registers[0],err


    # set flow rate per shelf
    def  setPumpFlowRatePerShelf(self, pumpNo, wFlowrate):
        res = 0
        err = 0
        if pumpNo == 1:
            addr = address.PUMP_0_FLOWRATE_PER_SHELF_ADDRESS
        else:
            addr = address.PUMP_1_FLOWRATE_PER_SHELF_ADDRESS

        res,err = self.plc.write_register(addr, wFlowrate)

        if err != 0:
            return False
        else:
            return True

    # get flow rate per shelf setting
    def  getPumpFlowRatePerShelf(self, pumpNo):
        if pumpNo == 1:
            res,err = self.plc.read_register(address.PUMP_0_FLOWRATE_PER_SHELF_ADDRESS, 1)
            return res.registers[0],err
        else:
            res,err = self.plc.read_register(address.PUMP_1_FLOWRATE_PER_SHELF_ADDRESS, 1)
            return res.registers[0],err


    # recover from stoppage due to low water and pump PID ramp-up too fast
    def recoverPump(self, pumpNo):
        if pumpNo == 1:
            res,err = self.plc.write_coil(address.PUMP_0_RECOVER_ADDRESS, address.PUMP_0_RECOVER_BITPOS, True)
            return res.registers[0],err
        else:
            res,err = self.plc.write_coil(address.PUMP_1_RECOVER_ADDRESS, address.PUMP_1_RECOVER_BITPOS, True)
            return res.registers[0],err


    # =========================================
    # Fill drain mode or normal mode
    def setPumpFillDrainMode(self, pumpNo, bFillMode):
        if pumpNo == 1:
            addr = address.PUMP_0_FILL_DRAIN_MODE_ADDRESS
            bitpos = address.PUMP_0_FILL_DRAIN_MODE_BITPOS
        else:
            addr = address.PUMP_1_FILL_DRAIN_MODE_ADDRESS
            bitpos = address.PUMP_1_FILL_DRAIN_MODE_BITPOS

        res,err = self.plc.write_coil(addr, bitpos, bFillMode)
        if err != 0:
            return False
        else:
            return True

    # Check whether pump is in Fill drain mode or Normal mode
    def  bIsPumpInFillDrainMode(self, pumpNo):
        if pumpNo == 1:
            addr = address.PUMP_0_FILL_DRAIN_MODE_ADDRESS
            bitpos = address.PUMP_0_FILL_DRAIN_MODE_BITPOS
        else:
            addr = address.PUMP_1_FILL_DRAIN_MODE_ADDRESS
            bitpos = address.PUMP_1_FILL_DRAIN_MODE_BITPOS

        res,err = self.plc.read_coil(addr, bitpos)
        if res.registers[0] == True:
            return True
        else:
            return False

    # In fill drain mode, the pump will alternately fill and drain, this function returns whether it is in fill or drain mode
    def bIsPumpFilling(self, pumpNo):
        if pumpNo == 1:
            addr = address.PUMP_0_FILLING_FLAG_ADDRESS
            bitpos = address.PUMP_0_FILLING_FLAG_BITPOS
        else:
            addr = address.PUMP_1_FILLING_FLAG_ADDRESS
            bitpos = address.PUMP_1_FILLING_FLAG_BITPOS
        
        res,err = self.plc.read_coil(addr, bitpos)
        if res.registers[0] == True:
            return True
        else:
            return False

    # Set Fill mode and Drain mode value
    def setFillDrainModeValue_Hz(self, pumpNo, wFillValue_hz, wDrainValue_hz):

        if pumpNo == 1:
            addr1 = address.PUMP_0_FILL_VALUE_HZ_ADDRESS
            addr2 = address.PUMP_0_DRAIN_VALUE_HZ_ADDRESS
        else:
            addr1 = address.PUMP_1_FILL_VALUE_HZ_ADDRESS
            addr2 = address.PUMP_1_DRAIN_VALUE_HZ_ADDRESS


        res,err = self.plc.write_register(addr1, wFillValue_hz)
        if err != 0:
            return False

        res,err = self.plc.write_register(addr2, wDrainValue_hz)
        if err != 0:
            return False
        else:
            return True

    # Set Fill and Drain duration in seconds
    def setFillDrainModeDuration_s(self, pumpNo, wFillDuration_s, wDrainDuration_s):
        if pumpNo == 1:
            addr1 = address.PUMP_0_FILL_DURATION_ADDRESS
            addr2 = address.PUMP_0_DRAIN_DURATION_ADDRESS
        else:
            addr1 = address.PUMP_1_FILL_DURATION_ADDRESS
            addr2 = address.PUMP_1_DRAIN_DURATION_ADDRESS

        res,err = self.plc.write_register(addr1, wFillDuration_s)
        if err != 0:
            return False

        res,err = self.plc.write_register(addr2, wDrainDuration_s)
        if err != 0:
            return False
        else:
            return True

    # Get Fill drain timer value
    def getFillDrainTimerValue(self, pumpNo):
        if pumpNo == 1:
            addr = address.PUMP_0_FILL_DRAIN_TIMER_ADDRESS
        else:
            addr = address.PUMP_1_FILL_DRAIN_TIMER_ADDRESS

        res,err = self.plc.read_register(addr, 1)
        return res.registers[0], err        


    # Get current Fill Drain action (whether it is filling or draining)
    def getCurrentFillDrainAction(self, pumpNo):
        if pumpNo == 1:
            addr = address.PUMP_0_FILL_DRAIN_ACTION_ADDRESS
        else:
            addr = address.PUMP_1_FILL_DRAIN_ACTION_ADDRESS

        res,err = self.plc.read_register(addr, 1)
        return res.registers[0], err


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
        res,err = self.plc.write_register(1000, 1512)   #.write_registers(1000, 1512, unit=1)
        res,err = self.plc.write_register(2000, False)

        res,err = self.plc.read_register(1000, 1)
        print(res.registers[0])

        #rr2 = self.client.read_holding_registers(2000, 1, unit=1)
        #print(rr2.registers[0])

        #rr = self.client.read_holding_registers(1000, 1, unit=1)
        #dassert(rq, lambda r: not r.isError())     # test for no error
        #print (r.registers)
        
        #val2 = self.client.read_holding_registers(2000, 1, unit=1)


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
        res,err = self.plc.write_register(ledOnAddress, bOnOff)

    
    def getLEDStatus(self, ledNum):
        ledOnAddress = getShelfLEDOnAddress(ledNum)
        res,err = self.plc.read_holding_registers(ledOnAddress, 1)
        if res.registers[0] == 1:
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
        res,err = self.plc.write_register(pvOnAddress, bOnOff)

    def setShelfPVPosition(self, pvNum, pvPos):
        pvPosAddress = address.SHELF_PV_POSITION_ADDRESS[pvNum]
        res,err = self.plc.write_register(pvPosAddress,pvPos)

    def setShelfPVLUTPosition(self, pvNum, pvPos):
        pvPosAddress = address.SHELF_PV_LUT_ADDRESS[pvNum]
        res,err = self.plc.write_register(pvPosAddress,pvPos)
    


    #================================================================
    # Pump
    #================================================================

    # Set overall flow rate setting
    def  setPumpFlowRate(self, wFlowrate):
        res,err = self.plc.write_register(address.PUMP_FLOWRATE_SET_ADDRESS, wFlowrate)
        if err != 0:
            return False
        else:
            return True

    # get overall flow rate setting
    def  getPumpFlowRate(self):
        res,err = self.plc.read_register(address.PUMP_FLOWRATE_ADDRESS, 1)
        return res.registers[0],err

    # set flow rate per shelf
    def  setPumpFlowRatePerShelf(self, wFlowrate):
        res,err = self.plc.write_register(address.PUMP_FLOWRATE_PER_SHELF_SET_ADDRESS, wFlowrate)
        if err != 0:
            return False
        else:
            return True

    # get flow rate per shelf setting
    def  getPumpFlowRatePerShelf(self):
        res,err = self.plc.read_register(address.PUMP_FLOWRATE_PER_SHELF_ADDRESS, 1)
        return res.registers[0],err


    # =========================================
    # Fill drain mode or normal mode
    def setPumpFillDrainMode(self, bFillMode):
        res,err = self.plc.write_register(address.PUMP_FILL_DRAIN_MODE_ADDRESS, bFillMode)
        if err != 0:
            return False
        else:
            return True

    # Check whether pump is in Fill drain mode
    def  bIsPumpInFillDrainMode(self):
        res,err = self.plc.read_register(address.PUMP_FILL_DRAIN_MODE_ADDRESS, 1)
        return res.registers[0],err

    # Set Fill mode and Drain mode value
    def setFillDrainModeValue_Hz(self, wFillValue_hz, wDrainValue_hz):
        res,err = self.plc.write_register(address.PUMP_FILL_VALUE_HZ_ADDRESS, wFillValue_hz)
        if err != 0:
            return False

        res,err = self.plc.write_register(address.PUMP_DRAIN_VALUE_HZ_ADDRESS, wDrainValue_hz)
        if err != 0:
            return False
        else:
            return True

    # Set Fill and Drain duration in seconds
    def setFillDrainModeDuration_s(self, wFillDuration_s, wDrainDuration_s):
        res,err = self.plc.write_register(address.PUMP_FILL_DURATION_ADDRESS, wFillDuration_s)
        if err != 0:
            return False

        res,err = self.plc.write_register(address.PUMP_DRAIN_DURATION_ADDRESS, wDrainDuration_s)
        if err != 0:
            return False
        else:
            return True

    # Get Fill drain timer value
    def getFillDrainTimerValue(self):
        res,err = self.plc.read_register(address.PUMP_FILL_DRAIN_TIMER_ADDRESS, 1)
        return res.registers[0],err        

    # Get current Fill Drain action (whether it is filling or draining)
    def getCurrentFillDrainAction(self):
        res,err = self.plc.read_register(address.PUMP_FILL_DRAIN_ACTION_ADDRESS, 1)
        return res.registers[0],err


'''
    This module contains the UI elements

'''

from ellemento_rack import ellemento_rack

import config
import tkinter as tk


class Application(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.create_ui(master)

        self.currPanPos = 0
        self.currTiltPos = 0

        self.modbusError = False

        self.elem1 = ellemento_rack(config.PLC_IP_ADDRESS)

        self.racktype = 0
        
        self.root = self.master 

        
    # Draw the UI
    def create_ui(self, root):
        self.master.title("Ellemento Farm Test GUI")
        self.master.resizable(0,0)

        # Grid
        content = tk.Frame(root)
        frame = tk.Frame(content, borderwidth=5, relief="sunken", width=1366, height=768)
        namelbl = tk.Label(content, text="Name")
        name = tk.Entry(content)

        content.grid(column=0, row=0)
        frame.grid(column=0, row=0, columnspan=20, rowspan=22)

        self.drawPVButtons(content)
        self.drawLEDControls(content)
        self.drawPumpControl(content)
        self.drawSectionControl(content)

        self.drawApplyButton(content)



    def drawPVButtons(self, content):

        self.pv1Btn = tk.Button(content, text="PV1 On")
        self.pv1Btn["command"] = self.pv1OnClick
        self.pv1Btn.grid(column=2, row=1, columnspan=1)

        self.pv2Btn = tk.Button(content, text="PV2 On")
        self.pv2Btn["command"] = self.pv2OnClick
        self.pv2Btn.grid(column=2, row=2, columnspan=1)

        self.pv3Btn = tk.Button(content, text="PV3 On")
        self.pv3Btn["command"] = self.pv3OnClick
        self.pv3Btn.grid(column=2, row=3, columnspan=1)

        self.pv4Btn = tk.Button(content, text="PV4 On")
        self.pv4Btn["command"] = self.pv4OnClick
        self.pv4Btn.grid(column=2, row=4, columnspan=1)

        self.pv5Btn = tk.Button(content, text="PV5 On")
        self.pv5Btn["command"] = self.pv5OnClick
        self.pv5Btn.grid(column=2, row=5, columnspan=1)

        self.pv6Btn = tk.Button(content, text="PV6 On")
        self.pv6Btn["command"] = self.pv6OnClick
        self.pv6Btn.grid(column=2, row=6, columnspan=1)

        self.pv7Btn = tk.Button(content, text="PV7 On")
        self.pv7Btn["command"] = self.pv7OnClick
        self.pv7Btn.grid(column=2, row=7, columnspan=1)

        self.pv8Btn = tk.Button(content, text="PV8 On")
        self.pv8Btn["command"] = self.pv8OnClick
        self.pv8Btn.grid(column=2, row=8, columnspan=1)

        self.pv9Btn = tk.Button(content, text="PV9 On")
        self.pv9Btn["command"] = self.pv9OnClick
        self.pv9Btn.grid(column=2, row=9, columnspan=1)

        self.pv10Btn = tk.Button(content, text="PV10 On")
        self.pv10Btn["command"] = self.pv10OnClick
        self.pv10Btn.grid(column=2, row=10, columnspan=1)

        self.pv11Btn = tk.Button(content, text="PV11 On")
        self.pv11Btn["command"] = self.pv11OnClick
        self.pv11Btn.grid(column=2, row=11, columnspan=1)

        self.pv12Btn = tk.Button(content, text="PV12 On")
        self.pv12Btn["command"] = self.pv12OnClick
        self.pv12Btn.grid(column=2, row=12, columnspan=1)

        self.pv13Btn = tk.Button(content, text="PV13 On")
        self.pv13Btn["command"] = self.pv13OnClick
        self.pv13Btn.grid(column=2, row=13, columnspan=1)

        self.pv14Btn = tk.Button(content, text="PV14 On")
        self.pv14Btn["command"] = self.pv14OnClick
        self.pv14Btn.grid(column=2, row=14, columnspan=1)

        #==================================

        self.pv1Btn = tk.Button(content, text="PV1 Off")
        self.pv1Btn["command"] = self.pv1OffClick
        self.pv1Btn.grid(column=3, row=1, columnspan=1)

        self.pv2Btn = tk.Button(content, text="PV2 Off")
        self.pv2Btn["command"] = self.pv2OffClick
        self.pv2Btn.grid(column=3, row=2, columnspan=1)

        self.pv3Btn = tk.Button(content, text="PV3 Off")
        self.pv3Btn["command"] = self.pv3OffClick
        self.pv3Btn.grid(column=3, row=3, columnspan=1)

        self.pv4Btn = tk.Button(content, text="PV4 Off")
        self.pv4Btn["command"] = self.pv4OffClick
        self.pv4Btn.grid(column=3, row=4, columnspan=1)

        self.pv5Btn = tk.Button(content, text="PV5 Off")
        self.pv5Btn["command"] = self.pv5OffClick
        self.pv5Btn.grid(column=3, row=5, columnspan=1)

        self.pv6Btn = tk.Button(content, text="PV6 Off")
        self.pv6Btn["command"] = self.pv6OffClick
        self.pv6Btn.grid(column=3, row=6, columnspan=1)

        self.pv7Btn = tk.Button(content, text="PV7 Off")
        self.pv7Btn["command"] = self.pv7OffClick
        self.pv7Btn.grid(column=3, row=7, columnspan=1)

        self.pv8Btn = tk.Button(content, text="PV8 Off")
        self.pv8Btn["command"] = self.pv8OffClick
        self.pv8Btn.grid(column=3, row=8, columnspan=1)

        self.pv9Btn = tk.Button(content, text="PV9 Off")
        self.pv9Btn["command"] = self.pv9OffClick
        self.pv9Btn.grid(column=3, row=9, columnspan=1)

        self.pv10Btn = tk.Button(content, text="PV10 Off")
        self.pv10Btn["command"] = self.pv10OffClick
        self.pv10Btn.grid(column=3, row=10, columnspan=1)

        self.pv11Btn = tk.Button(content, text="PV11 Off")
        self.pv11Btn["command"] = self.pv11OffClick
        self.pv11Btn.grid(column=3, row=11, columnspan=1)

        self.pv12Btn = tk.Button(content, text="PV12 Off")
        self.pv12Btn["command"] = self.pv12OffClick
        self.pv12Btn.grid(column=3, row=12, columnspan=1)

        self.pv13Btn = tk.Button(content, text="PV13 Off")
        self.pv13Btn["command"] = self.pv13OffClick
        self.pv13Btn.grid(column=3, row=13, columnspan=1)

        self.pv14Btn = tk.Button(content, text="PV14 Off")
        self.pv14Btn["command"] = self.pv14OffClick
        self.pv14Btn.grid(column=3, row=14, columnspan=1)

        # ---------------------------------------

        self.pv1Position = tk.Entry(content)
        self.pv1Position.grid(column=4, row=1, columnspan=1)

        self.pv2Position = tk.Entry(content)
        self.pv2Position.grid(column=4, row=2, columnspan=1)

        self.pv3Position = tk.Entry(content)
        self.pv3Position.grid(column=4, row=3, columnspan=1)

        self.pv4Position = tk.Entry(content)
        self.pv4Position.grid(column=4, row=4, columnspan=1)

        self.pv5Position = tk.Entry(content)
        self.pv5Position.grid(column=4, row=5, columnspan=1)

        self.pv6Position = tk.Entry(content)
        self.pv6Position.grid(column=4, row=6, columnspan=1)

        self.pv7Position = tk.Entry(content)
        self.pv7Position.grid(column=4, row=7, columnspan=1)

        self.pv8Position = tk.Entry(content)
        self.pv8Position.grid(column=4, row=8, columnspan=1)

        self.pv9Position = tk.Entry(content)
        self.pv9Position.grid(column=4, row=9, columnspan=1)

        self.pv10Position = tk.Entry(content)
        self.pv10Position.grid(column=4, row=10, columnspan=1)

        self.pv11Position = tk.Entry(content)
        self.pv11Position.grid(column=4, row=11, columnspan=1)

        self.pv12Position = tk.Entry(content)
        self.pv12Position.grid(column=4, row=12, columnspan=1)

        self.pv13Position = tk.Entry(content)
        self.pv13Position.grid(column=4, row=13, columnspan=1)

        self.pv14Position = tk.Entry(content)
        self.pv14Position.grid(column=4, row=14, columnspan=1)


        # PV status in UI
        self.uiPVFeedback = tk.StringVar()
        self.uiPVFeedback.set("PV status")
        self.PVFeedbackLabel = tk.Label( content, textvariable=self.uiPVFeedback )
        self.PVFeedbackLabel.grid(column=1, row=15, columnspan=5)


        self.pvUpdateBtn = tk.Button(content, text="Update PV setting")
        self.pvUpdateBtn["command"] = self.pvUpdateClick
        self.pvUpdateBtn.grid(column=4, row=17, columnspan=1)


    


        
    def updateSetPVPos(self):

        for x in range(14):

            switcher = {
                1: self.pv1Position,
                2: self.pv2Position,
                3: self.pv3Position,
                4: self.pv4Position,
                5: self.pv5Position,
                6: self.pv6Position,
                7: self.pv7Position,
                8: self.pv8Position,
                9: self.pv9Position,
                10: self.pv10Position,
                11: self.pv11Position,
                12: self.pv12Position,
                13: self.pv13Position,
                14: self.pv14Position
            }
            # Get the function from switcher dictionary
            func = switcher.get(x+1)

            tmps = func.get()

            if tmps == "":
                pvpos = 0
            else:
                pvpos = int(tmps, 10)
                
            self.elem1.setShelfPVPosition(x+1, pvpos)



        # --------------------------------------


    def drawLEDControls(self, content):
        self.led1Btn = tk.Button(content, text="LED1 On")
        self.led1Btn["command"] = self.led1OnClick
        self.led1Btn.grid(column=7, row=1, columnspan=1)

        self.led2Btn = tk.Button(content, text="LED2 On")
        self.led2Btn["command"] = self.led2OnClick
        self.led2Btn.grid(column=7, row=2, columnspan=1)

        self.led3Btn = tk.Button(content, text="LED3 On")
        self.led3Btn["command"] = self.led3OnClick
        self.led3Btn.grid(column=7, row=3, columnspan=1)

        self.led4Btn = tk.Button(content, text="LED4 On")
        self.led4Btn["command"] = self.led4OnClick
        self.led4Btn.grid(column=7, row=4, columnspan=1)

        self.led5Btn = tk.Button(content, text="LED5 On")
        self.led5Btn["command"] = self.led5OnClick
        self.led5Btn.grid(column=7, row=5, columnspan=1)

        self.led6Btn = tk.Button(content, text="LED6 On")
        self.led6Btn["command"] = self.led6OnClick
        self.led6Btn.grid(column=7, row=6, columnspan=1)

        self.led7Btn = tk.Button(content, text="LED7 On")
        self.led7Btn["command"] = self.led7OnClick
        self.led7Btn.grid(column=7, row=7, columnspan=1)

        self.led8Btn = tk.Button(content, text="LED8 On")
        self.led8Btn["command"] = self.led8OnClick
        self.led8Btn.grid(column=7, row=8, columnspan=1)

        self.led9Btn = tk.Button(content, text="LED9 On")
        self.led9Btn["command"] = self.led9OnClick
        self.led9Btn.grid(column=7, row=9, columnspan=1)

        self.led10Btn = tk.Button(content, text="LED10 On")
        self.led10Btn["command"] = self.led10OnClick
        self.led10Btn.grid(column=7, row=10, columnspan=1)

        self.led11Btn = tk.Button(content, text="LED11 On")
        self.led11Btn["command"] = self.led11OnClick
        self.led11Btn.grid(column=7, row=11, columnspan=1)

        self.led12Btn = tk.Button(content, text="LED12 On")
        self.led12Btn["command"] = self.led12OnClick
        self.led12Btn.grid(column=7, row=12, columnspan=1)

        self.led13Btn = tk.Button(content, text="LED13 On")
        self.led13Btn["command"] = self.led13OnClick
        self.led13Btn.grid(column=7, row=13, columnspan=1)

        self.led14Btn = tk.Button(content, text="LED14 On")
        self.led14Btn["command"] = self.led14OnClick
        self.led14Btn.grid(column=7, row=14, columnspan=1)

        #==================================

        self.led1Btn = tk.Button(content, text="LED1 Off")
        self.led1Btn["command"] = self.led1OffClick
        self.led1Btn.grid(column=8, row=1, columnspan=1)

        self.led2Btn = tk.Button(content, text="LED2 Off")
        self.led2Btn["command"] = self.led2OffClick
        self.led2Btn.grid(column=8, row=2, columnspan=1)

        self.led3Btn = tk.Button(content, text="LED3 Off")
        self.led3Btn["command"] = self.led3OffClick
        self.led3Btn.grid(column=8, row=3, columnspan=1)

        self.led4Btn = tk.Button(content, text="LED4 Off")
        self.led4Btn["command"] = self.led4OffClick
        self.led4Btn.grid(column=8, row=4, columnspan=1)

        self.led5Btn = tk.Button(content, text="LED5 Off")
        self.led5Btn["command"] = self.led5OffClick
        self.led5Btn.grid(column=8, row=5, columnspan=1)

        self.led6Btn = tk.Button(content, text="LED6 Off")
        self.led6Btn["command"] = self.led6OffClick
        self.led6Btn.grid(column=8, row=6, columnspan=1)

        self.led7Btn = tk.Button(content, text="LED7 Off")
        self.led7Btn["command"] = self.led7OffClick
        self.led7Btn.grid(column=8, row=7, columnspan=1)

        self.led8Btn = tk.Button(content, text="LED8 Off")
        self.led8Btn["command"] = self.led8OffClick
        self.led8Btn.grid(column=8, row=8, columnspan=1)

        self.led9Btn = tk.Button(content, text="LED9 Off")
        self.led9Btn["command"] = self.led9OffClick
        self.led9Btn.grid(column=8, row=9, columnspan=1)

        self.led10Btn = tk.Button(content, text="LED10 Off")
        self.led10Btn["command"] = self.led10OffClick
        self.led10Btn.grid(column=8, row=10, columnspan=1)

        self.led11Btn = tk.Button(content, text="LED11 Off")
        self.led11Btn["command"] = self.led11OffClick
        self.led11Btn.grid(column=8, row=11, columnspan=1)

        self.led12Btn = tk.Button(content, text="LED12 Off")
        self.led12Btn["command"] = self.led12OffClick
        self.led12Btn.grid(column=8, row=12, columnspan=1)

        self.led13Btn = tk.Button(content, text="LED13 Off")
        self.led13Btn["command"] = self.led13OffClick
        self.led13Btn.grid(column=8, row=13, columnspan=1)

        self.led14Btn = tk.Button(content, text="LED14 Off")
        self.led14Btn["command"] = self.led14OffClick
        self.led14Btn.grid(column=8, row=14, columnspan=1)

        # --------------------------------------------

        self.led1Intensity = tk.Entry(content)
        self.led1Intensity.grid(column=9, row=1, columnspan=1)

        self.led2Intensity = tk.Entry(content)
        self.led2Intensity.grid(column=9, row=2, columnspan=1)

        self.led3Intensity = tk.Entry(content)
        self.led3Intensity.grid(column=9, row=3, columnspan=1)

        self.led4Intensity = tk.Entry(content)
        self.led4Intensity.grid(column=9, row=4, columnspan=1)

        self.led5Intensity = tk.Entry(content)
        self.led5Intensity.grid(column=9, row=5, columnspan=1)

        self.led6Intensity = tk.Entry(content)
        self.led6Intensity.grid(column=9, row=6, columnspan=1)

        self.led7Intensity = tk.Entry(content)
        self.led7Intensity.grid(column=9, row=7, columnspan=1)

        self.led8Intensity = tk.Entry(content)
        self.led8Intensity.grid(column=9, row=8, columnspan=1)

        self.led9Intensity = tk.Entry(content)
        self.led9Intensity.grid(column=9, row=9, columnspan=1)

        self.led10Intensity = tk.Entry(content)
        self.led10Intensity.grid(column=9, row=10, columnspan=1)

        self.led11Intensity = tk.Entry(content)
        self.led11Intensity.grid(column=9, row=11, columnspan=1)

        self.led12Intensity = tk.Entry(content)
        self.led12Intensity.grid(column=9, row=12, columnspan=1)

        self.led13Intensity = tk.Entry(content)
        self.led13Intensity.grid(column=9, row=13, columnspan=1)

        self.led14Intensity = tk.Entry(content)
        self.led14Intensity.grid(column=9, row=14, columnspan=1)

        # LED status
        self.uiLEDFeedback = tk.StringVar()
        self.uiLEDFeedback.set("LED status")
        self.LEDFeedbackLabel = tk.Label( content, textvariable=self.uiLEDFeedback )
        self.LEDFeedbackLabel.grid(column=7, row=15, columnspan=4)

        
        self.ledUpdateBtn = tk.Button(content, text="Update LED setting")
        self.ledUpdateBtn["command"] = self.LEDUpdateClick
        self.ledUpdateBtn.grid(column=9, row=17, columnspan=1)


        
    def updateSetLEDPos(self):

        for x in range(14):

            switcher = {
                1: self.led1Intensity,
                2: self.led2Intensity,
                3: self.led3Intensity,
                4: self.led4Intensity,
                5: self.led5Intensity,
                6: self.led6Intensity,
                7: self.led7Intensity,
                8: self.led8Intensity,
                9: self.led9Intensity,
                10: self.led10Intensity,
                11: self.led11Intensity,
                12: self.led12Intensity,
                13: self.led13Intensity,
                14: self.led14Intensity
            }
            # Get the function from switcher dictionary
            func = switcher.get(x+1)

            tmps = func.get()

            if tmps == "":
                ledpos = 0
            else:
                ledpos = int(tmps, 10)

            self.elem1.setLEDIntensity(x+1, ledpos)


    # ----------------------------------------

    def drawPumpControl(self, content):

        rowOffset = 1

        self.pump1Label1Text = tk.StringVar()
        self.pump1Label1Text.set("Pump 1")
        self.pump1Label1 = tk.Label( content, textvariable=self.pump1Label1Text )
        self.pump1Label1.grid(column=12, row=rowOffset, columnspan=1)

        self.uipump1Onbutton = tk.Button(content, text="ON")
        self.uipump1Onbutton["command"] = self.uipump1OnbuttonClick
        self.uipump1Onbutton.grid(column=13, row=rowOffset, columnspan=1)

        self.uipump1Offbutton = tk.Button(content, text="OFF")
        self.uipump1Offbutton["command"] = self.uipump1OffbuttonClick
        self.uipump1Offbutton.grid(column=14, row=rowOffset, columnspan=1)


        self.uipump1FlowSetting = tk.Entry(content)
        self.uipump1FlowSetting.grid(column=13, row=rowOffset+1, columnspan=1)

        self.uipump1flowrateFeedback = tk.StringVar()
        self.uipump1flowrateFeedback.set("l/min")
        self.pump1flowrate = tk.Label( content, textvariable=self.uipump1flowrateFeedback )
        self.pump1flowrate.grid(column=14, row=rowOffset+1, columnspan=1)

        self.uipump1HzSetting = tk.Entry(content)
        self.uipump1HzSetting.grid(column=13, row=rowOffset+2, columnspan=1)

        self.uipump1HzFeedback = tk.StringVar()
        self.uipump1HzFeedback.set("Hz")
        self.pump1Hz = tk.Label( content, textvariable=self.uipump1HzFeedback )
        self.pump1Hz.grid(column=14, row=rowOffset+2, columnspan=1)

        self.uipump1ModeFeedback = tk.StringVar()
        self.uipump1ModeFeedback.set("Mode")
        self.uipump1ModeDisplay = tk.Label(content, textvariable=self.uipump1ModeFeedback) 
        self.uipump1ModeDisplay.grid(column=12, row=rowOffset+3, columnspan=1 )

        # pump mode buttons
        self.uipump1Autobutton = tk.Button(content, text="AUTO")
        self.uipump1Autobutton["command"] = self.uipump1AutobuttonClick
        self.uipump1Autobutton.grid(column=13, row=rowOffset+3, columnspan=1)

        self.uipump1Flowbutton = tk.Button(content, text="FLOW")
        self.uipump1Flowbutton["command"] = self.uipump1FlowbuttonClick
        self.uipump1Flowbutton.grid(column=14, row=rowOffset+3, columnspan=1)

        self.uipump1Hzbutton = tk.Button(content, text="FREQ")
        self.uipump1Hzbutton["command"] = self.uipump1HzbuttonClick
        self.uipump1Hzbutton.grid(column=15, row=rowOffset+3, columnspan=1)

        
        # -----------------------------------
        #  If type B then add second pump
        # -----------------------------------

        # Add fill drain mode

        # enable buttons
        self.uipump1FillDrainModeButton = tk.Button(content, text="Fill/Drain")
        self.uipump1FillDrainModeButton["command"] = self.uipump1FillDrainModeClick
        self.uipump1FillDrainModeButton.grid(column=14, row=rowOffset+5, columnspan=1)

        self.uipump1StaticModeButton = tk.Button(content, text="Static")
        self.uipump1StaticModeButton["command"] = self.uipump1StaticModeClick
        self.uipump1StaticModeButton.grid(column=15, row=rowOffset+5, columnspan=1)


        self.FDLabel1Text = tk.StringVar()
        self.FDLabel1Text.set("Duration")
        self.FDLabel1 = tk.Label( content, textvariable=self.FDLabel1Text )
        self.FDLabel1.grid(column=14, row=rowOffset+6, columnspan=1)

        self.FDLabel2Text = tk.StringVar()
        self.FDLabel2Text.set("Flowrate")
        self.FDLabel2 = tk.Label( content, textvariable=self.FDLabel2Text )
        self.FDLabel2.grid(column=15, row=rowOffset+6, columnspan=1)

        # Fill mode settings
        self.FillLabel1Text = tk.StringVar()
        self.FillLabel1Text.set("Fill settings")
        self.FillLabel1 = tk.Label( content, textvariable=self.FillLabel1Text )
        self.FillLabel1.grid(column=13, row=rowOffset+7, columnspan=1)

        self.FillDuration = tk.Entry(content)
        self.FillDuration.grid(column=14, row=rowOffset+7, columnspan=1)

        self.FillFlowrate = tk.Entry(content)
        self.FillFlowrate.grid(column=15, row=rowOffset+7, columnspan=1)

        # Fill mode settings
        self.DrainLabel1Text = tk.StringVar()
        self.DrainLabel1Text.set("Drain settings")
        self.DrainLabel1 = tk.Label( content, textvariable=self.DrainLabel1Text )
        self.DrainLabel1.grid(column=13, row=rowOffset+8, columnspan=1)

        self.DrainDuration = tk.Entry(content)
        self.DrainDuration.grid(column=14, row=rowOffset+8, columnspan=1)

        self.DrainFlowrate = tk.Entry(content)
        self.DrainFlowrate.grid(column=15, row=rowOffset+8, columnspan=1)

        # Separator
        #self.pumpSeparator = tk.Separator(content, orient='horizontal')
        #self.pumpSeparator.grid(column=13, row=rowOffset+9, columnspan=5)


        # Second pump

        rowOffset = 11

        self.pump2Label1Text = tk.StringVar()
        self.pump2Label1Text.set("Pump 2")
        self.pump2Label1 = tk.Label( content, textvariable=self.pump2Label1Text )
        self.pump2Label1.grid(column=12, row=rowOffset, columnspan=1)

        self.uipump2Onbutton = tk.Button(content, text="ON")
        self.uipump2Onbutton["command"] = self.uipump2OnbuttonClick
        self.uipump2Onbutton.grid(column=13, row=rowOffset, columnspan=1)

        self.uipump2Offbutton = tk.Button(content, text="OFF")
        self.uipump2Offbutton["command"] = self.uipump2OffbuttonClick
        self.uipump2Offbutton.grid(column=14, row=rowOffset, columnspan=1)

        self.uipump2FlowSetting = tk.Entry(content)
        self.uipump2FlowSetting.grid(column=13, row=rowOffset+1, columnspan=1)

        self.uipump2flowrateFeedback = tk.StringVar()
        self.uipump2flowrateFeedback.set("l/min")
        self.pump2flowrate = tk.Label( content, textvariable=self.uipump2flowrateFeedback )
        self.pump2flowrate.grid(column=14, row=rowOffset+1, columnspan=1)

        self.uipump2HzSetting = tk.Entry(content)
        self.uipump2HzSetting.grid(column=13, row=rowOffset+2, columnspan=1)

        self.uipump2HzFeedback = tk.StringVar()
        self.uipump2HzFeedback.set("Hz")
        self.pump2Hz = tk.Label( content, textvariable=self.uipump2HzFeedback )
        self.pump2Hz.grid(column=14, row=rowOffset+2, columnspan=1)

        self.uipump2ModeFeedback = tk.StringVar()
        self.uipump2ModeFeedback.set("Mode")
        self.uipump2ModeDisplay = tk.Label(content, textvariable=self.uipump2ModeFeedback) 
        self.uipump2ModeDisplay.grid(column=12, row=rowOffset+3, columnspan=1 )

        # pump mode buttons
        self.uipump2Autobutton = tk.Button(content, text="AUTO")
        self.uipump2Autobutton["command"] = self.uipump2Autobutton
        self.uipump2Autobutton.grid(column=13, row=rowOffset+3, columnspan=1)

        self.uipump2Flowbutton = tk.Button(content, text="FLOW")
        self.uipump2Flowbutton["command"] = self.uipump2Flowbutton
        self.uipump2Flowbutton.grid(column=14, row=rowOffset+3, columnspan=1)

        self.uipump2Hzbutton = tk.Button(content, text="FREQ")
        self.uipump2Hzbutton["command"] = self.uipump2Hzbutton
        self.uipump2Hzbutton.grid(column=15, row=rowOffset+3, columnspan=1)

        # ----------------------------------

        self.pumpUpdateBtn = tk.Button(content, text="Update Pump setting")
        self.pumpUpdateBtn["command"] = self.pumpUpdateClick
        self.pumpUpdateBtn.grid(column=11, row=17, columnspan=5)


    def updatePumpSetting(self):
        tmp = self.uipump1FlowSetting.get()
        fr = int(tmp)
        self.elem1.setPumpFlowrate(1,fr)

        tmp = self.uipump1HzSetting.get()
        hz = int(tmp)
        self.elem1.setPumpRPM(1,hz)

        tmp = self.uipump2FlowSetting.getint()
        fr = int(tmp)
        self.elem1.setPumpFlowrate(2,fr)

        tmp = self.uipump2HzSetting.getint()
        hz = int(tmp)
        self.elem1.setPumpRPM(2,hz)



    def drawSectionControl(self, content):
        self.sec1ModeAutoBtn = tk.Button(content, text="Sec 1 AUTO")
        self.sec1ModeAutoBtn["command"] = self.sec1AutoClick
        self.sec1ModeAutoBtn.grid(column=18, row=2, columnspan=1)

        self.sec1ModeSemiBtn = tk.Button(content, text="Sec 1 SEMI")
        self.sec1ModeSemiBtn["command"] = self.sec1SemiClick
        self.sec1ModeSemiBtn.grid(column=18, row=3, columnspan=1)

        self.sec1ModeManuBtn = tk.Button(content, text="Sec 1 MANU")
        self.sec1ModeManuBtn["command"] = self.sec1ManuClick
        self.sec1ModeManuBtn.grid(column=18, row=4, columnspan=1)

        self.sec2ModeAutoBtn = tk.Button(content, text="Sec 2 AUTO")
        self.sec2ModeAutoBtn["command"] = self.sec1AutoClick
        self.sec2ModeAutoBtn.grid(column=18, row=12, columnspan=1)

        self.sec2ModeSemiBtn = tk.Button(content, text="Sec 2 SEMI")
        self.sec2ModeSemiBtn["command"] = self.sec1SemiClick
        self.sec2ModeSemiBtn.grid(column=18, row=13, columnspan=1)

        self.sec2ModeManuBtn = tk.Button(content, text="Sec 2 MANU")
        self.sec2ModeManuBtn["command"] = self.sec1ManuClick
        self.sec2ModeManuBtn.grid(column=18, row=14, columnspan=1)


    # ==============================================================
    # Others
    # ==============================================================

    def drawApplyButton(self, content):
        # apply button
        self.applyBtn = tk.Button(content, text="Apply")
        self.applyBtn["command"] = self.applyOnClick
        self.applyBtn.grid(column=1, row=20, columnspan=15, ipadx=100)


    

    # ==============================================================
    # Event handlers
    # ==============================================================


    def pv1OnClick(self):
        self.elem1.togglePV(1, True)

    def pv2OnClick(self):
        self.elem1.togglePV(2, True)

    def pv3OnClick(self):
        self.elem1.togglePV(3, True)

    def pv4OnClick(self):
        self.elem1.togglePV(4, True)

    def pv5OnClick(self):
        self.elem1.togglePV(5, True)

    def pv6OnClick(self):
        self.elem1.togglePV(6, True)

    def pv7OnClick(self):
        self.elem1.togglePV(7, True)

    def pv8OnClick(self):
        self.elem1.togglePV(8, True)

    def pv9OnClick(self):
        self.elem1.togglePV(9, True)

    def pv10OnClick(self):
        self.elem1.togglePV(10, True)

    def pv11OnClick(self):
        self.elem1.togglePV(11, True)

    def pv12OnClick(self):
        self.elem1.togglePV(12, True)

    def pv13OnClick(self):
        self.elem1.togglePV(13, True)

    def pv14OnClick(self):
        self.elem1.togglePV(14, True)

    # ---------------------------------

    def pv1OffClick(self):
        self.elem1.togglePV(1, False)

    def pv2OffClick(self):
        self.elem1.togglePV(2, False)

    def pv3OffClick(self):
        self.elem1.togglePV(3, False)

    def pv4OffClick(self):
        self.elem1.togglePV(4, False)

    def pv5OffClick(self):
        self.elem1.togglePV(5, False)

    def pv6OffClick(self):
        self.elem1.togglePV(6, False)

    def pv7OffClick(self):
        self.elem1.togglePV(7, False)

    def pv8OffClick(self):
        self.elem1.togglePV(8, False)

    def pv9OffClick(self):
        self.elem1.togglePV(9, False)

    def pv10OffClick(self):
        self.elem1.togglePV(10, False)

    def pv11OffClick(self):
        self.elem1.togglePV(11, False)

    def pv12OffClick(self):
        self.elem1.togglePV(12, False)

    def pv13OffClick(self):
        self.elem1.togglePV(13, False)

    def pv14OffClick(self):
        self.elem1.togglePV(14, False)

    def pvUpdateClick(self):
        self.updateSetPVPos()
    
    # -----------------------------

    def led1OnClick(self):
        self.elem1.toggleLED(1, True)

    def led2OnClick(self):
        self.elem1.toggleLED(2, True)

    def led3OnClick(self):
        self.elem1.toggleLED(3, True)

    def led4OnClick(self):
        self.elem1.toggleLED(4, True)

    def led5OnClick(self):
        self.elem1.toggleLED(5, True)

    def led6OnClick(self):
        self.elem1.toggleLED(6, True)

    def led7OnClick(self):
        self.elem1.toggleLED(7, True)

    def led8OnClick(self):
        self.elem1.toggleLED(8, True)

    def led9OnClick(self):
        self.elem1.toggleLED(9, True)

    def led10OnClick(self):
        self.elem1.toggleLED(10, True)

    def led11OnClick(self):
        self.elem1.toggleLED(11, True)

    def led12OnClick(self):
        self.elem1.toggleLED(12, True)

    def led13OnClick(self):
        self.elem1.toggleLED(13, True)

    def led14OnClick(self):
        self.elem1.toggleLED(14, True)

    # ---------------------------------

    def led1OffClick(self):
        self.elem1.toggleLED(1, False)

    def led2OffClick(self):
        self.elem1.toggleLED(2, False)

    def led3OffClick(self):
        self.elem1.toggleLED(3, False)

    def led4OffClick(self):
        self.elem1.toggleLED(4, False)

    def led5OffClick(self):
        self.elem1.toggleLED(5, False)

    def led6OffClick(self):
        self.elem1.toggleLED(6, False)

    def led7OffClick(self):
        self.elem1.toggleLED(7, False)

    def led8OffClick(self):
        self.elem1.toggleLED(8, False)

    def led9OffClick(self):
        self.elem1.toggleLED(9, False)

    def led10OffClick(self):
        self.elem1.toggleLED(10, False)

    def led11OffClick(self):
        self.elem1.toggleLED(11, False)

    def led12OffClick(self):
        self.elem1.toggleLED(12, False)

    def led13OffClick(self):
        self.elem1.toggleLED(13, False)

    def led14OffClick(self):
        self.elem1.toggleLED(14, False)

    def LEDUpdateClick(self):
        self.updateSetLEDPos()

    # ----------------------------

    def sec1AutoClick(self):
        self.elem1.changeSectionMode(1,1)

    def sec1SemiClick(self):
        self.elem1.changeSectionMode(1,2)

    def sec1ManuClick(self):
        self.elem1.changeSectionMode(1,3)

    def sec2AutoClick(self):
        self.elem1.changeSectionMode(2,1)

    def sec2SemiClick(self):
        self.elem1.changeSectionMode(2,2)

    def sec2ManuClick(self):
        self.elem1.changeSectionMode(2,3)

    # -------------------------------
    # Pump on/off

    def uipump1OnbuttonClick(self):
        self.elem1.togglePump(1,True)
    
    def uipump1OffbuttonClick(self):
        self.elem1.togglePump(1,False)

    def uipump2OnbuttonClick(self):
        self.elem1.togglePump(2,True)
    
    def uipump2OffbuttonClick(self):
        self.elem1.togglePump(2,False)
    

    # ----------------------------
    # Set pump mode
    # ----------------------------
    
    def uipump1AutobuttonClick(self):
        print("Pump 1 auto mode")
        self.elem1.setPumpMode(1,1)

    def uipump1FlowbuttonClick(self):
        print("Pump 1 flowrate mode")
        self.elem1.setPumpMode(1,2)

    def uipump1HzbuttonClick(self):
        print("Pump 1 speed mode")
        self.elem1.setPumpMode(1,3)

    def uipump2AutobuttonClick(self):
        self.elem1.setPumpMode(2,1)

    def uipump2FlowbuttonClick(self):
        self.elem1.setPumpMode(2,2)

    def uipump2HzbuttonClick(self):
        self.elem1.setPumpMode(2,3)


    def pumpUpdateClick(self):
        self.updatePumpSetting()

    # ----------------------------    

    def uipump1FillDrainModeClick(self):
        self.elem1.setPumpFillDrainMode(1, True)

    def uipump1StaticModeClick(self):
        self.elem1.setPumpFillDrainMode(1, False)

    # ----------------------------    

    def applyOnClick(self):
        self.elem1.apply()



    #-----------------------------

    def updatePumpStatus(self):

        flowrate = self.elem1.getPumpRunningFlowRate(1)
        freq = self.elem1.getPumpRunningRPM(1)
        self.uipump1flowrateFeedback.set(flowrate)
        self.uipump1HzFeedback.set(freq)

        pumpMode = self.elem1.getPumpMode(1)
        if pumpMode == 1:
            self.uipump1ModeFeedback.set("Auto")
        elif pumpMode == 2:
            self.uipump1ModeFeedback.set("Flowrate")
        elif pumpMode == 3:
            self.uipump1ModeFeedback.set("Speed")
        else:
            self.uipump1ModeFeedback.set("Unknown")


        flowrate = self.elem1.getPumpRunningFlowRate(2)
        freq = self.elem1.getPumpRunningRPM(2)
        self.uipump2flowrateFeedback.set(flowrate)
        self.uipump2HzFeedback.set(freq)

        pumpMode = self.elem1.getPumpMode(2)
        if pumpMode == 1:
            self.uipump1ModeFeedback.set("Auto")
        elif pumpMode == 2:
            self.uipump1ModeFeedback.set("Flowrate")
        elif pumpMode == 3:
            self.uipump1ModeFeedback.set("Speed")
        else:
            self.uipump1ModeFeedback.set("Unknown")


    def updateValveStatus(self):
        tmpstr = ""
        for x in range(14):
            valvePos,err = self.elem1.getPVSetting(x + 1)
            tmpstr = tmpstr + str(valvePos)
            tmpstr = tmpstr + ", "
        
        self.uiPVFeedback.set("PV % : "+tmpstr)


    def updateLEDStatus(self):
        tmpstr = ""
        for x in range(14):
            ledPos,err = self.elem1.getLEDSetting(x + 1)
            tmpstr = tmpstr + str(int(ledPos/320))  #convert to %
            tmpstr = tmpstr + ", "
        
        self.uiLEDFeedback.set("LED % : "+tmpstr)
        


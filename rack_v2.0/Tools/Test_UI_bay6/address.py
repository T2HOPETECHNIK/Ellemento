
'''
    Address definitions
    Note that addresses needs to be defined properly. Unfortunately, there is no fix setting yet because the hardware are not available.
'''

REF_RACK_TYPE = 300


CTRL_APPLY_UPDATE_ADDR = 321
CTRL_APPLY_UPDATE_BITPOS = 0

CTRL_SHELF_VALVE_ADDR = 3060        # Valve control (unused)

CTRL_PV_VALUE_OFFSET_ADDR = 4000         # 14 PVs, for manual mode only

CTRL_LIGHT_ON_ADDR = 4080
CTRL_LIGHT_ON_BITPOS = 0                    # 14 bit positions
CTRL_LIGHT_INTENSITY_OFFSET_ADDR = 4085     # 14 light intensity addresses

CTRL_PUMP_MODE_ADDR = 4100                  # 3 pumps max
CTRL_PUMP_RPM_SETPOINT_ADDR = 4105
CTRL_PUMP_FLOWRATE_SETPOINT_ADDR = 4110

CTRL_PUMP_FILL_DRAIN_MODE_ADDR = 4050
CTRL_PUMP_FILL_DRAIN_MODE_BITPOS = 0        # 3 possible pumps
CTRL_PUMP_FILL_MODE_FLOWRATE_ADDR = 4055
CTRL_PUMP_DRAIN_MODE_FLOWRATE = 4060
CTRL_PUMP_FILL_DURATION_ADDR = 4065         # duration in sec
CTRL_PUMP_DRAIN_DURATION_ADDR = 4070

CTRL_PV_ON_ADDR = 4465                   # turn on PV
CTRL_PV_ON_BITPOS = 0                       # Max of 14

CTRL_PUMP_ON_ADDR = 4400                    # max 3
CTRL_PUMP_ON_BITPOS = 0

# Scheduler
CTRL_SCHEDULER_PVON_HH_ADDR = 4500
CTRL_SCHEDULER_PVON_MM_ADDR = 4515
CTRL_SCHEDULER_PVOFF_HH_ADDR = 4530
CTRL_SCHEDULER_PVOFF_MM_ADDR = 4545
CTRL_SCHEDULER_LIGHTON_HH_ADDR = 4560
CTRL_SCHEDULER_LIGHTON_MM_ADDR = 4575
CTRL_SCHEDULER_LIGHTOFF_HH_ADDR = 4590
CTRL_SCHEDULER_LIGHTOFF_MM_ADDR = 4605
CTRL_SCHEDULER_PV_VALUE_ADDR = 4660
CTRL_SCHEDULER_LIGHT_INTENSITY = 4680

CTRL_SECTION_MODE_ADDR = 4460
CTRL_SHELF_USE_SCHEDULER_ADDR = 4620        
CTRL_SHELF_USE_SCHEDULER_BITPOS = 0         # Max of 14


# Feedback
FEEDBACK_LED_ADDR = 4020
FEEDBACK_LED_BITPOS = 0
FEEDBACK_LED_INTENSITY_ADDR = 4022

FEEDBACK_VALVE_SETTING = 4640                   # Max 14

FEEDBACK_PUMP_HZ_ADDR = 4358                     # Max 3
FEEDBACK_PUMP_FLOWRATE_ADDR = 4361               # Max 3

FEEDBACK_FILL_MODE_ADDR = 4076
FEEDBACK_FILL_MODE_BITPOS = 0

FEEDBACK_PV_OFFSET_ADDR = 4640

FEEDBACK_PUMP1_MODE_ADDR = 4750
FEEDBACK_PUMP2_MODE_ADDR = 4751

FEEDBACK_SECTION1_MODE = 4755
FEEDBACK_SECTION2_MODE = 4756

FEEDBACK_PUMP_ABNORMAL_ADDR = 4115
FEEDBACK_PUMP_ERROR_ADDR = 4116

CTRL_PUMP_ABNORMAL_TERMINATION_RESET_ADDR = 4117


CTRL_SHELF_USE_SCHEDULER_ADDR = 4620


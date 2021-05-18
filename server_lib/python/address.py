
'''
    Address definitions
    Note that addresses needs to be defined properly. Unfortunately, there is no fix setting yet because the hardware are not available.
'''

modeAddress = 2500

SHELF_PV_ON_ADDRESS = [ 1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000 ]
SHELF_PV_ON_BITPOS = [ 0,0,0,0,0,0,0,0,0,0,0,0 ]
SHELF_PV_POSITION_ADDRESS = [ 1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000 ]
SHELF_PV_LUT_ADDRESS = [ 1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000 ]
SHELF_LIGHT_ON_ADDRESS = [ 1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000 ]
SHELF_LIGHT_ON_BITPOS = [ 0,0,0,0,0,0,0,0,0,0,0,0 ]
SHELF_LIGHT_INTENSITY_ADDRESS = [ 1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000 ]

PUMP_0_FLOWRATE_ADDRESS = 1000
PUMP_0_FLOWRATE_PER_SHELF_ADDRESS = 1000
PUMP_0_FILL_DRAIN_MODE_ADDRESS = 1000     # Whether pump is in normal mode or it is in Fill-Drain mode
PUMP_0_FILL_DRAIN_MODE_BITPOS = 0
PUMP_0_FILLING_FLAG_ADDRESS = 1000        # Flag for either filling or draining
PUMP_0_FILLING_FLAG_BITPOS = 0
PUMP_0_FILL_VALUE_HZ_ADDRESS = 1000       # Fill value setting
PUMP_0_DRAIN_VALUE_HZ_ADDRESS = 1000      # Drain value setting
PUMP_0_FILL_DURATION_ADDRESS = 3000       # duration setting of fill action
PUMP_0_DRAIN_DURATION_ADDRESS = 3000      # duration setting of drain action
PUMP_0_FILL_DRAIN_TIMER_ADDRESS = 1000    # setting of countdown timer for both fill and drain
PUMP_0_FILL_DRAIN_ACTION_ADDRESS = 1000   # Whether pump is currently filling or draining
PUMP_0_RECOVER_ADDRESS = 1000             # Recover from PID ramp up due to lack of water
PUMP_0_RECOVER_BITPOS = 0                 # bit position (0 = first bit)
PUMP_0_SET_RPM_ADDRESS = 1000             # set rpm value
PUMP_0_CURRENT_RPM_ADDRESS = 1000         # actual reading

PUMP_1_FLOWRATE_ADDRESS = 1000
PUMP_1_FLOWRATE_PER_SHELF_ADDRESS = 1000
PUMP_1_FILL_DRAIN_MODE_ADDRESS = 1000     # Whether pump is in normal mode or it is in Fill-Drain mode
PUMP_1_FILL_DRAIN_MODE_BITPOS = 0
PUMP_1_FILLING_FLAG_ADDRESS = 1000        # Flag for either filling or draining
PUMP_1_FILLING_FLAG_BITPOS = 0
PUMP_1_FILL_VALUE_HZ_ADDRESS = 1000       # Fill value setting
PUMP_1_DRAIN_VALUE_HZ_ADDRESS = 1000      # Drain value setting
PUMP_1_FILL_DURATION_ADDRESS = 3000       # duration setting of fill action
PUMP_1_DRAIN_DURATION_ADDRESS = 3000      # duration setting of drain action
PUMP_1_FILL_DRAIN_TIMER_ADDRESS = 1000    # setting of countdown timer for both fill and drain
PUMP_1_FILL_DRAIN_ACTION_ADDRESS = 1000   # Whether pump is currently filling or draining
PUMP_1_RECOVER_ADDRESS = 1000             # Recover from PID ramp up due to lack of water
PUMP_1_RECOVER_BITPOS = 0                 # bit position (0 = first bit)
PUMP_1_SET_RPM_ADDRESS = 1000             # set RPM value
PUMP_1_CURRENT_RPM_ADDRESS = 1000         # actual reading

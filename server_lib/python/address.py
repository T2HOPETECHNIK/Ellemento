
'''
    Address definitions
    Note that addresses needs to be defined properly. Unfortunately, there is no fix setting yet because the hardware are not available.
'''

modeAddress = 2500

SHELF_PV_ON_ADDRESS = [ 1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000 ]
SHELF_PV_POSITION_ADDRESS = [ 1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000 ]
SHELF_PV_LUT_ADDRESS = [ 1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000 ]
SHELF_LIGHT_ON_ADDRESS = [ 1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000 ]
SHELF_LIGHT_INTENSITY_ADDRESS = [ 1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000 ]

PUMP_FLOWRATE_SET_ADDRESS = 1000
PUMP_FLOWRATE_ADDRESS = 1000
PUMP_FLOWRATE_PER_SHELF_SET_ADDRESS = 1000
PUMP_FLOWRATE_PER_SHELF_ADDRESS = 1000

PUMP_FILL_DRAIN_MODE_ADDRESS = 1000     # Whether pump is in normal mode or it is in Fill-Drain mode
PUMP_FILL_VALUE_HZ_ADDRESS = 1000       # Fill value setting
PUMP_DRAIN_VALUE_HZ_ADDRESS = 1000      # Drain value setting
PUMP_FILL_DURATION_ADDRESS = 3000       # duration setting of fill action
PUMP_DRAIN_DURATION_ADDRESS = 3000      # duration setting of drain action
PUMP_FILL_DRAIN_TIMER_ADDRESS = 1000    # setting of countdown timer for both fill and drain
PUMP_FILL_DRAIN_ACTION_ADDRESS = 1000   # Whether pump is currently filling or draining



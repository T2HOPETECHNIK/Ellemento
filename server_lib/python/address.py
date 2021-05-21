
'''
    Address definitions
    Note that addresses needs to be defined properly. Unfortunately, there is no fix setting yet because the hardware are not available.
'''

modeAddress = 2500

SHELF_PV_ON_ADDRESS = [ 11000,11001,11002,11003,11004,11005,11006,11007,11008,11009,11010,11011 ]
SHELF_PV_ON_BITPOS = [ 0,0,0,0,0,0,0,0,0,0,0,0 ]
SHELF_PV_POSITION_ADDRESS = [ 11012,11013,11014,11015,11016,11017,11018,11019,11020,11021,11022,11023 ]
SHELF_PV_LUT_ADDRESS = [ 11024,11025,11026,11027,11028,11029,11030,11031,11032,11033,11034,11035 ]
SHELF_LIGHT_ON_ADDRESS = [ 11036,11037,11038,11039,11040,11041,11042,11043,11044,11045,11046,11047 ]
SHELF_LIGHT_ON_BITPOS = [ 0,0,0,0,0,0,0,0,0,0,0,0 ]
SHELF_LIGHT_INTENSITY_ADDRESS = [ 11048,11049,11050,11051,11052,11053,11054,11055,11056,11057,11058,11059 ]

PUMP_0_MODE_ADDRESS = 12000
PUMP_0_FLOWRATE_ADDRESS = 11060
PUMP_0_FLOWRATE_PER_SHELF_ADDRESS = 11061
PUMP_0_FILL_DRAIN_MODE_ADDRESS = 11062     # Whether pump is in normal mode or it is in Fill-Drain mode
PUMP_0_FILL_DRAIN_MODE_BITPOS = 0
PUMP_0_FILLING_FLAG_ADDRESS = 11063        # Flag for either filling or draining
PUMP_0_FILLING_FLAG_BITPOS = 0
PUMP_0_FILL_VALUE_HZ_ADDRESS = 11064       # Fill value setting
PUMP_0_DRAIN_VALUE_HZ_ADDRESS = 11065      # Drain value setting
PUMP_0_FILL_DURATION_ADDRESS = 11066       # duration setting of fill action
PUMP_0_DRAIN_DURATION_ADDRESS = 11067      # duration setting of drain action
PUMP_0_FILL_DRAIN_TIMER_ADDRESS = 11068    # setting of countdown timer for both fill and drain
PUMP_0_FILL_DRAIN_ACTION_ADDRESS = 11069   # Whether pump is currently filling or draining
PUMP_0_RECOVER_ADDRESS = 11070             # Recover from PID ramp up due to lack of water
PUMP_0_RECOVER_BITPOS = 0                  # bit position (0 = first bit)
PUMP_0_SET_RPM_ADDRESS = 11071             # set rpm value
PUMP_0_CURRENT_RPM_ADDRESS = 11072         # actual reading

PUMP_1_MODE_ADDRESS = 12001
PUMP_1_FLOWRATE_ADDRESS = 11073
PUMP_1_FLOWRATE_PER_SHELF_ADDRESS = 11074
PUMP_1_FILL_DRAIN_MODE_ADDRESS = 11075     # Whether pump is in normal mode or it is in Fill-Drain mode
PUMP_1_FILL_DRAIN_MODE_BITPOS = 0
PUMP_1_FILLING_FLAG_ADDRESS = 11076        # Flag for either filling or draining
PUMP_1_FILLING_FLAG_BITPOS = 0
PUMP_1_FILL_VALUE_HZ_ADDRESS = 11077       # Fill value setting
PUMP_1_DRAIN_VALUE_HZ_ADDRESS = 11078      # Drain value setting
PUMP_1_FILL_DURATION_ADDRESS = 11079       # duration setting of fill action
PUMP_1_DRAIN_DURATION_ADDRESS = 11080      # duration setting of drain action
PUMP_1_FILL_DRAIN_TIMER_ADDRESS = 11081    # setting of countdown timer for both fill and drain
PUMP_1_FILL_DRAIN_ACTION_ADDRESS = 11082   # Whether pump is currently filling or draining
PUMP_1_RECOVER_ADDRESS = 11083             # Recover from PID ramp up due to lack of water
PUMP_1_RECOVER_BITPOS = 0                  # bit position (0 = first bit)
PUMP_1_SET_RPM_ADDRESS = 11084             # set RPM value
PUMP_1_CURRENT_RPM_ADDRESS = 11085         # actual reading

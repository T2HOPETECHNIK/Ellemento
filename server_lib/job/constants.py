
# For debugging
NO_MODBUS =        True
NO_REST =       True


# Job definitions

JOB_PHASE_1_1 =         1
JOB_PHASE_1_2 =         2
JOB_TRANSPLANT_1 =      3
JOB_PHASE_4_1 =         4
JOB_PHASE_4_2 =         5
JOB_PHASE_4_3 =         6
JOB_TRANSPLANT_2 =      7
JOB_PHASE_5_1 =         8
JOB_PHASE_5_2 =         9
JOB_PHASE_5_3 =         10

task_names = [ \
    "sower_to_1_rack_move",\
    "1_rack_to_2_rack_move",\
    "2_rack_to_3_rack_move",\
    "3_rack_to_3_4_move",\
    "transplant_3_to_4",\
    "3_in_buffer",\
    "wash_tray_3",\
    "washer_to_sower",\
    "foam_inserter",\
    "4_out_buffer",\
    "3-4_to_4_move",\
    "4_to_4_5_move",\
    "buffer_4_in",\
    "transplant_4_to_5",\
    "wash_tray_4",\
    "4_lifter__to_tray",\
    "potting",\
    "lift_tray_pot",\
    "buffer_4",\
    "4_5_to_5_move",\
    "rack_to_harvester_move",\
    "harvester",\
    "wash_tray_5",\
    "washer_to_lifter",\
    "buffer_5",\
    "wash_to_pot"\
    
]

STATUS_CHECK_INTERVAL_SEC = 1

# Timeout period
MOVE_TIMEOUT_S = 300    # 5 min

#====================================
# Errors
#====================================
ERROR_NONE =                0

ERROR_MODBUS_READ_COIL =    1
ERROR_MODBUS_WRITE_COIL =   2

ERROR_REST_FAIL =           100

ERROR_TIMEOUT =             1000



#====================================
# URL and IP
#====================================

REST_URL = "http://127.0.0.1:3000/"

ROBOT_IP = "192.168.1.100"

MEGABOT_IP = "192.168.1.200"

RACK_IP = [ "192.168.1.5",
            "192.168.1.6",
            "192.168.1.7",
            "192.168.1.8",
            "192.168.1.9",
            "192.168.1.10",
            "192.168.1.11",
            "192.168.1.12",
            "192.168.1.13",
            "192.168.1.14",
            "192.168.1.15",
            "192.168.1.16",
            "192.168.1.17",
            "192.168.1.18" ]

#====================================
# Addresses
#====================================

# Server to RC
ADDR_RC_WATCHDOG =                      2000
ADDR_RC_ERROR =                         2001
ADDR_RC_START =                         2002
ADDR_RC_PAUSE =                         2003
ADDR_RC_MEGABOT =                       2004
ADDR_RC_EXTRA1 =                        2046
ADDR_RC_EXTRA2 =                        2048
ADDR_RC_EXTRA3 =                        2050
ADDR_RC_L1_READY_TO_RELEASE =           2100
ADDR_RC_L2_READY_TO_RELEASE =           2104
ADDR_RC_L2_READY_TO_COLLECT =           2106
ADDR_RC_L3_READY_TO_RELEASE =           2108
ADDR_RC_L3_READY_TO_COLLECT =           2110
ADDR_RC_L4_READY_TO_COLLECT =           2112
ADDR_RC_L4_START_FOAMING =              2114
ADDR_RC_L4_NUMBER_OF_TRAYS =            2116

# RC to Server
ADDR_TO_SERVER_WATCHDOG =               1000
ADDR_TO_SERVER_ERROR =                  1001
ADDR_TO_SERVER_WARNING =                1002
ADDR_TO_SERVER_READY_RC =               1003
ADDR_TO_SERVER_RUNNING_RC =             1004
ADDR_TO_SERVER_GEN_ERROR_L1 =           1010
ADDR_TO_SERVER_GEN_ERROR_L2 =           1012
ADDR_TO_SERVER_GEN_ERROR_L3 =           1014
ADDR_TO_SERVER_GEN_ERROR_L4 =           1016
# Power consumption
ADDR_TO_SERVER_VOLTAGE_AVERAGE_Uin =    1020
ADDR_TO_SERVER_VOLTAGE_AVERAGE_UiI =    1022
ADDR_TO_SERVER_CURRENT_AVERAGE =        1024
ADDR_TO_SERVER_ACTIVE_POWER =           1026
ADDR_TO_SERVER_REACTIVE_POWER =         1028
ADDR_TO_SERVER_APPARENT_POWER =         1030
ADDR_TO_SERVER_POWER_FACTOR_A =         1032
ADDR_TO_SERVER_POWER_FACTOR_B =         1034
ADDR_TO_SERVER_POWER_FACTOR_C =         1036
ADDR_TO_SERVER_POWER_FACTOR_TOTAL =     1038
ADDR_TO_SERVER_ENERGY_ACTIVE =          1040
ADDR_TO_SERVER_ENERGY_REACTIVE =        1042
ADDR_TO_SERVER_ENERGY_APPARENT =        1044
ADDR_TO_SERVER_EXTRA_1 =                1046
ADDR_TO_SERVER_EXTRA_2 =                1048
ADDR_TO_SERVER_EXTRA_3 =                1050

ADDR_TO_SERVER_L1_READY_TO_RECEIVE =        1100
ADDR_TO_SERVER_L2_READY_TO_RECEIVE =        1104
ADDR_TO_SERVER_L3_READY_TO_RECEIVE =        1108
ADDR_TO_SERVER_L4_READY_TO_FOAM =           1112
ADDR_TO_SERVER_L4_READY_TO_RELEASE_TRAY =   1114


#==============================================
#  LOCATIONS
#==============================================

LOCATION_SOWER = 0
LOCATION_RACK1 = 1
LOCATION_RACK2 = 2
LOCATION_RACK3 = 3

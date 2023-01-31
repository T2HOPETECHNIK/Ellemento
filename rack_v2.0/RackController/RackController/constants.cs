using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RackController
{

    public struct constants
    {
        public static readonly string[] RACK_PLC_IP = { 
            "192.168.11.5",     //"192.168.1.31"
            "192.168.1.32",
            "192.168.1.33",
            "192.168.1.34",
            "192.168.1.35",
            "192.168.1.36",
            "192.168.1.37",
            "192.168.1.38",
            "192.168.1.39",
            "192.168.1.40",
            "192.168.1.41",
            "192.168.1.42",
            "192.168.1.43",
            "192.168.1.44"
        };

        public static readonly ushort NUM_RACKS = 14;


        public static readonly uint[] NUM_SHELF_PER_RACK = { 12, 12, 12, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, };

        // Modbus addresses

        public static ushort modeAddress = 2500;

        public static readonly ushort[] SHELF_PV_ON_ADDRESS = { 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000 };
        public static readonly ushort[] SHELF_PV_POSITION_ADDRESS = { 1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000 };
        public static readonly ushort[] SHELF_PV_LUT_ADDRESS = { 1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000 };
        public static readonly ushort[] SHELF_LIGHT_ON_ADDRESS = { 1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000 };
        public static readonly ushort[] SHELF_LIGHT_INTENSITY_ADDRESS = { 1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000 };

        public static readonly ushort[] SHELF_LIGHT_SCHED_ON_ADDRESS = { 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000 };
        public static readonly ushort[] SHELF_LIGHT_START_HOUR_ADDRESS = { 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,1000,1000,1000,1000 };
        public static readonly ushort[] SHELF_LIGHT_START_MINUTE_ADDRESS = { 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000 };
        public static readonly ushort[] SHELF_LIGHT_END_HOUR_ADDRESS = { 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000 };
        public static readonly ushort[] SHELF_LIGHT_END_MINUTE_ADDRESS = { 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000 };
        public static readonly ushort[] SHELF_LIGHT_SCHED_INTENSITY_ADDRESS = { 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000 };

        public static readonly ushort[] SHELF_WATER_SCHED_ON_ADDRESS = { 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000 };
        public static readonly ushort[] SHELF_WATER_START_HOUR_ADDRESS = { 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000 };
        public static readonly ushort[] SHELF_WATER_START_MINUTE_ADDRESS = { 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000 };
        public static readonly ushort[] SHELF_WATER_END_HOUR_ADDRESS = { 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000 };
        public static readonly ushort[] SHELF_WATER_END_MINUTE_ADDRESS = { 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000 };
        public static readonly ushort[] SHELF_WATER_SCHED_VALVE_PERCENTAGE_ADDRESS = { 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000 };

        public static readonly ushort[] PUMP_FLOWRATE_SET_ADDRESS = { 1000, 1000 };
        public static readonly ushort[] PUMP_FLOWRATE_ADDRESS = { 1000, 1000 };
        public static readonly ushort[] PUMP_FLOWRATE_PER_SHELF_SET_ADDRESS = { 1000, 1000 };
        public static readonly ushort[] PUMP_FLOWRATE_PER_SHELF_ADDRESS = { 1000, 1000 };

        public static readonly ushort[] PUMP_FILL_DRAIN_MODE_ADDRESS = { 1000, 1000 };     // Whether pump is in normal mode or it is in Fill-Drain mode
        public static readonly ushort[] PUMP_FILL_VALUE_HZ_ADDRESS = { 1000, 1000 };       // Fill value setting
        public static readonly ushort[] PUMP_DRAIN_VALUE_HZ_ADDRESS = { 1000, 1000 };      // Drain value setting
        public static readonly ushort[] PUMP_FILL_DURATION_ADDRESS = { 1000, 1000 };       // duration setting of fill action
        public static readonly ushort[] PUMP_DRAIN_DURATION_ADDRESS = { 1000, 1000 };      // duration setting of drain action
        public static readonly ushort[] PUMP_FILL_DRAIN_TIMER_ADDRESS = { 1000, 1000 };    // setting of countdown timer for both fill and drain
        public static readonly ushort[] PUMP_FILL_DRAIN_ACTION_ADDRESS = { 1000, 1000 };   // Whether pump is currently filling or draining
    }
}

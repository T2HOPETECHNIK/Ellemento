using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FamrRackUI
{
    class Addresses
    {
        public const ushort ADDR_PV_VALUE = 4000;
        public const ushort ADDR_PV_ON = 4465;
        public const ushort ADDR_SECTION_MODE = 4460;
        public const ushort ADDR_LIGHT_ON = 4080;
        public const ushort ADDR_LIGHT_INTENSITY = 4085;
        public const ushort ADDR_PUMP_MODE = 4100;
        public const ushort ADDR_PUMP_FLOWRATE_SETPOINT = 4110;
        public const ushort ADDR_PUMP_ON = 4400;

        public const ushort ADDR_FEEDBACK_FLOWRATE = 4361;
        public const ushort ADDR_FEEDBACK_PUMP_ON = 4655;
        public const ushort ADDR_FEEDBACK_PUMP_MODE = 4750;
        public const ushort ADDR_FEEDBACK_PUMP_SPEED = 4358;    // RPM
        public const ushort ADDR_FEEDBACK_IS_FILLING = 4076;    // Whether it is filling or draining


        public const ushort ADDR_APPLY = 321;

        public const ushort ADDR_USE_SCHEDULER = 4620;

        public const ushort ADDR_WATER_START_SCHEDULE_HH = 4500;
        public const ushort ADDR_WATER_START_SCHEDULE_MM = 4515;
        public const ushort ADDR_WATER_END_SCHEDULE_HH = 4530;
        public const ushort ADDR_WATER_END_SCHEDULE_MM = 4545;

        public const ushort ADDR_LIGHT_START_SCHEDULE_HH = 4560;
        public const ushort ADDR_LIGHT_START_SCHEDULE_MM = 4575;
        public const ushort ADDR_LIGHT_END_SCHEDULE_HH = 4590;
        public const ushort ADDR_LIGHT_END_SCHEDULE_MM = 4605;

        public const ushort ADDR_PUMP_RESET_ABNORMALITY = 4117; // Recover from abnormality

        public const ushort ADDR_PUMP_FILL_DRAIN_MODE = 4050;
        public const ushort ADDR_PUMP_FD_FILL_RATE = 4055;
        public const ushort ADDR_PUMP_FD_DRAIN_RATE = 4060;
        public const ushort ADDR_PUMP_FD_FILL_DURATION = 4065;
        public const ushort ADDR_PUMP_FD_DRAIN_DURATION = 4070;
        



    }
}

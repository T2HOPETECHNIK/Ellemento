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

        public static readonly uint[] NUM_SHELF_PER_RACK = { 14, 14, 14, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12 };

        // Modbus addresses

        public static ushort modeAddress = 2500;


        // Mode:  1 = auto, 2 = semi, 3 = manual

        public static readonly ushort[] SHELF_PV_ON_ADDRESS = { 4465, 4465, 4465, 4465, 4465, 4465, 4465, 4465, 4465, 4465, 4465, 4465, 4465, 4465 };   // per bit
        public static readonly ushort[] SHELF_PV_ON_BITVAL = { 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192 };

        public static readonly ushort[] SHELF_PV_POSITION_ADDRESS = { 4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013 };
        public static readonly ushort[] SHELF_PV_LUT_ADDRESS = { 5120, 5134, 5148, 5162, 5176, 5190, 5204, 5218, 5232, 5246, 5260, 5274, 5288, 5302 };

        public static readonly ushort[] SHELF_LIGHT_ON_ADDRESS = { 4080, 4080, 4080, 4080, 4080, 4080, 4080, 4080, 4080, 4080, 4080, 4080, 4080, 4080 };    // per bit
        public static readonly ushort[] SHELF_LIGHT_ON_BITVAL = { 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192 };

        public static readonly ushort[] SHELF_LIGHT_INTENSITY_ADDRESS = { 4085,4086,4087,4088,4089,4090,4091,4092,4093,4094,4095,4096,4097,4098 };

        public static readonly ushort[] SHELF_WATER_SCHED_ON_ADDRESS = { 4620, 4620, 4620, 4620, 4620, 4620, 4620, 4620, 4620, 4620, 4620, 4620, 4620, 4620 };  // per bit
        public static readonly ushort[] SHELF_WATER_START_HOUR_ADDRESS = { 4500, 4501, 4502, 4503, 4504, 4505, 4506, 4507, 4508, 4509, 4510, 4511, 4512, 4513 };
        public static readonly ushort[] SHELF_WATER_START_MINUTE_ADDRESS = { 4515, 4516, 4517, 4518, 4519, 4520, 4521, 4522, 4523, 4524, 4525, 4526, 4527, 4528 };
        public static readonly ushort[] SHELF_WATER_END_HOUR_ADDRESS = { 4530, 4531, 4532, 4533, 4534, 4535, 4536, 4537, 4538, 4539, 4540, 4541, 4542, 4543 };
        public static readonly ushort[] SHELF_WATER_END_MINUTE_ADDRESS = { 4545, 4546, 4547, 4548, 4549, 4550, 4551, 4552, 4553, 4554, 4555, 4556, 4557 };
        public static readonly ushort[] SHELF_WATER_SCHED_VALVE_PERCENTAGE_ADDRESS = { 4660, 4661, 4662, 4663, 4664, 4665, 4666, 4667, 4668, 4669, 4670, 4671, 4672, 4673 }; 

        public static readonly ushort[] SHELF_LIGHT_SCHED_ON_ADDRESS = { 4620, 4620, 4620, 4620, 4620, 4620, 4620, 4620, 4620, 4620, 4620, 4620, 4620, 4620 };  // per bit
        public static readonly ushort[] SHELF_LIGHT_START_HOUR_ADDRESS = { 4560, 4561, 4562, 4563, 4564, 4565, 4566, 4567, 4568, 4569, 4570, 4571, 4572, 4573 };
        public static readonly ushort[] SHELF_LIGHT_START_MINUTE_ADDRESS = { 4575, 4576, 4577, 4578, 4579, 4580, 4581, 4582, 4583, 4584, 4585, 4586, 4587, 4588 };
        public static readonly ushort[] SHELF_LIGHT_END_HOUR_ADDRESS = { 4590, 4591, 4592, 4593, 4594, 4595, 4596, 4597, 4598, 4599, 4600, 4601, 4602, 4603 };
        public static readonly ushort[] SHELF_LIGHT_END_MINUTE_ADDRESS = { 4605, 4606, 4607, 4608, 4609, 4610, 4611, 4612, 4613, 4614, 4615, 4616, 4617, 4618 };
        public static readonly ushort[] SHELF_LIGHT_SCHED_INTENSITY_ADDRESS = { 4680, 4681, 4682, 4683, 4684, 4685, 4686, 4687, 4688, 4689, 4690, 4691, 4692, 4693 };

        public static readonly ushort[] PUMP_FLOWRATE_SET_ADDRESS = { 4110, 4111 };
        public static readonly ushort[] PUMP_FLOWRATE_PER_SHELF_SET_ADDRESS = { 4364, 4365 };

        public static readonly ushort[] PUMP_FLOWRATE_ADDRESS = { 4361, 4362 };     // Feedback
        public static readonly ushort[] PUMP_FLOWRATE_PER_SHELF_ADDRESS = { 1000, 1000 };   // Feedback

        public static readonly ushort[] PUMP_FILL_DRAIN_MODE_ADDRESS = { 4050, 4050 };     // Whether pump is in normal mode or it is in Fill-Drain mode
        public static readonly ushort[] PUMP_FILL_VALUE_HZ_ADDRESS = { 4055, 4056 };       // Fill value setting
        public static readonly ushort[] PUMP_DRAIN_VALUE_HZ_ADDRESS = { 4060, 4061 };      // Drain value setting
        public static readonly ushort[] PUMP_FILL_DURATION_ADDRESS = { 4065, 4066 };       // duration setting of fill action
        public static readonly ushort[] PUMP_DRAIN_DURATION_ADDRESS = { 4070, 4071 };      // duration setting of drain action

        // Feedback
        public static readonly ushort[] PUMP_FILL_DRAIN_TIMER_ADDRESS = { 4077, 4078 };    // setting of countdown timer for both fill and drain
        public static readonly ushort[] PUMP_FILL_DRAIN_ACTION_ADDRESS = { 4076, 4076 };   // Whether pump is currently filling or draining (bit)


        public static readonly ushort[] SHELF_OVERFLOW_ADDRESS = { 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000 };      // To do: Assignment
        public static readonly ushort[] SHELF_OVERFLOW_BITVAL = { 0, 1,2,3,4,5,6,7,8,9,10,11,12,13 };                   // To do: assigment
    }
}

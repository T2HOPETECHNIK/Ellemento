using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Sockets;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;
using Modbus;
using Modbus.Device;
using Modbus.Extensions.Enron;

namespace RackController
{
    internal class modbusTCP
    {
        ModbusIpMaster master = null;
        TcpClient tcpClient = null;  

        public modbusTCP(string ipAddr)
        {
            tcpClient = new TcpClient();

            init(ipAddr);
        }

        /*
        public void test()
        {
            string ipAddr = "192.168.11.5";
            int tcpPort = 502;

            ushort [] data;

            TcpClient tcpClient = new TcpClient();
            tcpClient.BeginConnect(ipAddr, tcpPort, null, null);

            // Create modbus master device on the tcp client

            ModbusIpMaster master = ModbusIpMaster.CreateIp(tcpClient);

            master.WriteSingleRegister(1001, 55);
            data = master.ReadHoldingRegisters(1005, 5);

            Console.Write(data[0]);

        }
        */


        public void init (string ipAddr)
        {
            int tcpPort = 502;
            
            tcpClient.BeginConnect(ipAddr, tcpPort, null, null);

            master = ModbusIpMaster.CreateIp(tcpClient);
        }

        /*
        public void test2()
        {
            ushort[] data;

            master.WriteSingleRegister(1001, 55);
            data = master.ReadHoldingRegisters(1005, 5);

            Console.Write(data[0]);
        }
        */

        // shelf start at 1, not 0
        public void setLightOn(int shelf, bool bOn)
        {
            ushort addr;

            addr = constants.SHELF_LIGHT_ON_ADDRESS[shelf - 1];
            master.WriteSingleRegister(addr, 1);
        }


        public void setLightIntensity(int shelf, ushort intensity)
        {
            ushort addr;

            addr = constants.SHELF_LIGHT_INTENSITY_ADDRESS[shelf - 1];
            master.WriteSingleRegister(addr, 1);
        }


        public ushort getLightIntensity(int shelf)
        {
            ushort addr;
            ushort[] data;

            addr = constants.SHELF_LIGHT_INTENSITY_ADDRESS[shelf - 1];
            data = master.ReadHoldingRegisters(addr, 1);

            return (data[0]);
        }


        public void setValvePercentage(int shelf, ushort percentage)
        {
            ushort addr;

            if (percentage > 0)
            {
                // on
                addr = constants.SHELF_PV_ON_ADDRESS[shelf - 1];
                master.WriteSingleRegister(addr, 1);
            }
            else
            {
                // off
                addr = constants.SHELF_PV_ON_ADDRESS[shelf - 1];
                master.WriteSingleRegister(addr, 0);
            }

            addr = constants.SHELF_PV_POSITION_ADDRESS[shelf - 1];
            master.WriteSingleRegister(addr, 1);

        }


        public void setLightSchedule(uint shelf, bool bOn, uint startHr, uint startMin, uint endHr, uint endMin, uint intensity)
        {
            ushort addr;

            addr = constants.SHELF_LIGHT_SCHED_ON_ADDRESS[shelf - 1];
            if (bOn)
                master.WriteSingleRegister(addr, 1);
            else
                master.WriteSingleRegister(addr, 0);

            if (bOn)
            {
                addr = constants.SHELF_LIGHT_START_HOUR_ADDRESS[shelf - 1];
                master.WriteSingleRegister(addr, (ushort)startHr);

                addr = constants.SHELF_LIGHT_START_MINUTE_ADDRESS[shelf - 1];
                master.WriteSingleRegister(addr, (ushort)startMin);

                addr = constants.SHELF_LIGHT_END_HOUR_ADDRESS[shelf - 1];
                master.WriteSingleRegister(addr, (ushort)endHr);

                addr = constants.SHELF_LIGHT_END_MINUTE_ADDRESS[shelf - 1];
                master.WriteSingleRegister(addr, (ushort)endMin);

                addr = constants.SHELF_LIGHT_SCHED_INTENSITY_ADDRESS[shelf - 1];
                master.WriteSingleRegister(addr, (ushort)intensity);

            }

        }


        public void setWaterSchedule(uint shelf, bool bOn, uint startHr, uint startMin, uint endHr, uint endMin, uint percentage)
        {
            ushort addr;

            addr = constants.SHELF_WATER_SCHED_ON_ADDRESS[shelf - 1];
            if (bOn)
                master.WriteSingleRegister(addr, 1);
            else
                master.WriteSingleRegister(addr, 0);

            if (bOn)
            {
                addr = constants.SHELF_WATER_START_HOUR_ADDRESS[shelf - 1];
                master.WriteSingleRegister(addr, (ushort)startHr);

                addr = constants.SHELF_WATER_START_MINUTE_ADDRESS[shelf - 1];
                master.WriteSingleRegister(addr, (ushort)startMin);

                addr = constants.SHELF_WATER_END_HOUR_ADDRESS[shelf - 1];
                master.WriteSingleRegister(addr, (ushort)endHr);

                addr = constants.SHELF_WATER_END_MINUTE_ADDRESS[shelf - 1];
                master.WriteSingleRegister(addr, (ushort)endMin);

                addr = constants.SHELF_WATER_SCHED_VALVE_PERCENTAGE_ADDRESS[shelf - 1];
                master.WriteSingleRegister(addr, (ushort)percentage);

            }

        }

    }
}

using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Sockets;
using System.Runtime.CompilerServices;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;
using Modbus;
using Modbus.Device;
using Modbus.Extensions.Enron;
using System.Threading;
using System.Net;
using System.Runtime.InteropServices;

namespace RackController
{
    internal class rackIO
    {
        ModbusIpMaster master = null;
        TcpClient tcpClient = null;
        bool bAvailable;

        string sIPaddress;
        int iTcpPort;

        public rackIO(string ipAddr)
        {
            tcpClient = new TcpClient();
                        
            bAvailable = init(ipAddr);

            sIPaddress = ipAddr;

            if (bAvailable)
            {
                disconnect();
            }
        }

        ~rackIO()
        {
            Console.WriteLine("Destroy instance");
        }


        public void test()
        {
            ushort addr;

            addr = constants.SHELF_PV_ON_ADDRESS[0];

            master.WriteSingleRegister(addr, 1);
        }


        public bool isAvailable()
        {
            return (bAvailable);
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


        public bool init(string ipAddr)
        {
            int tcpPort = 502;
            ulong time_ms = 0;

            
            sIPaddress = ipAddr;
            iTcpPort = tcpPort;
                        
            tcpClient.BeginConnect(sIPaddress, iTcpPort, null, null);

            // wait until connected or timeout
            while ((!tcpClient.Connected) && (time_ms < 2000))
            {
                Thread.Sleep(10);
                time_ms += 10;
            }

            if (time_ms >= 2000)
                return false;

            master = ModbusIpMaster.CreateIp(tcpClient);

            if (master == null)
            {
                //Console.WriteLine("Modbus initialization failed.");
                return false;
            }


            return true;

        }   // init


        void connect()
        {
            ulong time_ms = 0;

            if (tcpClient == null)
            {
                tcpClient = new TcpClient();

                tcpClient.BeginConnect(sIPaddress, iTcpPort, null, null);

                // wait until connected or timeout
                while ((!tcpClient.Connected) && (time_ms < 2000))
                {
                    Thread.Sleep(10);
                    time_ms += 10;
                }

                if (time_ms >= 2000)    //timeout
                    bAvailable = false;
                else
                    bAvailable = true;

                master = ModbusIpMaster.CreateIp(tcpClient);
            }

        }


        void disconnect()
        {
            tcpClient.Close();
            tcpClient.Dispose();
            tcpClient = null;
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
        public void setLightOn(uint shelf, bool bOn)
        {
            ushort addr;

            addr = constants.SHELF_LIGHT_ON_ADDRESS[shelf];
            master.WriteSingleRegister(addr, 1);

        }


        public void setLightIntensity(uint shelf, ushort intensity)
        {
            ushort addr;

            addr = constants.SHELF_LIGHT_INTENSITY_ADDRESS[shelf];
            master.WriteSingleRegister(addr, 1);

        }


        public ushort getLightIntensity(uint shelf)
        {
            ushort addr;
            ushort[] data;

            connect();

            addr = constants.SHELF_LIGHT_INTENSITY_ADDRESS[shelf];
            data = master.ReadHoldingRegisters(addr, 1);

            disconnect();

            return (data[0]);
        }


        public bool getLightStatus(uint shelf)
        {
            // To do
            return (true);
        }


        public void setValvePercentage(uint shelf, ushort percentage)
        {
            ushort addr;
                        
            if (percentage > 0)
            {
                // on
                addr = constants.SHELF_PV_ON_ADDRESS[shelf];
                master.WriteSingleRegister(addr, 1);
            }
            else
            {
                // off
                addr = constants.SHELF_PV_ON_ADDRESS[shelf];
                master.WriteSingleRegister(addr, 0);
            }

            addr = constants.SHELF_PV_POSITION_ADDRESS[shelf];
            master.WriteSingleRegister(addr, 1);

        }


        public ushort getValvePercentage(uint shelf)
        {
            // To do
            return (0);
        }


        public bool getOverflowSensorState(uint shelf)
        {
            return (false);
        }



        public void setLightSchedule(uint shelf, bool bOn, uint startHr, uint startMin, uint endHr, uint endMin, uint intensity)
        {
            ushort addr;

            connect();

            addr = constants.SHELF_LIGHT_SCHED_ON_ADDRESS[shelf];
            if (bOn)
                master.WriteSingleRegister(addr, 1);
            else
                master.WriteSingleRegister(addr, 0);

            if (bOn)
            {
                addr = constants.SHELF_LIGHT_START_HOUR_ADDRESS[shelf];
                master.WriteSingleRegister(addr, (ushort)startHr);

                addr = constants.SHELF_LIGHT_START_MINUTE_ADDRESS[shelf];
                master.WriteSingleRegister(addr, (ushort)startMin);

                addr = constants.SHELF_LIGHT_END_HOUR_ADDRESS[shelf];
                master.WriteSingleRegister(addr, (ushort)endHr);

                addr = constants.SHELF_LIGHT_END_MINUTE_ADDRESS[shelf];
                master.WriteSingleRegister(addr, (ushort)endMin);

                addr = constants.SHELF_LIGHT_SCHED_INTENSITY_ADDRESS[shelf];
                master.WriteSingleRegister(addr, (ushort)intensity);

            }

            disconnect();

        }


        public void setWaterSchedule(uint shelf, bool bOn, uint startHr, uint startMin, uint endHr, uint endMin, uint percentage)
        {
            ushort addr;

            connect();

            addr = constants.SHELF_WATER_SCHED_ON_ADDRESS[shelf];
            if (bOn)
                master.WriteSingleRegister(addr, 1);
            else
                master.WriteSingleRegister(addr, 0);

            if (bOn)
            {
                addr = constants.SHELF_WATER_START_HOUR_ADDRESS[shelf];
                master.WriteSingleRegister(addr, (ushort)startHr);

                addr = constants.SHELF_WATER_START_MINUTE_ADDRESS[shelf];
                master.WriteSingleRegister(addr, (ushort)startMin);

                addr = constants.SHELF_WATER_END_HOUR_ADDRESS[shelf];
                master.WriteSingleRegister(addr, (ushort)endHr);

                addr = constants.SHELF_WATER_END_MINUTE_ADDRESS[shelf];
                master.WriteSingleRegister(addr, (ushort)endMin);

                addr = constants.SHELF_WATER_SCHED_VALVE_PERCENTAGE_ADDRESS[shelf];
                master.WriteSingleRegister(addr, (ushort)percentage);

            }

            disconnect();

        }


        ushort bitVal(ushort bitidx)
        {
            return (ushort)(2 ^ bitidx);
        }

        //=============================================
        //=============================================


        public void setShelfData(uint rackID, uint shelfCount, ref shelfCommandType[] shelfData)
        {
            ushort addr;
            ushort uswater, uslight;

            connect();

            for (uint sid = 0; sid < shelfCount; sid++)
            {
                if (shelfData[sid].bAvailable)
                {
                    setValvePercentage(sid, shelfData[sid].C_valvePercentage);

                    setLightIntensity(sid, shelfData[sid].C_lightIntensity);

                    // Scheduler
                    setWaterSchedule(   
                                        sid,
                                        shelfData[sid].C_waterScheduleOn,
                                        shelfData[sid].C_waterScheduleStartHH,
                                        shelfData[sid].C_waterScheduleStartMM,
                                        shelfData[sid].C_waterScheduleEndHH,
                                        shelfData[sid].C_waterScheduleEndMM,
                                        shelfData[sid].C_waterScheduleValvePercentage
                                    );

                    setLightSchedule(   
                                        sid,
                                        shelfData[sid].C_lightSchedulerOn,
                                        shelfData[sid].C_lightScheduleStartHH,
                                        shelfData[sid].C_lightScheduleStartMM,
                                        shelfData[sid].C_lightScheduleEndHH,
                                        shelfData[sid].C_lightScheduleEndMM,
                                        shelfData[sid].C_lightScheduleIntensity
                                    );

                }   //if

            }   // for

            uswater = 0;
            uslight = 0;
            for (ushort sid = 0; sid < (ushort)shelfCount; sid++)
            {
                if (shelfData[sid].bAvailable)
                {
                    if (shelfData[sid].C_waterOn)
                        uswater = (ushort)(uswater | (ushort)bitVal(sid));

                    if (shelfData[sid].C_lightOn)
                        uslight = (ushort)(uslight | (ushort)bitVal(sid));



                }   // if

            }   // for

            // Update groups

            addr = constants.SHELF_PV_ON_ADDRESS[0];
            master.WriteSingleRegister(addr, uswater);

            addr = constants.SHELF_LIGHT_ON_ADDRESS[0];
            master.WriteSingleRegister(addr, uslight);

            disconnect();

        }


        public void getShelfFeedback(uint sid, ref shelfFeedbackType shelfData)
        {
            shelfData.F_lightIntensity = getLightIntensity(sid);
            shelfData.F_lightOn = getLightStatus(sid);
            shelfData.F_overflow = getOverflowSensorState(sid);
            shelfData.F_valvePercentage = getValvePercentage(sid);
            shelfData.F_waterOn = ((shelfData.F_valvePercentage > 0) ? true : false);

        }

        //=============================================
        //=============================================

        public void setPumpFlowrate(uint pumpID, uint flowrate)
        {
            ushort addr;

            addr = constants.SHELF_LIGHT_INTENSITY_ADDRESS[pumpID];
            master.WriteSingleRegister(addr, 1);

        }


        public ushort getPumpFlowrate(uint pumpID)
        {
            ushort addr;
            ushort[] data;

            connect();

            addr = constants.PUMP_FLOWRATE_ADDRESS[pumpID];
            data = master.ReadHoldingRegisters(addr, 1);

            disconnect();

            return (data[0]);
        }


        public void setPumpData(uint rackID, uint pumpID, ref pumpCommandType pumpData)
        {
            setPumpFlowrate(pumpID, pumpData.C_flowRate);
        }


        public void getPumpFeedback(uint pumpID, ref pumpFeedbackType pumpData)
        {
            pumpData.F_flowrate = getPumpFlowrate(pumpID);
        }

    }
}

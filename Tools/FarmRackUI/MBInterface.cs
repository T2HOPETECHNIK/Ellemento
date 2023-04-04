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

namespace FamrRackUI
{
    class MBInterface
    {
        ModbusIpMaster master = null;
        TcpClient tcpClient = null;
        string sIPaddress;
        int iTcpPort;
        bool bIsConnected;
        ERROR_CODE errCode;

        string[] msgList;
        int arrayIndex;

        string[] readMsgList;
        int arrayIndex2;

        // Buffer (flag holders)
        ushort buf_UseScheduler;
        ushort buf_LightOn;
        ushort buf_PVOn;
        ushort buf_FDModeOn;
        ushort buf_PumpOn;

        public MBInterface(string ip, int port)
        {

            msgList = new string[Constants.MAX_LOG_IN_MEMORY];
            arrayIndex = 0;

            readMsgList = new string[Constants.MAX_LOG_IN_MEMORY];
            arrayIndex2 = 0;

            sIPaddress = ip;
            iTcpPort = port;
            bIsConnected = false;

            if (!connect())
                errCode = ERROR_CODE.ERROR_COMM_ERROR;

        }


        public bool connect()
        {
            ulong time_ms = 0;

            if (tcpClient == null)
            {
                try
                {
                    tcpClient = new TcpClient();

                    tcpClient.BeginConnect(sIPaddress, iTcpPort, null, null);
                }
                catch
                {
                    return (false);
                }

                // wait until connected or timeout
                while ((!tcpClient.Connected) && (time_ms < Constants.TIMEOUT_CNT))
                {
                    Thread.Sleep(10);
                    time_ms += 10;
                }

                if (time_ms >= Constants.TIMEOUT_CNT)    //timeout
                    return (false);

                try
                {
                    master = ModbusIpMaster.CreateIp(tcpClient);

                    updateStates();
                }
                catch
                {
                    return (false);
                }

                bIsConnected = true;

                return (true);
            }

            return (false);

        }


        public void disconnect()
        {
            
        }


        public bool isConnected()
        {
            return (bIsConnected);
        }


        public ERROR_CODE getLastError()
        {
            return (errCode);
        }


        //===============================================

        public void updateStates()
        {
            ushort[] usbuf;

            usbuf = master.ReadHoldingRegisters(Addresses.ADDR_USE_SCHEDULER, 1);
            buf_UseScheduler = usbuf[0];

            usbuf = master.ReadHoldingRegisters(Addresses.ADDR_LIGHT_ON, 1);
            buf_LightOn = usbuf[0];

            usbuf = master.ReadHoldingRegisters(Addresses.ADDR_PV_ON, 1);
            buf_PVOn = usbuf[0];

            usbuf = master.ReadHoldingRegisters(Addresses.ADDR_PUMP_FILL_DRAIN_MODE, 1);
            buf_FDModeOn = usbuf[0];

            usbuf = master.ReadHoldingRegisters(Addresses.ADDR_PUMP_ON, 1);
            buf_PumpOn = usbuf[0];

        }


        // Shelf schedule set to ON/OFF
        public void setScheduleOnOff(ushort index, bool bVal)
        {
            if (master != null)
            {
                buf_UseScheduler = setBit(buf_UseScheduler, index, bVal);
                
                master.WriteSingleRegister(Addresses.ADDR_USE_SCHEDULER, buf_UseScheduler);
                addToMsgList("[" + Addresses.ADDR_USE_SCHEDULER.ToString() + "] <= " + buf_UseScheduler.ToString());
            }
        }   // setScheduleOnOff


        
        private ushort setBit(ushort currentValue, ushort bitPos, bool isSet)
        {
            ushort ustmp;

            ustmp = currentValue;
            if (isSet)
                ustmp |= (ushort) (1 << bitPos);
            else
                ustmp &= (ushort) ~(1 << bitPos);

            return ustmp;
        }   // setBit
        


        // Shelf mode (Auto, Manual, Semi auto)
        public void setMode(ushort index, ushort uVal)
        {
            if (master != null)
            {
                master.WriteSingleRegister((ushort)(Addresses.ADDR_SECTION_MODE + index), uVal);
                addToMsgList("[" + (Addresses.ADDR_SECTION_MODE + index).ToString() + "] <= " + uVal.ToString());
            }
        }


        public void lightControl(ushort index, bool bVal)
        {

            if (master != null)
            {
                buf_LightOn = setBit(buf_LightOn, index, bVal);

                master.WriteSingleRegister(Addresses.ADDR_USE_SCHEDULER, buf_LightOn);
                addToMsgList("[" + Addresses.ADDR_LIGHT_ON.ToString() + "] <= " + buf_LightOn.ToString());
            }
        }


        public void lightIntensityControl(ushort index, ushort uval)
        {
            if (master != null)
            {
                master.WriteSingleRegister((ushort)(Addresses.ADDR_LIGHT_INTENSITY + index), uval);
                addToMsgList("[" + (Addresses.ADDR_LIGHT_INTENSITY + index).ToString() + "] <= " + uval.ToString());
            }
        }
                
        public void pumpControl(ushort index, bool bVal)
        {
            if (master != null)
            {
                buf_PumpOn = setBit(buf_PumpOn, index, bVal);
                master.WriteSingleRegister(Addresses.ADDR_PUMP_ON, buf_PumpOn);
                addToMsgList("[" + Addresses.ADDR_PUMP_ON.ToString() + "] <= " + buf_PumpOn.ToString());
            }
        }

        public void pumpModeControl(ushort index, bool bval)
        {
            ushort uval = (ushort)Math.Pow(2, index);
            ushort uOut;

            if (master != null)
            {
                uOut = (ushort)((bval) ? uval : 0);
                master.WriteSingleRegister(Addresses.ADDR_PUMP_MODE, uOut);
                addToMsgList("[" + Addresses.ADDR_PUMP_MODE.ToString() + "] <= " + uOut.ToString());
            }


        }

        public void applyControl()
        {
            if (master != null)
            {
                master.WriteSingleRegister(Addresses.ADDR_APPLY, 1);
                addToMsgList("[" + Addresses.ADDR_APPLY.ToString() + "] <= 1");
            }
        }


        public void setValveOnOff(ushort index, bool bVal)
        {

            if (master != null)
            {
                buf_PVOn = setBit(buf_PVOn, index, bVal);

                master.WriteSingleRegister((ushort)(Addresses.ADDR_PV_ON + index), buf_PVOn);
                addToMsgList("[" + Addresses.ADDR_PV_ON.ToString() + "] <= " + buf_PVOn.ToString());
            }
        }


        public void setValve(ushort index, ushort ival)
        {
            if (master != null)
            {
                master.WriteSingleRegister((ushort)(Addresses.ADDR_PV_VALUE + index), ival);
                addToMsgList("[" + (Addresses.ADDR_PV_VALUE + index).ToString() + "] <= " + ival.ToString());
            }
        }


        public void setPumpFlowRate(int index, ushort ival)
        {
            if (master != null) { 
                master.WriteSingleRegister((ushort)(Addresses.ADDR_PUMP_FLOWRATE_SETPOINT + index), ival);
                addToMsgList("[" + (Addresses.ADDR_PUMP_FLOWRATE_SETPOINT + index).ToString() + "] <= " + ival.ToString());
            }
        }

        private string[] splitSchedule(string s)
        {
            int index;
            string[] sout = new string[4];

            index = 0;
            string[] stmp = s.Split('-');
            
            foreach(var word in stmp)
            {
                string[] stmp2 = word.Split(':');
                foreach(var stmp3 in stmp2)
                {
                    sout[index] = stmp3;
                    index++;
                }
            }

            return (sout);
        }


        public void setWaterSchedule(int index, string sval)
        {
            string[] s = splitSchedule(sval);
            ushort address = 0;
            bool bAddrSet = false;
            ushort uval;

            for(int itmp = 0; itmp < 4; itmp++)
            {

                switch(itmp)
                {
                    case 0:
                        address = (ushort)(Addresses.ADDR_WATER_START_SCHEDULE_HH + index);
                        bAddrSet = true;
                        break;
                    case 1:
                        address = (ushort)(Addresses.ADDR_WATER_START_SCHEDULE_MM + index);
                        bAddrSet = true;
                        break;
                    case 2:
                        address = (ushort)(Addresses.ADDR_WATER_END_SCHEDULE_HH + index);
                        bAddrSet = true;
                        break;
                    case 3:
                        address = (ushort)(Addresses.ADDR_WATER_END_SCHEDULE_MM + index);
                        bAddrSet = true;
                        break;
                }   //switch

                if (bAddrSet) {
                    uval = (ushort)ushort.Parse(s[itmp]);
                    if (master != null)
                    {
                        master.WriteSingleRegister((ushort)address, uval);
                        addToMsgList("[" + address.ToString() + "] <= " + uval);
                    }
                }


            }   //for

        }

        public void setLightSchedule(int index, string sval)
        {
            string[] s = splitSchedule(sval);
            ushort address = 0;
            bool bAddrSet = false;
            ushort uval;

            for (int itmp = 0; itmp < 4; itmp++)
            {
                switch (itmp)
                {
                    case 0:
                        address = (ushort)(Addresses.ADDR_LIGHT_START_SCHEDULE_HH + index);
                        break;
                    case 1:
                        address = (ushort)(Addresses.ADDR_LIGHT_START_SCHEDULE_MM + index);
                        break;
                    case 2:
                        address = (ushort)(Addresses.ADDR_LIGHT_END_SCHEDULE_HH + index);
                        break;
                    case 3:
                        address = (ushort)(Addresses.ADDR_LIGHT_END_SCHEDULE_MM + index);
                        break;
                }   //switch

                if (bAddrSet)
                {
                    uval = (ushort)ushort.Parse(s[itmp]);
                    if (master != null)
                    {
                        master.WriteSingleRegister((ushort)address, uval);
                        addToMsgList("[" + address.ToString() + "] <= " + uval);
                    }
                }

            }   //for
        }


        public void fillDrainControl(ushort index, bool bVal)
        {
            if (master != null)
            {
                buf_FDModeOn = setBit(buf_FDModeOn, index, bVal);
                master.WriteSingleRegister((ushort)(Addresses.ADDR_PUMP_FILL_DRAIN_MODE + index), buf_FDModeOn);
                addToMsgList("[" + Addresses.ADDR_PUMP_FILL_DRAIN_MODE.ToString() + "] <= " + buf_FDModeOn.ToString());
            }
        }


        public void setFillDuration(ushort index, ushort iValue)
        {
            if (master != null)
            {
                master.WriteSingleRegister((ushort)(Addresses.ADDR_PUMP_FD_FILL_DURATION + index), iValue);
                addToMsgList("[" + Addresses.ADDR_PUMP_FD_FILL_DURATION.ToString() + "] <= " + iValue.ToString());
            }
        }


        public void setDrainDuration(ushort index, ushort iValue)
        {
            if (master != null)
            {
                master.WriteSingleRegister((ushort)(Addresses.ADDR_PUMP_FD_DRAIN_DURATION + index), iValue);
                addToMsgList("[" + Addresses.ADDR_PUMP_FD_DRAIN_DURATION.ToString() + "] <= " + iValue.ToString());
            }
        }

        public void setFillRate(ushort index, ushort iValue)
        {
            if (master != null)
            {
                master.WriteSingleRegister((ushort)(Addresses.ADDR_PUMP_FD_FILL_RATE + index), iValue);
                addToMsgList("[" + Addresses.ADDR_PUMP_FD_FILL_RATE.ToString() + "] <= " + iValue.ToString());
            }
        }


        public void setDrainRate(ushort index, ushort iValue)
        {
            if (master != null)
            {
                master.WriteSingleRegister((ushort)(Addresses.ADDR_PUMP_FD_DRAIN_RATE + index), iValue);
                addToMsgList("[" + Addresses.ADDR_PUMP_FD_DRAIN_RATE.ToString() + "] <= " + iValue.ToString());
            }
        }



        public void recoverPumpClick(int index)
        {
            ushort uval = (ushort)Math.Pow(2, index);
            if (master != null)
            {
                master.WriteSingleRegister(Addresses.ADDR_PUMP_RESET_ABNORMALITY, uval);
                addToMsgList("[" + Addresses.ADDR_PUMP_RESET_ABNORMALITY.ToString() + "] <= " + uval.ToString());
            }
        }

        //================================================

        // Common function for reading pump ushort data
        public ushort[] getPumpUSCommonData(ushort addr)
        {
            ushort[] usfr = new ushort[2];
            string stmp;

            if (master != null)
            {
                usfr = master.ReadHoldingRegisters((ushort)(addr), 2);

                stmp = "[" + addr.ToString() + "] => ";
                for (int i = 0; i < 2; i++)
                {
                    stmp = stmp + "[" + usfr[i].ToString() + "]";
                }
                addToMsgList2(stmp);

            }   // if

            return (usfr);

        }   // getPumpUSCommonData


        public bool[] getPumpBoolCommonData(ushort addr)
        {
            bool[] bPs = new bool[2];
            ushort[] ustmp;
            string stmp;

            if (master != null)
            {
                ustmp = master.ReadHoldingRegisters((ushort)(addr), 1);

                bPs[0] = false;
                bPs[1] = false;


                if ((ustmp[0] & 1) == 1)
                    bPs[0] = true;

                if ((ustmp[0] & 2) == 2)
                    bPs[1] = true;

                stmp = "[" + addr.ToString() + "] => " + ustmp[0].ToString();
                addToMsgList2(stmp);

            }   // if

            return (bPs);
        }   //getPumpBoolCommonData



        public ushort[] getPumpFlowrateFeedback()
        {
            ushort[] usfr = new ushort[2];
            
            usfr = getPumpUSCommonData(Addresses.ADDR_FEEDBACK_FLOWRATE);

            return (usfr);
        }


        public bool[] getPumpOnStatus()
        {
            bool[] bPs = new bool[2];

            bPs = getPumpBoolCommonData(Addresses.ADDR_FEEDBACK_PUMP_ON);

            return (bPs);
        }


        public ushort[] getPumpSpeed()
        {
            ushort[] usfr = new ushort[2];

            usfr = getPumpUSCommonData(Addresses.ADDR_FEEDBACK_PUMP_SPEED);

            return (usfr);
        }


        public bool[] getPumpIsFilling()
        {
            bool[] btmp = new bool[2];

            btmp = getPumpBoolCommonData(Addresses.ADDR_FEEDBACK_IS_FILLING);

            return (btmp);
        }


        //====================================================
        // Logs
        //====================================================


        private void addToMsgList(string s)
        {
            if (arrayIndex < msgList.Length-1)
            {
                msgList[arrayIndex] = s;
                arrayIndex++;
            }
        }


        public string[] getMessageList()
        {
            return (msgList);
        }

        public void clearMessageList()
        {
            Array.Clear(msgList, 0, msgList.Length);
            arrayIndex = 0;
        }



        private void addToMsgList2(string s)
        {
            if (arrayIndex < msgList.Length - 1)
            {
                readMsgList[arrayIndex2] = s;
                arrayIndex2++;
            }
        }


        public string[] getMessageList2()
        {
            return (readMsgList);
        }

        public void clearMessageList2()
        {
            Array.Clear(readMsgList, 0, readMsgList.Length);
            arrayIndex2 = 0;
        }

    }   // MBInterface
}

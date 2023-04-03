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

namespace ControlUI
{
    class comInterface
    {

        ModbusIpMaster master = null;
        TcpClient tcpClient = null;
        string sIPaddress;
        int iTcpPort;
        bool isConnected;
        ERROR_CODE errCode;
        ulong TIMEOUT_CNT = 5000;


        public comInterface(string ipAddr, int port)
        {

            sIPaddress = ipAddr;
            iTcpPort = port;
            isConnected = false;
            errCode = 0;

            tcpClient = new TcpClient();

            isConnected = init(ipAddr);

            if (!isConnected)
            {
                disconnect();
            }
        }

        ~comInterface()
        {
            Console.WriteLine("Destroy instance");
        }



        public bool init(string ipAddr)
        {
            int loctcpPort = iTcpPort;
            //ulong time_ms = 0;
            bool bres;

            tcpClient = new TcpClient();

            sIPaddress = ipAddr;

            bres = initcomm(sIPaddress, loctcpPort);
            return (bres);
        }   // init



        private bool checkConnection()
        {
            ushort usRes;
            usRes = getRegister(0);
            if (errCode != 0)
                return (false);
            else
                return (true);
        }


        public bool connect()
        {
            bool bres;

            if (!checkConnection())
            {
                bres = initcomm(sIPaddress, iTcpPort);
                return (bres);
            }
            else
            {
                return (true);
            }
        }


        private bool initcomm(string iIPAddr, int iPort) { 
            ulong time_ms = 0;

            if (tcpClient == null)
            {
                try
                {
                    tcpClient = new TcpClient();

                    tcpClient.BeginConnect(iIPAddr, iPort, null, null);
                }
                catch
                {
                    return (false);
                }

                // wait until connected or timeout
                while ((!tcpClient.Connected) && (time_ms < TIMEOUT_CNT))
                {
                    Thread.Sleep(10);
                    time_ms += 10;
                }

                if (time_ms >= TIMEOUT_CNT)    //timeout
                    return (false);

                try { 
                    master = ModbusIpMaster.CreateIp(tcpClient);
                }
                catch
                {
                    return (false);
                }

                return (true);
            }

            return (false);

        }


        public bool isAvailable()
        {
            return (isConnected);
        }



        public void disconnect()
        {

            isConnected = false;

            tcpClient.Close();
            tcpClient.Dispose();
            tcpClient = null;
        }



        public void setRegister(ushort addr, ushort value)
        {
            try
            {
                if (master != null)
                {
                    master.WriteSingleRegister(addr, value);
                    errCode = ERROR_CODE.ERROR_NONE;
                }
            }
            catch(Exception e)
            {
                // Error handler
                Console.WriteLine(e.ToString());
                errCode = ERROR_CODE.ERROR_COMM_FAIL;
            }
        }



        public ushort getRegister(ushort addr)
        {
            ushort[] usarray;
            ushort usout;

            try
            {
                if (master != null)
                {
                    usarray = master.ReadHoldingRegisters(addr, 1);
                    errCode = ERROR_CODE.ERROR_NONE;
                }
                else
                {
                    errCode = ERROR_CODE.ERROR_COMM_FAIL;
                    return (0);
                }
            }
            catch
            {
                errCode = ERROR_CODE.ERROR_COMM_FAIL;
                return (0);
            }

            usout = usarray[0];
            return (usout);
        }


        private ushort binaryValue(ushort bitpos)
        {
            return ((ushort)(32768 >> (15 - bitpos)));
        }



        public void setCoil(ushort addr, ushort bitpos, bool bval)
        {
            ushort ustmp;
            ushort bitval;

            ustmp = getRegister(addr);

            bitval = binaryValue(bitpos);

            if (bval)
                ustmp |= bitval;
            else
                ustmp = (ushort)(ustmp ^ bitval);

            try
            {
                if (master != null)
                    master.WriteSingleRegister(addr, ustmp);
            }
            catch
            {
                errCode = ERROR_CODE.ERROR_COMM_FAIL;
            }
        }


        public bool getCoil(ushort addr, ushort bitpos)
        {

            ushort[] usarray;
            ushort usout;
            bool btmp = false;

            try
            {
                if (master != null)
                {
                    usarray = master.ReadHoldingRegisters(addr, 1);
                    usout = usarray[0];

                    if ((usout & binaryValue(bitpos)) != 0)
                        btmp = true;
                    else
                        btmp = false;
                }
            }
            catch 
            {

                errCode = ERROR_CODE.ERROR_COMM_FAIL;

                return (false);
            }

            return (btmp);
        }


        public ERROR_CODE getError()
        {
            return (errCode);
        }


        /*

        public void setCoil(ushort addr, ushort bitpos, bool bval)
        {
            master.WriteSingleCoil(addr, bval);
        }


        public bool getCoil(ushort addr, ushort bitpos)
        {

            bool[] bres = master.ReadCoils(addr, 1);

            return (bres[0]);
        }
        */


    }   // class

}   // namespace


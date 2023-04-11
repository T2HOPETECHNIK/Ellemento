using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;
using System.IO;

namespace ControlUI
{
    class scriptHandler
    {
        string errorMsg;

        string[] scriptLine = new string[1024];
        int iScriptNumLines, iScriptIndex;

        public string getError()
        {
            return (errorMsg);
        }


        void addToQueue(string s)
        {
            scriptLine[iScriptIndex] = s;
            iScriptIndex++;

            iScriptNumLines = iScriptIndex;
        }


        // Execute instructions in the queue
        public void executeScriptLines(comInterface mbcom)
        {
            int i = 0;
            string stmp;

            while (i < iScriptNumLines)
            {
                stmp = interpretLine(scriptLine[i], mbcom);
                
                i++;
            }
        }   // executeScript


        public void resetPointer()
        {
            iScriptIndex = 0;
        }


        public bool executeOneLine(comInterface mbcom, ref string msg)
        {
            string strtmp;

            if (iScriptIndex < iScriptNumLines)
            {
                strtmp = interpretLine(scriptLine[iScriptIndex], mbcom);
                iScriptIndex++;
                msg = strtmp;
                return (true);
            }
            else
            {
                msg = "";
                return (false);
            }
        }


        // read script file and add to queue
        public void ProcessScript(string filename)
        {
            int lineCount = 0;
            string stmp = "";

            errorMsg = "";

            if (File.Exists(filename))
            {

                try
                {
                    // Reads file line by line
                    System.IO.StreamReader Textfile = new StreamReader(filename);
                    string line;

                    while ((line = Textfile.ReadLine()) != null)
                    {
                        if (line != "")
                        {
                            lineCount++;
                            addToQueue(line);
                        }   // if
                                                
                    }   //while

                }
                catch
                {
                    errorMsg = "Script failed";
                }


                resetPointer();

            }   //if
                
        }   //Runscript


        private ushort getBitAddr(string dotaddr)
        {
            string[] strarray = dotaddr.Split(".");
            ushort ustmp;

            ustmp = (ushort) Int32.Parse(strarray[0]);
            return (ustmp);
        }


        private ushort getBitPos(string dotaddr)
        {
            string[] strarray = dotaddr.Split(".");
            ushort ustmp;

            ustmp = (ushort)Int32.Parse(strarray[1]);
            return (ustmp);
        }


        private string interpretLine(string strline, comInterface mbcom)
        {
            string keyword = "";
            string strtmp;
            
            string[] strParams = new string[10];
            int counter = 0;
            ushort address, value, targetValue;
            ushort bitpos;
            ushort usTimeout;
            bool bres;
            ushort uvalue;
            string strResult = "";

            if (strline == "")
                return (strResult);

            string[] strArray = strline.Split(' ');

            foreach (var tag in strArray)
            {
                strtmp = tag.ToUpper();
                if ((strtmp == "WAIT") ||
                    (strtmp == "WAITBIT") ||
                    (strtmp == "SET") ||
                    (strtmp == "GET") ||
                    (strtmp == "SETBIT") ||
                    (strtmp == "GETBIT"))
                {
                    keyword = strtmp;
                }

                if (keyword != "")
                {
                    if ((tag != "") && (tag != keyword))
                    {
                        strParams[counter] = tag;
                        counter++;
                    }
                }
            }   // foreach

            if (keyword == "WAIT")
            {
                address = (ushort)Int32.Parse(strParams[0]);
                targetValue = (ushort)Int32.Parse(strParams[1]);
                usTimeout = (ushort)Int32.Parse(strParams[2]);

                do
                {
                    value = mbcom.getRegister(address);
                    if (value != targetValue)
                    {
                        Thread.Sleep(1000);
                    }

                } while (value != targetValue);

                strResult = strParams[0] + " = " + targetValue.ToString();

            }   //wait

            if (keyword == "WAITBIT")
            {
                address = getBitAddr(strParams[0]);
                bitpos = getBitPos(strParams[0]);

                targetValue = (ushort)Int32.Parse(strParams[1]);
                usTimeout = (ushort)Int32.Parse(strParams[2]);

                do
                {
                    bres = mbcom.getCoil(address, bitpos);
                    if (bres != (targetValue == 1))
                        Thread.Sleep(1000);

                } while (bres != (targetValue == 1));

                strResult = strParams[0] + " = " + targetValue.ToString() + "b";
            }   //waitbit

            if (keyword == "SET")
            {
                address = (ushort)Int32.Parse(strParams[0]);
                value = (ushort)Int32.Parse(strParams[1]);

                mbcom.setRegister(address, value);

                strResult = strParams[0] + " <= " + value.ToString();
            }

            if (keyword == "GET")
            {
                address = (ushort)Int32.Parse(strParams[0]);
                uvalue = mbcom.getRegister(address);

                strResult = strParams[0] + " => " + uvalue.ToString();
            }

            if (keyword == "SETBIT")
            {
                address = getBitAddr(strParams[0]);
                bitpos = getBitPos(strParams[0]);
                value = (ushort)Int32.Parse(strParams[1]);
                mbcom.setCoil(address, bitpos, ((value==1)? true:false));

                strResult = strParams[0] + " <= " + value.ToString();
            }

            if (keyword == "GETBIT")
            {
                address = getBitAddr(strParams[0]);
                bitpos = getBitPos(strParams[0]);
                bres = mbcom.getCoil(address, bitpos);

                strResult = strParams[0] + ": " + (bres? "True": "False");
            }


            return (strResult);

        }   // interpret line

    }
}

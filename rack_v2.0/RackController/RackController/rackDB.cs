using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Data;
using System.Data.SqlClient;
using System.Linq;
using System.Threading.Tasks;
using System.Data.Common;

namespace RackController
{
    internal class rackDB
    {

        SqlConnection conn;

        public void test()
        {
            string connetionString;
            SqlConnection cnn;
            //connetionString = @"Data Source=143.198.222.246;Initial Catalog=ellemento;User ID=sa;Password=Hope@608614";
            connetionString = @"Data Source=localhost;Initial Catalog=ellementoRacks;User ID=sa;Password=password";
            cnn = new SqlConnection(connetionString);
            cnn.Open();

            Console.Write("Connection Open  !");
            
            SqlCommand cmd;
            SqlDataReader dataReader;
            String sql, output = "", output2 = "";

            sql = "Select * from rackInfo";
            cmd = new SqlCommand(sql, cnn);
            dataReader = cmd.ExecuteReader();

            while (dataReader.Read())
            {
                output = output + dataReader.GetValue(0);
            }

            Console.Write(output);

            dataReader.Close();


            sql = "Select * from shelfFeedback";
            cmd = new SqlCommand(sql, cnn);
            dataReader = cmd.ExecuteReader();

            while (dataReader.Read())
            {
                output2 = output2 + dataReader.GetValue(0);
            }

            Console.Write(output2);


            cnn.Close();
        }


        public rackDB()
        {
            string connectionString;
            
            //connectionString = @"Data Source=143.198.222.246;Initial Catalog=ellemento;User ID=sa;Password=Hope@608614";
            connectionString = @"Data Source=localhost;Initial Catalog=ellementoRacks;User ID=sa;Password=password";
            conn = new SqlConnection(connectionString);
            conn.Open();
            if (isValidConnection())
            {
                Console.WriteLine("DB connection established");
            }
            else
            {
                Console.WriteLine("DB connection failed!");
            }
        }


        ~rackDB()
        {
            conn.Close();
        }


        bool isValidConnection()
        {
            if (conn != null)
            {
                if (conn.State == ConnectionState.Closed)
                {
                    Console.WriteLine("Connection is closed");
                    return false;
                }
                else
                {
                    Console.WriteLine("Connection is open");
                    return true;
                }
            }
            else
            {
                Console.WriteLine("Connection is null");
                return false;
            }
        }


        ushort getHH(uint s)
        {
            // To do
            return (8);
        }

        ushort getMM(uint s)
        {
            // To do
            return (0);
        }





        public void getRackInfo(uint rackID, ref rackType rack)
        {
            SqlCommand cmd;
            SqlDataReader dataReader;
            String sql, output = "";
            uint id;

            if (!isValidConnection())
            {
                Console.WriteLine("SQL disconnected");
                return;
            }

            id = rackID + 1;


            sql = "Select top 1 * from ellementoRacks.dbo.rackInfo where rackID=" + id.ToString();   // only one, duplicate entry will be ignored
            cmd = new SqlCommand(sql, conn);
            dataReader = cmd.ExecuteReader();
            if (dataReader.Read())
            {
                rack.bAvailable = (bool) dataReader.GetBoolean(4);
                rack.numShelf = (ushort) dataReader.GetInt32(5);
                rack.numPump = (ushort) dataReader.GetInt32(6);
            }

            dataReader.Close();



        }


        public void getRackUpdateList(ref bool[] changelist)
        {
            SqlCommand cmd;
            SqlDataReader dataReader;
            String sql;
            ushort index;

            for (int i = 0; i < constants.NUM_RACKS; i++)
                changelist[i] = false;

            sql = "Select rackID from ellementoRacks.dbo.rackInfo where isDataUpdated=1";   // only one, duplicate entry will be ignored
            cmd = new SqlCommand(sql, conn);
            dataReader = cmd.ExecuteReader();
            while (dataReader.Read())
            {
                index = (ushort) dataReader.GetInt32(0);
                changelist[index - 1] = true;       // rackID starts with 1 while our index starts with zero
            }

            dataReader.Close();
        }





        public bool readShelfData(uint rackID, uint shelfID, ref shelfCommandType sdata)
        {
            SqlCommand cmd;
            SqlDataReader dataReader;
            String sql, output = "";
            shelfCommandType outShelfData;
            bool bRecordFound = false;
            uint rid = rackID + 1;
            uint sid = shelfID + 1;
            UInt32 uitmp;
            TimeSpan ts;


            sql = "select top 1 * from ellementoRacks.dbo.shelfController where rackID=" + rid.ToString() + " and shelfID=" + sid.ToString() ;   // only one, duplicate entry will be ignored
            cmd = new SqlCommand(sql, conn);
            dataReader = cmd.ExecuteReader();

            while (dataReader.Read())
            {
                sdata.bAvailable = true;

                sdata.C_mode = (ushort)dataReader.GetInt32(4);

                //output = output + "," + dataReader.GetValue(0);
                sdata.C_lightOn = (bool)dataReader.GetBoolean(5);             // lightOn
                sdata.C_lightIntensity = (ushort) dataReader.GetInt32(6);      // lightIntensity
                sdata.C_valvePercentage = (ushort) dataReader.GetInt32(7);     // valve percentage
                sdata.C_lightSchedulerOn = (bool)dataReader.GetBoolean(8);    // light scheduler on

                ts = dataReader.GetTimeSpan(9);
                sdata.C_lightScheduleStartHH = (ushort)ts.Hours;
                sdata.C_lightScheduleStartMM = (ushort)ts.Minutes;
                ts = dataReader.GetTimeSpan(10);
                sdata.C_lightScheduleEndHH = (ushort)ts.Hours;
                sdata.C_lightScheduleEndMM = (ushort)ts.Minutes;

                sdata.C_lightScheduleIntensity = (ushort)dataReader.GetInt32(11);
                sdata.C_waterScheduleOn = (bool)dataReader.GetBoolean(12);    // water scheduler on

                ts = dataReader.GetTimeSpan(13);
                sdata.C_waterScheduleStartHH = (ushort)ts.Hours;
                sdata.C_waterScheduleStartMM = (ushort)ts.Minutes;
                ts = dataReader.GetTimeSpan(14);
                sdata.C_waterScheduleEndHH = (ushort)ts.Hours;
                sdata.C_waterScheduleEndMM = (ushort)ts.Minutes;

                sdata.C_waterScheduleValvePercentage = (ushort)dataReader.GetInt32(15);

                bRecordFound = true;
            }   // while

            dataReader.Close();

            return bRecordFound;

        }   // readShelfData


        public bool setShelfData(uint rackID, uint shelfID, ref shelfFeedbackType shelfData)
        {
            SqlCommand cmd;
            String sql = "";
            uint rid = rackID + 1;
            uint sid = shelfID + 1;
            int res;

            sql = "update ellementoRacks.dbo.shelfFeedback set" +
                                            " shelfID=" + sid.ToString() +
                                            ", rackID=" + rid.ToString() +
                                            ", lightOn=" + (shelfData.F_lightOn ? "1" : "0") +
                                            ", lightIntensity=" + shelfData.F_lightIntensity.ToString() +
                                            ", valveSetting=" + shelfData.F_valvePercentage.ToString() +
                                            ", waterOn=" + (shelfData.F_waterOn ? "1" : "0") +
                                            " where shelfID=" + sid.ToString() + " and rackID=" + rid.ToString();

            cmd = new SqlCommand(sql, conn);

            res = cmd.ExecuteNonQuery();

            if (res < 1)
                return (false);
            else
                return (true);

        }

    }
}

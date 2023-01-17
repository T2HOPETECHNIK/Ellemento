using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Data;
using System.Data.SqlClient;
using System.Linq;
using System.Threading.Tasks;

namespace RackController
{
    internal class rackDB
    {

        SqlConnection cnn;

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
            String sql, output = "";

            sql = "Select * from rackInfo";
            cmd = new SqlCommand(sql, cnn);
            dataReader = cmd.ExecuteReader();

            while (dataReader.Read())
            {
                output = output + dataReader.GetValue(0);
            }

            Console.Write(output);
            

            cnn.Close();
        }


        public rackDB()
        {
            string connectionString;
            
            //connetionString = @"Data Source=143.198.222.246;Initial Catalog=ellemento;User ID=sa;Password=Hope@608614";
            connectionString = @"Data Source=localhost;Initial Catalog=ellementoRacks;User ID=sa;Password=password";
            cnn = new SqlConnection(connectionString);
            cnn.Open();

        }

        uint getHH(string s)
        {
            // To do
            return (8);
        }

        uint getMM(string s)
        {
            // To do
            return (0);
        }


        public bool readShelfData(uint rackID, uint shelfID, ref shelfType sdata)
        {
            SqlCommand cmd;
            SqlDataReader dataReader;
            String sql, output = "";
            shelfType outShelfData;
            bool bRecordFound = false;

            sql = "Select * from shelfController where rackID=" + rackID.ToString() + " and shelfID=" + shelfID.ToString() + " count=1" ;   // only one, duplicate entry will be ignored
            cmd = new SqlCommand(sql, cnn);
            dataReader = cmd.ExecuteReader();

            while (dataReader.Read())
            {
                //output = output + "," + dataReader.GetValue(0);
                sdata.lightOn = (bool)dataReader.GetValue(6);             // lightOn
                sdata.lightIntensity = (uint) dataReader.GetValue(7);      // lightIntensity
                sdata.valvePercentage = (uint) dataReader.GetValue(8);     // valve percentage
                sdata.lightSchedulerOn = (bool)dataReader.GetValue(9);    // light scheduler on
                sdata.lightScheduleStartHH = (uint)getHH((string)dataReader.GetValue(9));
                sdata.lightScheduleStartMM = (uint)getMM((string)dataReader.GetValue(9));
                sdata.lightScheduleEndHH = (uint)getHH((string)dataReader.GetValue(10));
                sdata.lightScheduleEndMM = (uint)getMM((string)dataReader.GetValue(10));
                sdata.lightScheduleIntensity = (uint)dataReader.GetValue(11);
                sdata.waterScheduleOn = (bool)dataReader.GetValue(12);    // water scheduler on
                sdata.waterScheduleStartHH = (uint)getHH((string)dataReader.GetValue(13));
                sdata.waterScheduleStartMM = (uint)getMM((string)dataReader.GetValue(13));
                sdata.waterScheduleEndHH = (uint)getHH((string)dataReader.GetValue(14));
                sdata.waterScheduleEndMM = (uint)getMM((string)dataReader.GetValue(14));
                sdata.waterScheduleValvePercentage = (uint)dataReader.GetValue(15);

                bRecordFound = true;
            }   // while

            return bRecordFound;

        }   // readShelfData

    }
}

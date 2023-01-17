using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;


/*
 * Packages required:
 *  NModbus4
 *  System.Data.SqlClient
 */

namespace RackController
{
    class Program
    {
        /*
        void test()
        {
            rackDB rdb = new rackDB();
            modbusTCP mb = new modbusTCP("192.168.11.5");

            rdb.test();
            //mb.test2();
        }
        */


        static void mainProcess()
        {
            RESULT_CODE result;
            rackDB rdb = new rackDB();
            farmType farm = new farmType();
            rackOperation[] rackOpInstance = new rackOperation[constants.NUM_RACKS];
            bool bAvailable;
            string s;


            farm.numRacks = constants.NUM_RACKS;

            // initialize
            for (uint rid = 0; rid < farm.numRacks; rid++)
            {
                s = constants.RACK_PLC_IP[rid];
                rackOpInstance[rid] = new rackOperation(rid);

                farm.rackArray[rid] = new rackType();
                farm.rackArray[rid].numShelf = constants.NUM_SHELF_PER_RACK[rid];
                bAvailable = rackOpInstance[rid].init(s, ref farm);

                if (bAvailable)
                {
                    for (int sid = 0; sid < farm.rackArray[0].numShelf; sid++)
                    {
                        farm.rackArray[rid].shelfArray[sid] = new shelfType();
                    }
                }
            }

            Console.WriteLine("Done initialization");

            while (true)
            {

                
                for(int rid=0; rid<farm.numRacks; rid++)
                {
                    if (farm.rackArray[rid].bAvailable)
                    {
                        result = rackOpInstance[rid].processRack(rdb, ref farm.rackArray[rid]);

                        // If disconnected, reinitialize
                        if (result == RESULT_CODE.ERROR_DISCONNECTED)
                        {   // reinit
                            farm.rackArray[rid].bAvailable = rackOpInstance[rid].init(constants.RACK_PLC_IP[rid], ref farm);
                        }   // if disconnected

                    }   // if available
                }   // for

            }   //while

        }


        static void Main(string[] args)
        {
            Console.Write("Rack controller started");

            mainProcess();

            Console.Write("Rack controller terminated");
        }
    }
}

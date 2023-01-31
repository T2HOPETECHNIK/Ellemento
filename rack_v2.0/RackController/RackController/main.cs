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
            int iRacksAvailable = 0;
            bool[] isChanged = new bool[constants.NUM_RACKS];
            bool bStartup = true;

            //rdb.test();


            farm.numRacks = (ushort) constants.NUM_RACKS;

            // initialize
            for (uint rid = 0; rid < farm.numRacks; rid++)
            {
                s = constants.RACK_PLC_IP[rid];
                rackOpInstance[rid] = new rackOperation(rid);
                                
                farm.rackArray[rid] = new rackType();
                farm.rackArray[rid].numShelf = 14;  // (ushort) constants.NUM_SHELF_PER_RACK[rid];
                //farm.rackArray[rid].shelfCommandArray = new shelfCommandType[14];
                //farm.rackArray[rid].shelfFeedbackArray = new shelfFeedbackType[14];
                //farm.rackArray[rid].shelfCommandArray = new shelfCommandType[NUM_SHELF_PER_RACK[rid]];
                //farm.rackArray[rid].shelfFeedbackArray = new shelfFeedbackType[NUM_SHELF_PER_RACK[rid]];
                bAvailable = rackOpInstance[rid].init(s, ref farm, ref rdb);

                if (bAvailable)
                {
                    iRacksAvailable++;
                    for (int sid = 0; sid < farm.rackArray[0].numShelf; sid++)
                    {
                        farm.rackArray[rid].shelfCommandArray[sid] = new shelfCommandType();
                    }
                }
            }

            //rackOpInstance[0].test();

            Console.WriteLine("Done initialization");

            while (true)
            {

                if (iRacksAvailable == 0)
                {
                    Console.WriteLine("No racks to process. Terminating.");
                    break;
                }

                // Get list of racks with changes only, so that we don't waste time processing those racks that are not changed.
                rdb.getRackUpdateList(ref isChanged);


                for (int rid=0; rid<farm.numRacks; rid++)
                {
                    if ((farm.rackArray[rid].bAvailable) && (isChanged[rid] || bStartup))
                    {
                        result = rackOpInstance[rid].processRack(rdb, ref farm.rackArray[rid]);

                        // If disconnected, reinitialize
                        if (result == RESULT_CODE.ERROR_DISCONNECTED)
                        {   // reinit
                            farm.rackArray[rid].bAvailable = rackOpInstance[rid].init(constants.RACK_PLC_IP[rid], ref farm, ref rdb);
                        }   // if disconnected

                    }   // if available
                }   // for

                // Do first processing done
                bStartup = false;

            }   //while

        }


        static void Main(string[] args)
        {
            Console.WriteLine("Rack controller started");

            mainProcess();

            Console.WriteLine("Rack controller terminated");
        }
    }
}

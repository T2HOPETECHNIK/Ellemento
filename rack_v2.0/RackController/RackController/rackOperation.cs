using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RackController
{
    internal class rackOperation
    {
        modbusTCP mb;
        farmType farm;
        uint rackID;

        public rackOperation(uint rID)
        {
            rackID = rID;
        }


        public void test()
        {
            Console.WriteLine(">> Test");
        }

        public bool init(string ip, ref farmType farmIn)
        {
            Console.WriteLine("Init " + ip);

            farm = farmIn;

            mb = new modbusTCP(ip);

            return (true);
        }


        public RESULT_CODE processRack(rackDB rdb, ref rackType currentRack)
        {
            uint numShelf;
            bool bresult;

            numShelf = constants.NUM_SHELF_PER_RACK[rackID];

            for (uint sid = 0; sid < numShelf; sid++) {
                bresult = rdb.readShelfData(rackID, sid, ref currentRack.shelfArray[sid]);
            }

            // read DB and process data
            return (RESULT_CODE.NO_ERROR);
        }

    }
}

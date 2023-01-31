using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

namespace RackController
{
    internal class rackOperation
    {
        rackIO mb;
        farmType farm;
        uint rackID;

        public rackOperation(uint rID)
        {
            rackID = rID;
        }

        ~rackOperation()
        {

        }
        
        
        public bool init(string ip, ref farmType farmIn, ref rackDB rdb)
        {
            Console.Write("Init " + ip);

            farm = farmIn;

            mb = new rackIO(ip);

            farm.rackArray[rackID].bAvailable = mb.isAvailable();

            if (farm.rackArray[rackID].bAvailable)
            {
                Console.WriteLine(" OK");
                rdb.getRackInfo(rackID, ref farm.rackArray[rackID]);  // rackID in table starts at 1, while arrays starts at 0
                return true;
            }
            else
            {
                Console.WriteLine(" failed");
                return (false);
            }
        }


        public void test()
        {
            mb.test();
        }


        public RESULT_CODE processRack(rackDB rdb, ref rackType currentRack)
        {
            uint numShelf;
            bool bresult;
            uint numPump;
            
            numShelf = constants.NUM_SHELF_PER_RACK[rackID];

            for (uint sid = 0; sid < numShelf; sid++) {
                // Shelf shelf data from DB
                bresult = rdb.readShelfData(rackID, sid, ref currentRack.shelfCommandArray[sid]);
            }
            // update via modbus
            mb.setShelfData(rackID, numShelf, ref currentRack.shelfCommandArray);

            // Pumps
            numPump = currentRack.numPump;

            for (uint sid = 0; sid < numShelf; sid++)
            {
                // read modbus data
                mb.getShelfFeedback(sid, ref currentRack.shelfFeedbackArray[sid]);
                // To do: Update shelf data to DB
                rdb.setShelfData(rackID, sid, ref currentRack.shelfFeedbackArray[sid]);
            }

            // read DB and process data
            return (RESULT_CODE.NO_ERROR);
        }

    }

}

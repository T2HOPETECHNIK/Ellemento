using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FamrRackUI
{
    class FarmSetup
    {
        public FarmSetup()
        {

        }


        public FARM setup()
        {
            var frm = new FARM();

            frm.numRacks = Constants.numRacks;

            frm.rack = new RACK[frm.numRacks];

            for(int idx = 0; idx < frm.numRacks; idx++) 
            {
                //frm.rack[idx].IP = "192.168.1." + (31 + idx).ToString();
                frm.rack[idx].IP = "192.168.11.5";
                frm.rack[idx].port = Constants.portNum;

                if (idx < 3) 
                {
                    frm.rack[idx].numShelf = Constants.numShelf_B;
                    frm.rack[idx].numPump = Constants.numPump_B;
                    frm.rack[idx].numLight = Constants.numLight_B;
                    frm.rack[idx].rackType = RACK_TYPE.TYPE_B;
                }
                else
                {
                    frm.rack[idx].numShelf = Constants.numShelf_A;
                    frm.rack[idx].numPump = Constants.numPump_A;
                    frm.rack[idx].numLight = Constants.numLight_A;
                    frm.rack[idx].rackType = RACK_TYPE.TYPE_A;
                }

                /*
                frm.rack[idx].shelf = new SHELF[frm.rack[idx].numShelf];
                frm.rack[idx].pump = new PUMP[frm.rack[idx].numPump];
                frm.rack[idx].light = new LIGHT[frm.rack[idx].numLight];
                */

                frm.rack[idx].shelf = new SHELF[Constants.maxShelf];
                frm.rack[idx].pump = new PUMP[Constants.maxPump];
                frm.rack[idx].light = new LIGHT[Constants.maxLight];

                // Set whether available or not

                for (int idx2 = 0; idx2 < Constants.maxLight; idx2++)
                {
                    if (idx2 < frm.rack[idx].numLight)
                        frm.rack[idx].light[idx2].bIsAvailable = true;
                    else
                        frm.rack[idx].light[idx2].bIsAvailable = false;
                }


                for (int idx2 = 0; idx2 < Constants.maxShelf; idx2++)
                {
                    if (idx2 < frm.rack[idx].numShelf)
                        frm.rack[idx].shelf[idx2].bIsAvailable = true;
                    else
                        frm.rack[idx].shelf[idx2].bIsAvailable = false;
                }

                
                for (int idx2 = 0; idx2 < Constants.maxPump; idx2++)
                {
                    if (idx2 < frm.rack[idx].numPump)
                        frm.rack[idx].pump[idx2].bIsAvailable = true;
                    else
                        frm.rack[idx].pump[idx2].bIsAvailable = false;
                }
                


            }   // for

            return frm;

        }   // setup

    }   // Farm Setup

}


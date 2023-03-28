using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FamrRackUI
{
    class Constants
    {

        public const int TIMER_INTERVAL_MS = 2000;

        public const int MAX_LOG_IN_MEMORY = 100;

        public const ulong TIMEOUT_CNT = 2000;
        public const int numRacks = 14;


        public const int maxShelf = 14; 
        public const int maxLight = 14;
        public const int maxPump = 2;


        public const int numShelf_A = 11;
        public const int numShelf_B = 14;

        public const int numPump_A = 1;
        public const int numPump_B = 2;

        public const int numLight_A = 11;
        public const int numLight_B = 14;


        public const int portNum = 502;


        public const int POS_TOP = 5;
        public const int CTRL_HEIGHT = 40;
        public const int POS_LABEL_LEFT = 40;
        public const int WIDTH_LABEL = 100;
        public const int WIDTH_SCHEDULE = 70;
        public const int WIDTH_TEXTBOX = 60;
        public const int WIDTH_CHECKBOX = 70;
        public const int WIDTH_BAR = 150;
        public const int WIDTH_UNIT_LABEL = 40;

        public const int SPACER = 20;


        public const int POS_PUMP_TOP = 100;
        public const int POS_PUMP_LEFT = 1200;
        public const int POS_PUMP_WIDTH = 90;
        public const int POS_PUMP_HEIGHT = 30;

        public const int PUMP_CTRL_GAP = 5;

        //==============================================

        public const int STAT_IDX_UNKNOWN = 2;
        public const int STAT_IDX_NORMAL = 0;
        public const int STAT_IDX_ERROR = 1;


        public static readonly string[] STATUS_INDICATOR = {
            "NORMAL",
            "ERROR",
            "-----"
        };


        public static readonly string[] ERROR_DESCRIPTION = {
            "Normal operation",
            "Unable to communicate",
            "Unknown error"
        };

    }
}

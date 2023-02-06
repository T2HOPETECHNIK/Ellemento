

using RackController;
using System.Security.Permissions;

public enum RESULT_CODE
{
    NO_ERROR,
    ERROR_DISCONNECTED
}


public struct shelfCommandType
{

    public bool bAvailable;

    // ====================================
    // DB to modbus

    public bool C_lightOn;
    public bool C_waterOn;
    public ushort C_lightIntensity;
    public ushort C_valvePercentage;

    public bool C_lightSchedulerOn;
    public ushort C_lightScheduleStartHH;
    public ushort C_lightScheduleStartMM;
    public ushort C_lightScheduleEndHH;
    public ushort C_lightScheduleEndMM;
    public ushort C_lightScheduleIntensity;

    public bool C_waterScheduleOn;
    public ushort C_waterScheduleStartHH;
    public ushort C_waterScheduleStartMM;
    public ushort C_waterScheduleEndHH;
    public ushort C_waterScheduleEndMM;
    public ushort C_waterScheduleValvePercentage;

    public ushort C_mode;

    /*
    public shelfCommandType()
    {
        C_lightOn = false;
        C_waterOn = false;
        C_lightIntensity = 0;
        C_valvePercentage = 0;

        C_lightSchedulerOn = false;
        C_lightScheduleStartHH = 0;
        C_lightScheduleStartMM = 0;
        C_lightScheduleEndHH = 0;
        C_lightScheduleEndMM = 0;
        C_lightScheduleIntensity = 0;

        C_waterScheduleOn = false;
        C_waterScheduleStartHH = 0;
        C_waterScheduleStartMM = 0;
        C_waterScheduleEndHH = 0;
        C_waterScheduleEndMM = 0;
        C_waterScheduleValvePercentage = 0;
    }
    */

}

public struct shelfFeedbackType 
{

    // =====================================
    // Modbus to DB

    public bool bAvailable;

    public bool F_lightOn;
    public bool F_waterOn;
    public bool F_overflow;

    public ushort F_lightIntensity;
    public ushort F_valvePercentage;

    /*
    public shelfFeedbackType()
    {
        bAvailable = false;

        F_lightOn = false;
        F_waterOn = false;
        F_overflow = false;

        F_lightIntensity = 0;
        F_valvePercentage = 0;
    }
    */

}


public struct pumpCommandType
{
    public ushort C_flowRate;
    public ushort C_frequency;
    public bool C_on;

}

public struct pumpFeedbackType
{ 
    public ushort F_flowrate;
    public ushort F_frequency;

}


public class rackType
{
    public shelfCommandType[] shelfCommandArray;
    public shelfFeedbackType[] shelfFeedbackArray;
    public pumpCommandType[] pumpCommandArray;
    public pumpFeedbackType[] pumpFeedbackArray;
    public bool bAvailable;
    public ushort numShelf;
    public ushort numPump;

    public rackType()
    {
        
            shelfCommandArray = new shelfCommandType[14];
            shelfFeedbackArray = new shelfFeedbackType[14];
            pumpCommandArray = new pumpCommandType[2];
            pumpFeedbackArray = new pumpFeedbackType[2];
        
    }

}



public class farmType
{
    public rackType[] rackArray;
    public ushort numRacks;

    public farmType()
    {
        rackArray = new rackType[constants.NUM_RACKS];
        numRacks = (ushort) constants.NUM_RACKS;
    }

}




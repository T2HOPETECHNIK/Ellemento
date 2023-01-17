

using RackController;


public enum RESULT_CODE
{
    NO_ERROR,
    ERROR_DISCONNECTED
}


public class shelfType
{

    public bool bAvailable;

    public bool lightOn;
    public bool waterOn;
    public uint lightIntensity;
    public uint valvePercentage;

    public bool lightSchedulerOn;
    public uint lightScheduleStartHH;
    public uint lightScheduleStartMM;
    public uint lightScheduleEndHH;
    public uint lightScheduleEndMM;
    public uint lightScheduleIntensity;

    public bool waterScheduleOn;
    public uint waterScheduleStartHH;
    public uint waterScheduleStartMM;
    public uint waterScheduleEndHH;
    public uint waterScheduleEndMM;
    public uint waterScheduleValvePercentage;

}


public class rackType
{
    public shelfType[] shelfArray;
    public bool bAvailable;
    public uint numShelf;

    public rackType()
    {
        shelfArray = new shelfType[14];
    }
}



public class farmType
{
    public rackType[] rackArray;
    public uint numRacks;

    public farmType()
    {
        rackArray = new rackType[constants.NUM_RACKS];
    }
}




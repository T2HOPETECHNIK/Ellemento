
struct FARM
{
    public int numRacks;
    public RACK[] rack;
}


enum RACK_TYPE
{
    TYPE_A,
    TYPE_B
}


struct SHELF
{
    public bool bIsAvailable;
    public bool bPlantsAvailable;
    public bool mode;
    public uint iPVvalue;
    public bool bOverflow;
    public bool bUseWaterSchedule;
    public string sWaterSchedule;

}

struct PUMP
{
    public bool bIsAvailable;
    public int iOutFlowrate;
    public int iFBFlowrate;
    public uint iOutFrequency;
    public bool bFillDrainMode;
}

struct LIGHT
{
    public bool bIsAvailable;
    public uint iIntensity;
    public bool bOnOff;
    public bool bUseLightSchedule;
    public string sLightSchedule;

}


struct RACK
{
    public string IP;
    public int port;
    public RACK_TYPE rackType;


    public int numShelf;
    public int numPump;
    public int numLight;

    public SHELF[] shelf;
    public PUMP[] pump;
    public LIGHT[] light;

    public bool bApplyChange;

}


enum ERROR_CODE
{
    ERROR_NONE,
    ERROR_COMM_ERROR,
    ERROR_UNKNOWN
}



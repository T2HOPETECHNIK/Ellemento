


enum DATA_TYPES{
    UINT_TYPE,
    INT_TYPE,
    FLOAT_TYPE,
    BYTE_TYPE,
    BIT_TYPE,
    UNKNOWN_TYPE
}


enum ADDRESS_ACCESS_TYPES
{
    READ_ONLY,
    WRITE_ONLY,
    READ_WRITE,
    UNKNOWN
}


enum CONFIG_LINE_TYPE
{
    CLT_EMPTY,
    CLT_IP,
    CLT_CONTROL
}


enum ERROR_CODE
{
    ERROR_NONE,
    ERROR_CONFIG_FAIL,
    ERROR_NO_CONFIG,
    ERROR_COMM_FAIL
}


struct SYSTEM_CONFIG
{
    public string appTitle;
    public string ip;
    public int port;
    public int updateCycle_ms;
    public uint numFields;
}

struct FIELD
{
    public DATA_TYPES dataType;
    public ushort address;
    public ADDRESS_ACCESS_TYPES access;
    public byte controlType;
    public ushort bitpos;
    public string textLabel;

}

public struct READ_DATA
{
    public const int max_fields = 200;
    public ushort[] tbValue; 
    public bool[] cbValue; 
}


public struct WRITE_DATA
{
    public const int max_fields = 200;
    public bool[] isBitField;
    public ushort[] WordValue;
    public bool[] BitValue;
}


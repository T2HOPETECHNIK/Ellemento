Ellemento High Level Software<a name="TOP"></a>
===================

# Build 
To build the project 
```
cd server_lib
python -m build
```

# Entry Point
To run the project
```
python -m ellemento
python -m ellemento.job
```
To run the main file for plc
```
python -m ellemento.plc 
``` 


To run the main file for the logging 
```
python -m lib.logging 
```
# Test
To test the project
```
 python -m unittest discover
```

# Modules
## Ellemento 
### Model
[Model description](Ellemento/model/readme.md)
### PLC
### Bridge
### Job 

## lib 

# Config

## PLC address configuration 

The files contains the definition of the PLC address, memory address for reading and accessing the plc registers 
```
cd ellemento/plc 
code addresss.json 
{
    "Description": "For modbus ip and address configurations", 
    "modbus": 
    [
        {
            "name": "Ellemento rack 1", 
            "ip": "192.168.1.5",    # modbus ip address for the rack 
            "id": 1,                # rack id in the system 
            "FEEDBACK_LED":         # LED address 
            {
                "position": 4020, 
                "bits": 14
            },
            "CTRL_LIGHT_ON": 
            {
                "position": 4080, 
                "bits": 14
            }
            ...
        },
        {
            ...
        }
    ]
}
```
## Model_plc_mapping 
The bridge module maps lower level plc address to high level models. For example, the server program needs to open a lights. We have a LightControl class, it has a method called Lightcontrol.on

### The detailed call would be 
LightContro->on 
{
    LightBridge->On
    {
        Plc write on (True) the light on register 
    }
}

### The mapping between high level model to lowe level plc address is 
```
cd ellemento/bridge 
code model_plc_mapping.json 
{
    "id": 1, 
    "Description": "For farm models and modbus plc address mapping", 
    "Pump":
    [
        {
            "id": 1, 
            "address":
            {
                "modbus_id": 1, 
                "status":{
                    "tag": "FEEDBACK_PUMP_ON",
                    "position": 0, 
                    "type": "boolean"
                }, 
                "control":{
                    "tag": "CTRL_PUMP_ON", 
                    "position": 0, 
                    "type": "boolean"
                },
            }
        }
    ],
    "Rack":
    [
        {
            "id": 1,    
        }
    ]
    "Shelf":
    []
}
```
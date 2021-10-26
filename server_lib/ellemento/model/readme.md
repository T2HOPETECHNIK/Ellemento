Model Design<a name="TOP"></a>
===================
Descripitons on the models 
# Rack

<h2>There are three types of rack</h2>

* Type A_1 Rack: 1 section only, 12 shelves, height is xxx
* Type A_2 Rack: 1 section only, 12 shelves, height is yyy
* Type B_2 Rack: 
    * Section Top: 8 top shelves
    * Section Bottom: 5 shelves 

Each section has one pump for each racks 

<h2>Class definition</h2>

* apply_update(): 
>> Called after system changed configuration of plcs. All settings can be set at the any time. But they will ONLY take effect once it is applied. This prevents the PLC from resetting the values that are tied to addresses once the HMI is unplugged, by applying any changes only when intended 
* change_session_mode: 
    * Auto – use in scheduling, must turn on scheduling of each shelf
    * Semi auto – Control PV setting is from the look-up table, Only need to turn on/off
    * Manual – Set percentage to turn on PV, 0 is off, 100 is fully open
>> Change section mode to  any of the mode above 

# Shelf

# LightControl 
Each shelf has one light  control 

<h2>Class definition</h2>

* on  - on the light
* status - get status of the light
* off - off the light 
* intensity - get intensity of the light 
* set_intensity - set intensity of the light 
* adjust - adjust the intensity of the light with perctage 
  
# Water Control 
Each shelf has one water control 

<h2>Class definition</h2>

* on - turn on the water  of the valves
* off - turn of the water of the valves 
* adjust - adjust the light of the light 
* get_percent - Get percentage of the water flow 

# PumpControl

<h2>Class definition</h2>

* On
>> Trun on the pump 
* Off
>> Trun of the pump 
* set_mode
>> Set pumpo to rpm mode or flowrate mode 
* Set_rpm
>> Set rpm of pump when pump is on rpm mode 
* set_flowrate
>> Set flowrate value when pump is on flowrate mode 



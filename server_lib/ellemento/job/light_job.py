# on and off the lights according to the 
from ellemento.model.light_control import LightControl

def on_lights():
    if(len(LightControl.all_lights) < 1):
        raise Exception("No lights is added in the system, no of lights is 0")
    for light_x in LightControl.all_lights:
        light_x.on(percent = 100)
    pass 

def off_lights(): 
    if(len(LightControl.all_lights) < 1):
        raise Exception("No lights is added in the system, no of lights is 0")
    for light_x in LightControl.all_lights:
        light_x.off(percent = 100)
    pass 




# if __name__ == '__main__':
#     print("Started")
#     LightControl.all_lights





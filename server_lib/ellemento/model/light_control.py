from enum import Enum

class LightStatus(Enum):
    OFF = 1        # clean and ready to use
    ON = 2      # with plants 
     
# Other status could be added later 

class LightControl:
    
    all_lights = {} 

    @staticmethod 
    def get_light(id):
        return LightControl.all_lights[id]

    @staticmethod 
    def print(): 
        for shelf_x in LightControl.all_lights:
            print(LightControl.all_lights[shelf_x])

    @staticmethod 
    def add_light(light_new):
        LightControl.all_lights[light_new.id] = light_new

    def __init__(self, id, type_name):
        self._id = id
        self._percent = 0
        self._status = LightStatus.OFF
        self._type_name = type_name

    @property
    def id(self):
        return self._id 

    @id.setter
    def id(self, value):
        self._id = value 

    def on(self, percent = 100): 
        self._status = LightStatus.ON
        self._percent = percent

    def off(self):
        self._status = LightStatus.OFF

    def adjust(self, percent):
        self._percent = percent


    def __repr__(self):
        return "<object: %s, id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)

    def __str__(self):
        return "<object: %s, id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)
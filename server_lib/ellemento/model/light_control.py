from enum import Enum

from ellemento.bridge.bridge_factory import ModelPlcBridgeFactory


class LightStatus(Enum):
    OFF = 1  # clean and ready to use
    ON = 2  # with plants


# Other status could be added later 

class LightControl:
    all_lights = {}

    @staticmethod
    def get_light(id):
        return LightControl.all_lights[id]

    @staticmethod
    def print():
        for light_x in LightControl.all_lights:
            print(LightControl.all_lights[light_x])

    @staticmethod
    def add_light(light_new):
        LightControl.all_lights[light_new.id] = light_new

    def __init__(self, id, type_name):
        self._id = id
        self._percent = 0
        self._status = LightStatus.OFF
        self._type_name = type_name
        self.mod_bus = ModelPlcBridgeFactory.get_bridge(type='Light', id=self._id)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

        # bind the light control with a particular modbus io

    def bind_plc(self, plc):
        self._plc = plc

    def on(self, percent=100):
        ret, error = self.mod_bus.on_light()
        self._status = LightStatus.ON
        self._percent = percent
        return self._status, error

    def status(self):
        light_on, error = self.mod_bus.on_off_status()
        if light_on:
            self._status = LightStatus.ON
        else:
            self._status = LightStatus.OFF
        return self._status, error

    def intensity(self):
        intensity, error = self.mod_bus.intensity()
        return intensity, error

    def off(self):
        ret, error = self.mod_bus.off_light()
        print(ret)
        print(error)
        self._status = LightStatus.OFF
        return ret, error

    def set_intensity(self, value):
        ret, error = self.mod_bus.set_intensity(value)
        return ret, error

    def adjust(self, percent):
        self._percent = percent

    def __repr__(self):
        return "<object: %s, id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)

    def __str__(self):
        return "<object: %s, id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)

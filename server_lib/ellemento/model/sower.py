# shelf 
# pum;p 
# each shelf has 9 trays maximum 
# Each shelf has light and water control 
from enum import Enum

class Sower:
    def __init__(self, id = -1, type_name = "Default"):
        self._id = id
        self._type_name = type_name
        self._tray = None
        
    @property
    def id(self): 
        return self._id 

    @id.setter
    def id(self, value):
        self._id = value 

    def __repr__(self):
        return "<object: %s, id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)

    def __str__(self):
        return "<object: %s, id:%d type:%s>" % (self.__class__.__name__, self._id, self._type_name)
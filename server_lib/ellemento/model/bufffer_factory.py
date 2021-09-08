from ellemento.model.buffer import Buffer
from enum import Enum

class BufferType(Enum):
    BUFFER_3_IN = 1            # clean and ready to use
    BUFFER_4 = 2        # with plants 
    BUFFER_4_OUT = 3
    BUFFER_4_IN = 4     
    BUFFER_5 = 5

class BufferFactory:

    all_buffers = {}
    @staticmethod  
    def create_buffer(type_name = "Default", id = -1):
        buffer_new = None
        #Tray.add_tray(tray_new)
        buffer_new = Buffer(id = id, type_name = type_name)
        return buffer_new  

    @staticmethod 
    def create_all_buffers(): 
        # Crete all kind of buffers 
        buffer_3_in = BufferFactory.create_buffer(type_name="3-In-Buffer", id = 1)
        buffer_4 = BufferFactory.create_buffer(type_name="4-Buffer", id = 2)
        buffer_4_out = BufferFactory.create_buffer(type_name="4-Out-Buffer", id = 3)
        buffer_4_in = BufferFactory.create_buffer(type_name="4-In-Buffer", id = 4)
        buffer_5  = BufferFactory.create_buffer(type_name="5-Buffer", id = 5)
        BufferFactory.all_buffers[BufferType.BUFFER_3_IN]   = buffer_3_in
        BufferFactory.all_buffers[BufferType.BUFFER_4]      = buffer_4
        BufferFactory.all_buffers[BufferType.BUFFER_4_OUT]  = buffer_4_out
        BufferFactory.all_buffers[BufferType.BUFFER_4_IN]   = buffer_4_in
        BufferFactory.all_buffers[BufferType.BUFFER_5]      = buffer_5

    @staticmethod 
    def get_buffer(type = BufferType.BUFFER_3_IN): 
        return BufferFactory.all_buffers[type]

    @staticmethod 
    def print():
        Buffer.print() 
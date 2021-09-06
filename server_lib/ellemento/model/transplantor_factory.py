from os import stat

from ellemento.model.transplantor import Transplantor, TransplantorType

class TransplantorFactory:
    all_transplantors = {}

    @staticmethod 
    def get_transplator_3_4(): 
        if len(TransplantorFactory.all_transplantors) == 0: 
            TransplantorFactory.create_transplantors()
        return TransplantorFactory.all_transplantors[1] 
     
    @staticmethod 
    def get_transplator_4_5(): 
        if len(TransplantorFactory.all_transplantors) == 0: 
            TransplantorFactory.create_transplantors()
        return TransplantorFactory.all_transplantors[2] 
    
    @staticmethod 
    def create_transplantors(): 
        tansplantor_3_4 = TransplantorFactory.create_transplantor(id = 1, type_name = "transplantor_3_4")
        tansplantor_4_5 = TransplantorFactory.create_transplantor(id = 2, type_name = "transplantor_4_5")
        TransplantorFactory.all_transplantors[tansplantor_3_4.id] = tansplantor_3_4
        TransplantorFactory.all_transplantors[tansplantor_4_5.id] = tansplantor_4_5 
        pass 

    @staticmethod  
    def create_transplantor(type_name = "default", id = -1):
        shelf_new = None
        #Tray.add_tray(tray_new)
        shelf_new = Transplantor(id = id, type_name = type_name)
        # add trays, 
        # add water controls
        # add lights 
        
        return Transplantor.get_shelf(id)

    @staticmethod 
    def print():
        Transplantor.print() 


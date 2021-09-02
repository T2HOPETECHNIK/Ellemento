from ellemento.model.transplantor import Transplantor

class TransplantorFactory:
    all_transplantors = {}

    @staticmethod  
    def create_transplantors(type_name = "default", id = -1):
        shelf_new = None
        #Tray.add_tray(tray_new)
        shelf_new = Transplantor(id = id, type_name = type_name)
        # add trays, 
        # add water controls
        # add lights 
        Transplantor.add_shelf(shelf_new)
        
        return Transplantor.get_shelf(id)

    @staticmethod 
    def print():
        Transplantor.print() 

    @staticmethod
    def get_empty_shelf_of_phase(phase = Phase.PHASE1): 
        lst_empty_shelf = [] 
        for shelf_x in Shelf.all_shelves:
            shelf_of_idx = Shelf.all_shelves[shelf_x]; 
            if shelf_of_idx.status == ShelfStatus.IDLE and shelf_of_idx.phase == phase: 
                lst_empty_shelf.append(shelf_of_idx)
        return lst_empty_shelf
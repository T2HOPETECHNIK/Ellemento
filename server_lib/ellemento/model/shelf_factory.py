from ellemento.model.shelf import Shelf

class ShelfFactory:
    @staticmethod  
    def create_shelf(type_name = "default", id = -1):
        tray_new = None
        #Tray.add_tray(tray_new)
        shelf_new = Shelf(id = id, type_name = type_name)
        Shelf.add_shelf(shelf_new)
        return Shelf.get_shelf(id)

    @staticmethod 
    def print():
        Shelf.print_shelf() 
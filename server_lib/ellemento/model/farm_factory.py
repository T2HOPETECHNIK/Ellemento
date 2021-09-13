from ellemento.model.farm import Farm

class FarmFactory:
    @staticmethod  
    def create_farm(type_name = "Default", id = -1):
        return Farm.create_farm(id = 1, type_name="Default")

    @staticmethod 
    def print():
        Farm.print() 
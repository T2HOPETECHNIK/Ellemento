from ellemento.model.transplanter import Transplanter


class TransplantorFactory:
    all_transplanters = {}

    @staticmethod
    def get_transplanter_3_4():
        if len(TransplantorFactory.all_transplanters) == 0:
            TransplantorFactory.create_transplanter()
        return TransplantorFactory.all_transplanters[1]

    @staticmethod
    def get_transplantor_4_5():
        if len(TransplantorFactory.all_transplanters) == 0:
            TransplantorFactory.create_transplanter()
        return TransplantorFactory.all_transplanters[2]

    @staticmethod
    def create_transplanter():
        transplanter_3_4 = TransplantorFactory.create_transplantor(id=1, type_name="transplantor_3_4")
        transplanter_4_5 = TransplantorFactory.create_transplantor(id=2, type_name="transplantor_4_5")
        TransplantorFactory.all_transplanters[transplanter_3_4.id] = transplanter_3_4
        TransplantorFactory.all_transplanters[transplanter_4_5.id] = transplanter_4_5
        pass

    @staticmethod
    def create_transplantor(type_name="default", id=-1):
        trans_new = None
        # Tray.add_tray(tray_new)
        trans_new = Transplanter(id=id, type_name=type_name)
        # add trays, 
        # add water controls
        # add lights Z
        return trans_new

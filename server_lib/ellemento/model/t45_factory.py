from ellemento.model.t45_control import t45


class t45Factory:
    @staticmethod
    def create_t45(id=-1):
        t45_new = t45(id=id)
        t45.add_t45(t45_new)
        return t45.get_t45(id)

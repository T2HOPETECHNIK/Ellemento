from ellemento.model.t34_control import t34


class t34Factory:
    @staticmethod
    def create_t34(id=-1):
        t34_new = t34(id=id)
        t34.add_t34(t34_new)
        return t34.get_t34(id)

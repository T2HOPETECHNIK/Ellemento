from ellemento.model.sower_control import sower


class sowerFactory:
    @staticmethod
    def create_sower(id=-1):
        sower_new = sower(id=id)
        sower.add_sower(sower_new)
        return sower.get_sower(id)

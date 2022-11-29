from ellemento.model.harvester_control import harvester


class harvesterFactory:
    @staticmethod
    def create_harvestor(id=-1):
        harvestor_new = harvester(id=id)
        harvester.add_harvester(harvestor_new)
        return harvester.get_harvester(id)

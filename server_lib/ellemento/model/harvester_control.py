import time
from ellemento.bridge.bridge_factory import ModelPlcBridgeFactory


class harvester:
    all_harvester = {}

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @staticmethod
    def get_harvester(id):
        return harvester.all_harvester[id]

    @staticmethod
    def print():
        for harvester_x in harvester.all_harvester:
            print(harvester.all_harvester[harvester_x])

    @staticmethod
    def add_harvester(harvester_new):
        harvester.all_harvester[harvester_new.id] = harvester_new

    def __init__(self, id):
        self._id = id
        self.twin_cat = ModelPlcBridgeFactory.get_bridge(type='harvester', id=self._id)

    def load_tray(self):
        if self.twin_cat.ready_to_place():
            time.sleep(1)
            self.twin_cat.ASRS_arrived(True)
            if self.twin_cat.lock_ASRS():
                self.twin_cat.ASRS_locked(True)
                time.sleep(1)
                print("waiting for tray transfer")
                time.sleep(1)
                print("tray received")
                self.twin_cat.ASRS_part_presence(True)
                time.sleep(1)
                self.twin_cat.part_placed(True)

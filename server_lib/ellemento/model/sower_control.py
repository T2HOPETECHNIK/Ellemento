import time

from ellemento.bridge.bridge_factory import ModelPlcBridgeFactory


class sower:
    all_sower = {}

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @staticmethod
    def get_sower(id):
        return sower.all_sower[id]

    @staticmethod
    def print():
        for sower_x in sower.all_sower:
            print(sower.all_sower[sower_x])

    @staticmethod
    def add_sower(sower_new):
        sower.all_sower[sower_new.id] = sower_new

    def __init__(self, id):
        self._id = id
        self.twin_cat = ModelPlcBridgeFactory.get_bridge(type='sower', id=self._id)

    def unload_tray(self):
        if self.twin_cat.ready_to_pick():
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
                self.twin_cat.part_picked(True)

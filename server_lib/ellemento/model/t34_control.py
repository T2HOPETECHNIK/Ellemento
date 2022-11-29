import time

from ellemento.bridge.bridge_factory import ModelPlcBridgeFactory


class t34:
    all_t34 = {}

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @staticmethod
    def get_t34(id):
        return t34.all_t34[id]

    @staticmethod
    def print():
        for t34_x in t34.all_t34:
            print(t34.all_t34[t34_x])

    @staticmethod
    def add_t34(t34_new):
        t34.all_t34[t34_new.id] = t34_new

    def __init__(self, id):
        self._id = id
        self.twin_cat = ModelPlcBridgeFactory.get_bridge(type='t34', id=self._id)

    def load_tray(self):
        if self.twin_cat.ready_to_place():
            time.sleep(1)
            self.twin_cat.ASRS_arrived_place_pos(True)
            if self.twin_cat.lock_ASRS_place_pos():
                self.twin_cat.ASRS_locked_place_pos(True)
                time.sleep(1)
                print("waiting for tray transfer")
                time.sleep(1)
                print("tray received")
                self.twin_cat.ASRS_part_presence_place_pos(True)
                time.sleep(1)
                self.twin_cat.part_placed(True)

    def unload_tray(self):
        if self.twin_cat.ready_to_pick():
            time.sleep(1)
            self.twin_cat.ASRS_arrived_pick_pos(True)
            if self.twin_cat.lock_ASRS_pick_pos():
                self.twin_cat.ASRS_locked_pick_pos(True)
                time.sleep(1)
                print("waiting for tray transfer")
                time.sleep(1)
                print("tray received")
                self.twin_cat.ASRS_part_presence_pick_pos(True)
                time.sleep(1)
                self.twin_cat.part_picked(True)

import time
from ellemento.bridge.bridge_factory import ModelPlcBridgeFactory


class t45:
    all_t45 = {}

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @staticmethod
    def get_t45(id):
        return t45.all_t45[id]

    @staticmethod
    def print():
        for t45_x in t45.all_t45:
            print(t45.all_t45[t45_x])

    @staticmethod
    def add_t45(t45_new):
        t45.all_t45[t45_new.id] = t45_new

    def __init__(self, id):
        self._id = id
        self.twin_cat = ModelPlcBridgeFactory.get_bridge(type='t45', id=self._id)

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
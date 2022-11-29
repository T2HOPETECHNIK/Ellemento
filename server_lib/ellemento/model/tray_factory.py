import datetime
import time
from ellemento.model.tray import Tray, TransferStatus, TrayStatus
from ellemento.model.tray_phase_1_3 import TrayPhase13
from ellemento.model.tray_phase_4 import TrayPhase4
from ellemento.model.tray_phase_5 import TrayPhase5
from lib.logging.logger_initialiser import EllementoLogger
from ellemento.model import constants

logger = EllementoLogger.__call__().logger


class TrayFactory:
    max_tray_id = 0
    terminate_job = False
    all_phase123_trays = {}
    all_phase_4_trays = {}
    all_phase_5_trays = {}
    full_grown_trays = {}

    @staticmethod
    def get_full_grown_trays(status=TrayStatus.PHASE1):
        if not status in TrayFactory.full_grown_trays:
            TrayFactory.full_grown_trays[status] = []
        return TrayFactory.full_grown_trays[status]

    @classmethod
    def reset_phase123_status_time(self, status=TrayStatus.PHASE1):
        for tray in self.all_phase123_trays:
            if tray.status == status:
                tray.reset_status_time()

    @classmethod
    def reset_phase4_status_time(self):
        for tray in self.all_phase_4_trays:
            tray.reset_status_time()

    @classmethod
    def reset_phase5_status_time(self):
        for tray in self.all_phase_5_trays:
            tray.reset_status_time()

    @staticmethod
    def create_phase123_trays():
        if len(TrayFactory.all_phase123_trays) != 0:
            return TrayFactory.all_phase123_trays
        phase_1_2_3_trays = constants.TOTAL_PHASE123_SHELF * 9
        logger.info("Initializing phase 1, 2, 3, trays: %d", phase_1_2_3_trays)
        for i in range(1, phase_1_2_3_trays + 1):
            TrayFactory.max_tray_id = TrayFactory.max_tray_id + 1
            tray_new = TrayFactory.create_tray(id=TrayFactory.max_tray_id, type_name="phase1")
            # set tray
            tray_new.has_foam = True
            tray_new.has_veg = True
            TrayFactory.all_phase123_trays[tray_new.id] = tray_new
        return TrayFactory.all_phase123_trays

    @staticmethod
    def create_phase4_trays():
        if len(TrayFactory.all_phase_4_trays) != 0:
            return TrayFactory.all_phase_4_trays
        phase_4_trays = constants.TOTAL_PHASE4_SHELF * 9
        logger.info("Initializing phase 4 trays : %d", phase_4_trays)
        for i in range(1, phase_4_trays + 1):
            TrayFactory.max_tray_id = TrayFactory.max_tray_id + 1
            tray_new = TrayFactory.create_tray(id=TrayFactory.max_tray_id, type_name="phase4")
            tray_new.has_foam = True
            tray_new.has_veg = True
            TrayFactory.all_phase_4_trays[tray_new.id] = tray_new
        return TrayFactory.all_phase_4_trays

    @staticmethod
    def create_phase5_trays():
        if len(TrayFactory.all_phase_5_trays) != 0:
            return TrayFactory.all_phase_5_trays
        phase_5_trays = constants.TOTAL_PHASE5_SHELF * 9
        logger.info("Initializing phase 5 trays : %d", phase_5_trays)
        for i in range(1, phase_5_trays + 1):
            TrayFactory.max_tray_id = TrayFactory.max_tray_id + 1
            print(TrayFactory.max_tray_id)
            tray_new = TrayFactory.create_tray(id=TrayFactory.max_tray_id, type_name="phase5")
            tray_new.has_foam = True
            tray_new.has_veg = True
            TrayFactory.all_phase_5_trays[tray_new.id] = tray_new
            print(TrayFactory.all_phase_5_trays)
            time.sleep(0.5)
        return TrayFactory.all_phase_5_trays

    @staticmethod
    def create_tray(type_name="Unknown", id=-1):
        if type_name in ["phase1","phase2","phase3"]:
            tray_new = TrayPhase13(id=id, type_name="phase1-3")
        elif type_name in ["phase4"]:
            tray_new = TrayPhase4(id=id, type_name="phase4")
        elif type_name in ["phase5"]:
            tray_new = TrayPhase5(id=id, type_name="phase5")
        else:
            raise TypeError("Invalid type of trays created: " + type_name)
        Tray.add_tray(tray_new)
        return Tray.get_tray(id)

    @staticmethod
    def print():
        Tray.print()

    @staticmethod
    def check_duration(trays=None, status=TrayStatus.PHASE1, duration=3, unit='day'):
        if trays is None:
            trays = []
        while not TrayFactory.terminate_job:
            ret_list = TrayFactory.get_full_grown_trays(status)
            # logger.info("Checking growing status %s", str(status))
            logger.warn("Checking phase 5 trays %s %d", status, len(ret_list))
            for tray_idx in trays:
                time_now = datetime.datetime.now()
                diff = time_now - trays[tray_idx].status_time
                day = diff.days
                hour = diff.seconds / 3600
                minute = diff.seconds / 60
                # print(trays[tray_idx].status)
                if trays[tray_idx].status == status and trays[tray_idx].transfer_status == TransferStatus.IDLE:
                    if unit == 'day':
                        if day > duration:
                            trays[tray_idx].set_transfer_status(TransferStatus.READY_TO_TRANSFER)
                            ret_list.append(trays[tray_idx])
                    elif unit == 'hour':
                        hour = day * 24 + hour
                        if hour > duration:
                            trays[tray_idx].set_transfer_status(TransferStatus.READY_TO_TRANSFER)
                            ret_list.append(trays[tray_idx])
                    elif unit == 'minute':
                        minute = day * 24 * 60 + hour * 60 + minute
                        if minute > duration:
                            trays[tray_idx].set_transfer_status(TransferStatus.READY_TO_TRANSFER)
                            ret_list.append(trays[tray_idx])
                    elif unit == 'second':
                        second = diff.seconds
                        if second > duration:
                            logger.warning("Greater than duration %d", duration)
                            trays[tray_idx].set_transfer_status(TransferStatus.READY_TO_TRANSFER)
                            ret_list.append(trays[tray_idx])
                    else:
                        raise Exception("Invalid unit provided")
            time.sleep(2)

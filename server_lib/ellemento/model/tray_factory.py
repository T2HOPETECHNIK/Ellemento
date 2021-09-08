from enum import Enum
import datetime

from ellemento.model.tray import Tray, TransferStatus, TrayStatus
from ellemento.model.tray_phase_1_3 import TrayPhase13
from ellemento.model.tray_phase_4 import TrayPhase4
from ellemento.model.tray_phase_5 import TrayPhase5
from lib.logging.logger_initialiser import EllementoLogger
from ellemento.model import constants


logger = EllementoLogger.__call__().logger; 

class TrayFactory:
    max_tray_id = 0
    all_phase123_trays  = {}
    all_phase_4_trays   = {}
    all_phase_5_trays   = {}


    @staticmethod 
    def create_phase123_trays(): 
        phase_1_2_3_trays = constants.TOTAL_PHASE123_SHELF * 9 
        logger.info("Initializing phase 1, 2, 3, trays: %d", phase_1_2_3_trays)
        for i in range (1, phase_1_2_3_trays + 1): 
            TrayFactory.max_tray_id = TrayFactory.max_tray_id + 1 
            tray_new = TrayFactory.create_tray(id = TrayFactory.max_tray_id, type_name = "phase1-3")
            TrayFactory.all_phase123_trays[tray_new.id] = tray_new
        pass 

    @staticmethod
    def create_phase4_trays(): 
        phase_4_trays = constants.TOTAL_PHASE4_SHELF * 9
        logger.info("Initializing phase 4 trays : %d" , phase_4_trays)
        for i in range (1, phase_4_trays + 1): 
            TrayFactory.max_tray_id = TrayFactory.max_tray_id + 1 
            tray_new =  TrayFactory.create_tray(id = TrayFactory.max_tray_id + i, type_name = "phase4")
            TrayFactory.all_phase_4_trays[tray_new.id] = tray_new

    @staticmethod 
    def create_phase5_trays(): 
        phase_5_trays = constants.TOTAL_PHASE5_SHELF * 9
        logger.info("Initializing phase 5 trays : %d" , phase_5_trays)
        for i in range (1, phase_5_trays + 1): 
            TrayFactory.max_tray_id = TrayFactory.max_tray_id + 1 
            tray_new =  TrayFactory.create_tray(id = TrayFactory.max_tray_id + i, type_name = "phase4")
            TrayFactory.all_phase_5_trays[tray_new.id] = tray_new
        pass 

    @staticmethod  
    def create_tray(type_name = "Unknown", id = -1):
        tray_new = None
        if type_name in ["phase1", "phase 1", "phase 2", "phase2", "phase3", "phase 3", "phase1-3", "phase1-2-3"]: 
            tray_new = TrayPhase13(id = id, type_name = "phase1-3")
        elif type_name in ["phase4", "phase 4"]:
            tray_new = TrayPhase4(id = id, type_name = "phase4")
        elif type_name in ["phase5", "phase 5"]:
            tray_new = TrayPhase5(id = id, type_name = "phase5")
        else:
            raise TypeError("Invalid type of trays created: "+ type_name)
        Tray.add_tray(tray_new)
        return Tray.get_tray(id)

    @staticmethod 
    def print():
        Tray.print() 

    @staticmethod
    def check_duration(tray_list, status = TrayStatus.PHASE1, duration = 3 , unit = 'day'):
        ret_list = [] 
        print (unit)
        for tray_idx in tray_list:
            time_now    = datetime.datetime.now() 
            diff        = time_now -  tray_list[tray_idx].status_time 
            day         = diff.days 
            hour        = diff.seconds / 3600 
            minute      = diff.seconds / 60
            
            if (tray_list[tray_idx].status == status and tray_list[tray_idx].TransferStatus != TransferStatus.READY_TO_TRANSFER):
                if unit == 'day': 
                    if day > duration: 
                        tray_list[tray_idx].set_transfer_status(TransferStatus.READY_TO_TRANSFER)
                        ret_list.append(tray_list[tray_idx])
                elif unit == 'hour': 
                    hour = day * 24 + hour
                    if hour > duration: 
                        tray_list[tray_idx].set_transfer_status(TransferStatus.READY_TO_TRANSFER)
                        ret_list.append(tray_list[tray_idx])
                elif unit == 'minute': 
                    minute = day * 24 * 60 + hour * 60 + minute
                    if minute > duration: 
                        tray_list[tray_idx].set_transfer_status(TransferStatus.READY_TO_TRANSFER)
                        ret_list.append(tray_list[tray_idx])
                elif unit == 'second': 
                    second = diff.seconds 
                    print("..............")
                    if second > duration: 
                        tray_list[tray_idx].set_transfer_status(TransferStatus.READY_TO_TRANSFER)
                        ret_list.append(tray_list[tray_idx])
                else:  
                    raise Exception("Invalid unit provided")
        return ret_list 
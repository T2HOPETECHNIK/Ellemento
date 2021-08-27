from ellemento.model.tray import Tray, TransferStatus, TrayStatus
from ellemento.model.tray_phase_1_3 import TrayPhase13
from ellemento.model.tray_phase_4 import TrayPhase4
from ellemento.model.tray_phase_5 import TrayPhase5

from enum import Enum
import datetime

class TrayFactory:
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
                    if day > diff_required: 
                        tray_list[tray_idx].set_transfer_status(TransferStatus.READY_TO_TRANSFER)
                        ret_list.append(tray_list[tray_idx])
                elif unit == 'hour': 
                    hour = day * 24 + hour
                    if hour > diff_required: 
                        tray_list[tray_idx].set_transfer_status(TransferStatus.READY_TO_TRANSFER)
                        ret_list.append(tray_list[tray_idx])
                elif unit == 'minute': 
                    minute = day * 24 * 60 + hour * 60 + minute
                    if minute > diff_required: 
                        tray_list[tray_idx].set_transfer_status(TransferStatus.READY_TO_TRANSFER)
                        ret_list.append(tray_list[tray_idx])
                elif unit == 'second': 
                    second = diff.seconds 
                    print("..............")
                    if second > diff_required: 
                        tray_list[tray_idx].set_transfer_status(TransferStatus.READY_TO_TRANSFER)
                        ret_list.append(tray_list[tray_idx])
                else:  
                    raise Exception("Invalid unit provided")
        return ret_list 
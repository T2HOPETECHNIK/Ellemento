import logging
import time
from multiprocessing import Process
from ellemento.model.tray_phase_1_3 import TrayPhase13
from ellemento.model.tray_phase_4 import TrayPhase4
from ellemento.model.transplantor_factory import TransplantorFactory
from ellemento.model.transplanter import Transplanter, TransplantorType
from lib.logging.logger_initialiser import EllementoLogger

logger = EllementoLogger.__call__().logger


class TransplantJob:
    transplant_job_list = []
    terminate_job = False

    @staticmethod
    def execute_transplant(source, destinations):
        #
        # To do, get a global value of transplanting
        #
        time.sleep(2)

        source_tray = TrayPhase13(source)
        source_tray.transplant_out()
        for tay_x in destinations:
            dest = TrayPhase4(tay_x)
            dest.transplant_in()
            tay_x = dest
            print(tay_x.has_veg)
        print('Transplanting', destinations)

    @staticmethod
    def create_transplant_jobs():
        while not TransplantJob.terminate_job:
            if len(TransplantJob.transplant_job_list) == 0:
                TransplantJob.create_transplant_job(trans_type=TransplantorType.PHASE_3_4_TRANSPLANTOR)
            else:
                logging.info("Already have 1 transplant job ongoing")
            time.sleep(2)
            return

    @staticmethod
    def create_transplant_job(trans_type=TransplantorType.PHASE_3_4_TRANSPLANTOR):
        transplanter_found = None
        if trans_type == TransplantorType.PHASE_3_4_TRANSPLANTOR:
            transplanter_found = Transplanter(TransplantorFactory.get_transplanter_3_4())
            if transplanter_found.ready_to_transplant():
                trans_job_1 = TransplantJob(id=1)
                trans_job_1.set_transplanter(transplanter_found)
                TransplantJob.transplant_job_list.append(trans_job_1)
            else:
                logger.info("Transplanter is not ready")
        elif trans_type == TransplantorType.PHASE_4_5_TRANSPLANTOR:
            transplanter_found = TransplantorFactory.get_transplantor_4_5()
            if transplanter_found.ready_to_transplant():
                trans_job_2 = TransplantJob(id=2)
                trans_job_2.set_transplanter(transplanter_found)
                TransplantJob.transplant_job_list[2] = trans_job_2
            else:
                logger.info("PHASE_4_5_TRANSPLANTOR is not ready")
        if transplanter_found is None:
            raise Exception("Invalid transplantor")

    def __init__(self, id=-1, type_name='Default'):
        self._destination_trays = None
        self._source_tray = None
        self._destination_tray = None
        self._transplantor = None

    def set_transplanter(self, transplantor):
        self._transplantor = transplantor

    def set_source_tray(self, tray):
        self._source_tray = tray

    def set_destination_tray(self, tray):
        self._destination_trays = tray

    def transplant(self):
        if self._source_tray is None:
            raise Exception("Source tray not specified")
        if len(self._destination_trays) == 0:
            raise Exception("Destinations trays not specified")

        p = Process(target=TransplantJob.execute_transplant, args=(self._source_tray, self._destination_trays))
        p.start()
        p.join()

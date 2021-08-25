from ellemento.job import job_main, transfer_job
from ellemento.job import light_job
from ellemento.model.light_control import LightControl
from ellemento.job.tansplant_job import TransplantJob 
from ellemento.model.tray_factory import Tray 
import unittest


class TestTransplantJob(unittest.TestCase):

    def test_transplant(self):
        tr_job = TransplantJob()
        tray = Tray(id = 1, type_name= "Phase1-3")
        tray.location = "sower"
        print("Tansfer job")
        tr_job.set_source_tray(tray)

        tray2 = Tray(id = 2, type_name= "Phase4")
        tray3 = Tray(id = 3, type_name= "Phase4")
        tray_list = [tray2, tray3]

        tr_job.set_destination_tray(tray_list)
        tr_job.transplant()

        # After transplanting, the input tray will not have any plants 
        self.assertEqual(tray.has_veg, False)

        # After transplating, the output tray shall have plants 
        for obj in tray_list: 
            #print(obj)
            self.assertEqual(obj.has_veg, True)

        

if __name__ == '__main__':
    unittest.main()
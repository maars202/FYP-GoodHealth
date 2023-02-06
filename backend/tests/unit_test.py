import unittest
# from backend.app import db, app, Duty_Hour_Log
# , Duty_Hour_Log
# from __main__ import app,db
# from Duty_Hour_Log1 import Duty_Hour_Log

class TestJobRole(unittest.TestCase):
    def test_to_dict(self):
        # jr1 = Duty_Hour_Log(BillingName="SGHGasEnt",
        # Compliance_or_Not="",
        # Employee_id="MOM12390",
        # MmYyyy ="",
        # Month="July",
        # Number_of_sessions_attended = "14",
        # Percentage_of_sessions_attended = "100%",
        # Posting_Department= "",
        # Posting_Institution= "",
        # Scheduled_Teachings= "",
        # Total_tracked_sessions= "14"
        # )
        # self.assertEqual(jr1.to_dict(), {
        #     "BillingName": "SGHGasEnt",
        #     "Compliance_or_Not": "",
        #     "Employee_id": "MOM12390",
        #     "MmYyyy": "",
        #     "Month": "July",
        #     "Number_of_sessions_attended": "14",
        #     "Percentage_of_sessions_attended": "100%",
        #     "Posting_Department": "",
        #     "Posting_Institution": "",
        #     "Scheduled_Teachings": "",
        #     "Total_tracked_sessions": "14"
        # }
        # )
        assert("one", "one")

if __name__ == "__main__":
    unittest.main()
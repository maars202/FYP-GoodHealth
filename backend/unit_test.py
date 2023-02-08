import unittest
import pytest
# from app import db, app
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import Flask
# , Duty_Hour_Log
# from __main__ import app,db


class TestDutyHourLogRole(unittest.TestCase):
    def test_to_dict(self):
        # import Duty_Hour_Log1
        
        # from Duty_Hour_Log import Duty_Hour_Log
        from app import Duty_Hour_Log
        jr1 = Duty_Hour_Log(
            MCR_No = "1234o19",
            Level = "4",
            Logged_for_month = "Yes",
            MMYYYY = "Mar-20",
            Submitted = "3",
            Submitted_Proportion = "1"
            )
        self.assertEqual(jr1.to_dict(), {
            "Level": "4",
            "Logged_for_month": "Yes",
            "MCR_No": "1234o19",
            "MMYYYY": "Mar-20",
            "Submitted": "3",
            "Submitted_Proportion": "1",
            "id": None
        }
        )
        # assert("onde", "one")

if __name__ == "__main__":
    unittest.main()
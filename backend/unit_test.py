import unittest
import pytest
# from app import db, app
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import Flask
# , Duty_Hour_Log
# from __main__ import app,db

def create_app():
    app = Flask(__name__)
    print("app initialising")
    app.app_context().push()
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(app)
    db.create_all()

    CORS(app)
    return [db, app]


@pytest.fixture(scope='module')
def test_client():
    # Create a Flask app configured for testing
    appData = create_app()
    flask_app = appData[0]
    db = appData[1]
    flask_app.config.from_object('config.TestingConfig')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!



class TestJobRole(unittest.TestCase):
    def test_to_dict(self):
        # import Duty_Hour_Log1
        
        from Duty_Hour_Log1 import Duty_Hour_Log
        # from app import Duty_Hour_Log
        jr1 = Duty_Hour_Log(Employee_id= "MOM12390",
            Level= "4",
            Logged_for_month= "Yes",
            MMYYYY= "Mar-20",
            Submitted= "3",
            Submitted_Proportion= "0.5")
        self.assertEqual(jr1.to_dict(), {"Employee_id": "MOM12390",
            "Level": "4",
            "Logged_for_month": "Yes",
            "MMYYYY": "Mar-20",
            "Submitted": "3",
            "Submitted_Proportion": "0.5"}
        )
        # assert("onde", "one")

if __name__ == "__main__":
    unittest.main()
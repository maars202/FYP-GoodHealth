import unittest
import flask_testing
import pytest
import json
from .app4 import app, db, Personal_Details

class TestApp(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


# CREATE LEARNING JOURNEY:
class TestCreateLearningJourney(TestApp):

    def test_read_jobrole(self):
        data ={
            "ACLS_Expiry_Date": None,
            "Academic_Clinical_Programme": "Medicine",
            "Academic_Year": "2022",
            "BCLS_Expiry_Date": None,
            "Building_Name": "",
            "Contact_No_Personal": "91515780",
            "Contact_No_Work": "",
            "Covid_19_Vaccination_Status": "Yes",
            "Date_of_Birth": "Thu, 05 Dec 1991 00:00:00 GMT",
            "Date_of_First_Dose": "Tue, 09 Feb 2021 00:00:00 GMT",
            "Date_of_Second_Dose": "Tue, 02 Mar 2021 00:00:00 GMT",
            "Department": "Residency",
            "Designation": "Senior Resident",
            "Email_Official": "hyunbin.kang@mohh.com.sg",
            "Email_Personal": "",
            "Employee_id": "MOM05690",
            "Employment_Status": "Active",
            "Gender": "Male",
            "House_Blk_No": "",
            "Institution": "MOHH",
            "MCR_No": "M88791Z",
            "Nationality": "Singaporean",
            "Personal_Details_deleted": False,
            "Postal_Code": "536000",
            "Programme": "Gastroenterology",
            "Registration_Type": "Full",
            "Staff_Name": "Kang Hyun Bin",
            "Street": "Lorong Gambir",
            "Unit_No": "",
            "Vaccination_Remarks": "",
            "Year_of_Training": "SR3"
        }
       
        skill = Personal_Details(**data)
        db.session.add(skill)
        db.session.commit()

        response = self.client.get("/personal_details_table")
        self.assertEqual(response.status_code, 200)
        print(f"response.json: {response.json}")
        self.assertEqual(response.json,{
    "data": [
        {
            "ACLS_Expiry_Date": None,
            "Academic_Clinical_Programme": "Medicine",
            "Academic_Year": "2022",
            "BCLS_Expiry_Date": None,
            "Building_Name": "",
            "Contact_No_Personal": "91515780",
            "Contact_No_Work": "",
            "Covid_19_Vaccination_Status": "Yes",
            "Date_of_Birth": "Thu, 05 Dec 1991 00:00:00 GMT",
            "Date_of_First_Dose": "Tue, 09 Feb 2021 00:00:00 GMT",
            "Date_of_Second_Dose": "Tue, 02 Mar 2021 00:00:00 GMT",
            "Department": "Residency",
            "Designation": "Senior Resident",
            "Email_Official": "hyunbin.kang@mohh.com.sg",
            "Email_Personal": "",
            "Employee_id": "MOM05690",
            "Employment_Status": "Active",
            "Gender": "Male",
            "House_Blk_No": "",
            "Institution": "MOHH",
            "MCR_No": "M88791Z",
            "Nationality": "Singaporean",
            "Personal_Details_deleted": False,
            "Postal_Code": "536000",
            "Programme": "Gastroenterology",
            "Registration_Type": "Full",
            "Staff_Name": "Kang Hyun Bin",
            "Street": "Lorong Gambir",
            "Unit_No": "",
            "Vaccination_Remarks": "",
            "Year_of_Training": "SR3"
        }]})


if __name__ == '__main__':
    unittest.main()
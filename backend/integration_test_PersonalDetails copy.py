import unittest
import flask_testing
import pytest
import json
from app import app, db, Personal_Details

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


# Read Personal_Details:
class TestReadPersonalDetails(TestApp):

    def test_read_personal_details(self):
        data ={
            "ACLS_Expiry_Date": "",
            "Academic_Clinical_Programme": "",
            "Academic_Year": "",
            "BCLS_Expiry_Date": "",
            "Building_Name": "",
            "Contact_No_Personal": "",
            "Contact_No_Work": "",
            "Covid_19_Vaccination_Status": "",
            "Date_of_Birth": "",
            "Date_of_First_Dose": "",
            "Date_of_Second_Dose": "",
            "Department": "",
            "Designation": "",
            "Email_Official": "",
            "Email_Personal": "",
            "Employee_ID": "1234o18",
            "Employment_Status": "",
            "Gender": "",
            "House_Blk_No": "",
            "Institution": "dkjn",
            "MCR_No": "1234o18",
            "Nationality": "",
            "Postal_Code": "",
            "Programme": "",
            "Registration_Type": "",
            "Staff_Name": "kevjn",
            "Street": "",
            "Unit_No": "",
            "Vaccination_Remarks": "",
            "Year_of_Training": ""
        }
       
        skill = Personal_Details(**data)
        db.session.add(skill)
        db.session.commit()

        response = self.client.get("/personaldetails")
        self.assertEqual(response.status_code, 200)
        print(f"response.json: {response.json}")
        self.assertEqual(response.json,{
    "data": [{
            "ACLS_Expiry_Date": "",
            "Academic_Clinical_Programme": "",
            "Academic_Year": "",
            "BCLS_Expiry_Date": "",
            "Building_Name": "",
            "Contact_No_Personal": "",
            "Contact_No_Work": "",
            "Covid_19_Vaccination_Status": "",
            "Date_of_Birth": "",
            "Date_of_First_Dose": "",
            "Date_of_Second_Dose": "",
            "Department": "",
            "Designation": "",
            "Email_Official": "",
            "Email_Personal": "",
            "Employee_ID": "1234o18",
            "Employment_Status": "",
            "Gender": "",
            "House_Blk_No": "",
            "Institution": "dkjn",
            "MCR_No": "1234o18",
            "Nationality": "",
            "Postal_Code": "",
            "Programme": "",
            "Registration_Type": "",
            "Staff_Name": "kevjn",
            "Street": "",
            "Unit_No": "",
            "Vaccination_Remarks": "",
            "Year_of_Training": ""
        } ]})

if __name__ == '__main__':
    unittest.main()
import unittest
import flask_testing
import pytest
import json
from app import app, db, Personal_Details, Presentations

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
class TestReadPresentation(TestApp):

    def test_create_personal_details(self):
        personal_details_data = [{
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
        }, {
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
            "Employee_ID": "1234o19",
            "Employment_Status": "",
            "Gender": "",
            "House_Blk_No": "",
            "Institution": "dkjn",
            "MCR_No": "1234o19",
            "Nationality": "",
            "Postal_Code": "",
            "Programme": "",
            "Registration_Type": "",
            "Staff_Name": "kevjn",
            "Street": "",
            "Unit_No": "",
            "Vaccination_Remarks": "",
            "Year_of_Training": ""
        }]

        for data in personal_details_data:
            person1 = Personal_Details(**data)
            db.session.add(person1)
            db.session.commit()

        response = self.client.get("/personaldetails")
        self.assertEqual(response.status_code, 200)
        print(f"response.json: {response.json}")
        self.assertEqual(response.json,{
    "data": [
        {
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
        },
        {
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
            "Employee_ID": "1234o19",
            "Employment_Status": "",
            "Gender": "",
            "House_Blk_No": "",
            "Institution": "dkjn",
            "MCR_No": "1234o19",
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
    ]})

    def test_create_presentations(self):

        all_presentations_data = [
        {
            "Conference_Name": "Conference_Name111",
            "Country": "Country111",
            "MCR_No": "1234o19",
            "Presentation_Date": "Presentation_Date111",
            "Project_ID": "Project_ID111",
            "Title": "Title111",
            "Type": "Type111"
        }
    ]
        for data in all_presentations_data:
            presentation = Presentations(**data)
            db.session.add(presentation)
            db.session.commit()

        response = self.client.get("/presentations")
        self.assertEqual(response.status_code, 200)
        print(f"created presentation response.json: {response.json}")
        self.assertEqual(response.json,{
        "data": [
        {
            "Conference_Name": "Conference_Name111",
            "Country": "Country111",
            "MCR_No": "1234o19",
            "Presentation_Date": "Presentation_Date111",
            "Project_ID": "Project_ID111",
            "Title": "Title111",
            "Type": "Type111",
            "id": 1
        }
    ]})




    def test_read_presentation_by_person(self):

        personal_details_data = [{
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
        }, {
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
            "Employee_ID": "1234o19",
            "Employment_Status": "",
            "Gender": "",
            "House_Blk_No": "",
            "Institution": "dkjn",
            "MCR_No": "1234o19",
            "Nationality": "",
            "Postal_Code": "",
            "Programme": "",
            "Registration_Type": "",
            "Staff_Name": "kevjn",
            "Street": "",
            "Unit_No": "",
            "Vaccination_Remarks": "",
            "Year_of_Training": ""
        }]

        for data in personal_details_data:
            person1 = Personal_Details(**data)
            db.session.add(person1)
            db.session.commit()

        all_presentations_data = [
        {
            "Conference_Name": "Conference_Name111",
            "Country": "Country111",
            "MCR_No": "1234o19",
            "Presentation_Date": "Presentation_Date111",
            "Project_ID": "Project_ID111",
            "Title": "Title111",
            "Type": "Type111"
        }
    ]
        for data in all_presentations_data:
            presentation = Presentations(**data)
            db.session.add(presentation)
            db.session.commit()

        response = self.client.get("/presentations/1234o19")
        self.assertEqual(response.status_code, 200)
        print(f"response.json: {response.json}")
        self.assertEqual(response.json,
        {
    "data": [
        {
            "Conference_Name": "Conference_Name111",
            "Country": "Country111",
            "MCR_No": "1234o19",
            "Presentation_Date": "Presentation_Date111",
            "Project_ID": "Project_ID111",
            "Title": "Title111",
            "Type": "Type111",
            "id": 1
        }
        ]
    })

    # def test_cannot_create_presentation_if_mcr_not_present(self):
    #     assert(True, True)


    

if __name__ == '__main__':
    unittest.main()
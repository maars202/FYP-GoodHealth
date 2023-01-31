
from __main__ import app,db
from flask import request, jsonify

class PersonalDetails(db.Model):
    __tablename__ = 'PersonalDetails'
    Employee_id = db.Column(db.String(100), primary_key=True)
    MCR_No = db.Column(db.String(100))
    Staff_Name = db.Column(db.String(100))
    Designation = db.Column(db.String(100))

    Programme = db.Column(db.String(100))
    Year_of_Training = db.Column(db.String(100))
    Academic_Year = db.Column(db.Integer)
    Department = db.Column(db.String(100))

    Institution = db.Column(db.String(100))
    Academic_Clinical_Programme = db.Column(db.String(100))
    Employment_Status = db.Column(db.String(100))
    Nationality = db.Column(db.String(100))
    Date_of_Birth = db.Column(db.DateTime)

    Gender = db.Column(db.String(100))
    Registration_Type = db.Column(db.String(100))
    House_Blk_No = db.Column(db.String(100))
    Street = db.Column(db.String(100))
    Building_Name = db.Column(db.String(100))
    Unit_No = db.Column(db.String(100))
    Postal_Code = db.Column(db.String(100))
    Contact_No_Work = db.Column(db.String(100))
    Contact_No_Personal = db.Column(db.String(100))

    Email_Official = db.Column(db.String(100))
    Email_Personal = db.Column(db.String(100))
    BCLS_Expiry_Date = db.Column(db.DateTime)
    ACLS_Expiry_Date = db.Column(db.DateTime)
    Covid_19_Vaccination_Status = db.Column(db.String(100))
    Date_of_First_Dose = db.Column(db.DateTime)
    Date_of_Second_Dose = db.Column(db.DateTime)
    Vaccination_Remarks = db.Column(db.String(100))

    __mapper_args__ = {
        'polymorphic_identity': 'PersonalDetails'
    }

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        print(f"columns: {columns}")
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result
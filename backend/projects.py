
from flask import request, jsonify
from __main__ import app,db



class PersonalDetails(db.Model):
    __tablename__ = 'PersonalDetails'

    Employee_id = db.Column(db.String(100), primary_key=True)
    MCR_No = db.Column(db.Integer)
    Staff_Name = db.Column(db.String(100))
    designation = db.Column(db.String(100))
    Department = db.Column(db.String(100))
    institution = db.Column(db.String(100))
    BCLS_Expiry_Date = db.Column(db.DateTime)
    ACLS_Expiry_Date = db.Column(db.DateTime)
 
    Covid_19_Vaccination_Status = db.Column(db.String(100))
    Date_of_First_Dose = db.Column(db.DateTime)
    Date_of_Second_Dose = db.Column(db.DateTime)
    Vaccination_Remarks = db.Column(db.String(100))

    Year_of_Graduation = db.Column(db.Integer)
    Date_of_Graduation = db.Column(db.DateTime)
    Basic_Qualification = db.Column(db.String(100))
    Medical_School = db.Column(db.String(100))

    Country_of_Graduation = db.Column(db.String(100))
    IM_Residency_Start_Date = db.Column(db.DateTime)
    IM_Residency_End_Date = db.Column(db.DateTime)
    SR_Residency_Programme = db.Column(db.String(100))

    SR_Residency_Start_Date = db.Column(db.DateTime)
    PG_Year = db.Column(db.Integer)

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

# Read Existing personaldetails (R)
@app.route("/personaldetails")
def read_personaldetails():
    pdList = PersonalDetails.query.all()
    return jsonify(
        {
            "data": [pd.to_dict()
                    for pd in pdList]
        }
    ), 200






class Project(db.Model):
    __tablename__ = 'Projects'

    Project_ID= db.Column(db.String(100), primary_key=True)
    Employee_id = db.Column(db.String(100),  db.ForeignKey('PersonalDetails.Employee_id'))
    Project_Type = db.Column(db.String(100))

    Project_Title = db.Column(db.String(100))
    StartDate = db.Column(db.DateTime)
    EndDate = db.Column(db.DateTime)
    PMID = db.Column(db.String(100))


    __mapper_args__ = {
        'polymorphic_identity': 'Projects'
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

# Read Existing personaldetails (R)
@app.route("/projects")
def read_projects():
    pdList = Project.query.all()
    print (pdList,'oierjngosenrboaeir!!!!!!!!!!!!!!!!!!!!!!OSJNWOJN')
    return jsonify(
        {
            "data": [pd.to_dict()
                    for pd in pdList]
        }
    ), 200
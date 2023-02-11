from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json
import pandas as pd
import traceback

app = Flask(__name__)
# # Mac user ====================================================================
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:' + \
#                                         '@localhost:3306/SingHealth'
# # =============================================================================


# # Windows user -------------------------------------------------------------------
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root' + \
# #                                         '@localhost:3306/SingHealth'
# # --------------------------------------------------------------------------------
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
#                                         'pool_recycle': 280}

# db = SQLAlchemy(app)

# CORS(app)
app = Flask(__name__)
app.app_context().push()

if __name__ == '__main__':
    print("running on main")
    # Mac user -------------------------------------------------------------------
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root' + \
                                            '@localhost:3306/SingHealth'
    # --------------------------------------------------------------------------------

    # # Windows user -------------------------------------------------------------------
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root' + \
    #                                         '@localhost:3306/SingHealth'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
    #                                         'pool_recycle': 280}
else:
    print("running not on main")
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)
    
#Read PersonalDetails field/column name (R)
@app.route('/', methods=['GET'])
def display():
    return render_template('homepage2.html')


class Personal_Details(db.Model):
    __tablename__ = 'Personal_Details'
    Employee_ID = db.Column(db.String(50), primary_key=True)
    MCR_No = db.Column(db.String(50))
    Staff_Name = db.Column(db.String(50))
    Designation = db.Column(db.String(50))

    Programme = db.Column(db.String(50))
    Year_of_Training = db.Column(db.String(50))
    Academic_Year = db.Column(db.String(50))
    Department = db.Column(db.String(50))

    Institution = db.Column(db.String(50))
    Academic_Clinical_Programme = db.Column(db.String(50))
    Employment_Status = db.Column(db.String(50))
    Nationality = db.Column(db.String(50))
    Date_of_Birth = db.Column(db.String(50))

    Gender = db.Column(db.String(50))
    Registration_Type = db.Column(db.String(50))
    House_Blk_No = db.Column(db.String(50))
    Street = db.Column(db.String(50))
    Building_Name = db.Column(db.String(50))
    Unit_No = db.Column(db.String(50))
    Postal_Code = db.Column(db.String(50))
    Contact_No_Work = db.Column(db.String(50))
    Contact_No_Personal = db.Column(db.String(50))

    Email_Official = db.Column(db.String(50))
    Email_Personal = db.Column(db.String(50))
    BCLS_Expiry_Date = db.Column(db.String(50))
    ACLS_Expiry_Date = db.Column(db.String(50))
    Covid_19_Vaccination_Status = db.Column(db.String(50))
    Date_of_First_Dose = db.Column(db.String(50))
    Date_of_Second_Dose = db.Column(db.String(50))
    Vaccination_Remarks = db.Column(db.String(50))

    presentations = db.relationship('Presentations', backref='Personal_Details')
    posting_histories = db.relationship('Posting_History', backref='Personal_Details')
    duty_hour_logs = db.relationship('Duty_Hour_Log', backref='Personal_Details')
    case_logs = db.relationship('Case_Log', backref='Personal_Details')
    procedure_logs = db.relationship('Procedure_Log', backref='Personal_Details')
    exam_histories = db.relationship('Exam_History', backref='Personal_Details')
    publications = db.relationship('Publications', backref='Personal_Details')
    evaluations = db.relationship('Evaluations', backref='Personal_Details')
    trgExtRem_Histories = db.relationship('TrgExtRem_History', backref='Personal_Details')
    projects = db.relationship('Projects', backref='Personal_Details')
    awards = db.relationship('Awards', backref='Personal_Details')
    grants = db.relationship('Grants', backref='Personal_Details')
    ihis = db.relationship('IHI', backref='Personal_Details')
    involvements = db.relationship('Involvement', backref='Personal_Details')


    __mapper_args__ = {
        'polymorphic_identity': 'Personal_Details'
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

class Presentations(db.Model):
    __tablename__ = 'Presentations'
    id=db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    MCR_No = db.Column(db.String(100),  db.ForeignKey('Personal_Details.MCR_No'))
    Title = db.Column(db.String(100))
    Conference_Name = db.Column(db.String(100))
    Type = db.Column(db.String(100))
    Project_ID = db.Column(db.String(100))
    Country = db.Column(db.String(100))
    Presentation_Date = db.Column(db.String(100))

    __mapper_args__ = {
        'polymorphic_identity': 'Presentations'
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


class Posting_History(db.Model):
    __tablename__ = 'Posting_History'
    id=db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    MCR_No = db.Column(db.String(100),  db.ForeignKey('Personal_Details.MCR_No'))
    Posting_Institution = db.Column(db.String(100))
    Posting_Department = db.Column(db.DateTime)
    Posting_StartDate = db.Column(db.DateTime)
    Posting_EndDate = db.Column(db.String(100))

    __mapper_args__ = {
        'polymorphic_identity': 'Posting_History'
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


class Duty_Hour_Log(db.Model):
    __tablename__ = 'Duty_Hour_Log'
    id=db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    MCR_No = db.Column(db.String(100),  db.ForeignKey('Personal_Details.MCR_No'))
    Level = db.Column(db.String(100))
    Submitted = db.Column(db.String(100))
    Submitted_Proportion = db.Column(db.String(100))
    MMYYYY = db.Column(db.String(100))
    Logged_for_month = db.Column(db.String(100))

    __mapper_args__ = {
        'polymorphic_identity': 'Duty_Hour_Log'
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

class Case_Log(db.Model):
    __tablename__ = 'Case_Log'
    id=db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    MCR_No = db.Column(db.String(100),  db.ForeignKey('Personal_Details.MCR_No'))
    Case_Name = db.Column(db.String(100))
    Subspecialty = db.Column(db.String(100))
    Type_of_Case_Log = db.Column(db.String(100))
    Date_of_Log = db.Column(db.String(100))
    CPT = db.Column(db.String(100))
    Total = db.Column(db.String(100))
    Performed = db.Column(db.String(100))
    Observed = db.Column(db.String(100))
    Verified = db.Column(db.String(100))
    Certified = db.Column(db.String(100))
 
    __mapper_args__ = {
        'polymorphic_identity': 'Case_Log'
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


class Procedure_Log(db.Model):
    __tablename__ = 'Procedure_Log'
    id=db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    MCR_No = db.Column(db.String(100),  db.ForeignKey('Personal_Details.MCR_No'))
    Procedure_Name = db.Column(db.String(100))
    Date_of_Completion = db.Column(db.String(100))
    CPT = db.Column(db.String(100))
    Total = db.Column(db.String(100))
    Performed = db.Column(db.String(100))
    Observed = db.Column(db.String(100))
    Verified = db.Column(db.String(100))
    Certified = db.Column(db.String(100))

    __mapper_args__ = {
        'polymorphic_identity': 'Procedure_Log'
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

class Exam_History(db.Model):
    __tablename__ = 'Exam_History'
    id=db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    MCR_No = db.Column(db.String(100),  db.ForeignKey('Personal_Details.MCR_No'))
    Name_of_Exam = db.Column(db.String(100))
    Date_of_Attempt = db.Column(db.String(100))
    Exam_Status = db.Column(db.String(100))

    __mapper_args__ = {
        'polymorphic_identity': 'Exam_History'
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


class Publications(db.Model):
    __tablename__ = 'Publications'
    id=db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    MCR_No = db.Column(db.String(100),  db.ForeignKey('Personal_Details.MCR_No'))
    
    Publication_Title = db.Column(db.String(100))
    Journal_Title = db.Column(db.String(100))
    
    PMID = db.Column(db.String(100))
    Publication_Date = db.Column(db.DateTime)
    
    __mapper_args__ = {
        'polymorphic_identity': 'Publications'
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


class Evaluations(db.Model):
    __tablename__ = 'Evaluations'
    id=db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    MCR_No = db.Column(db.String(100),  db.ForeignKey('Personal_Details.MCR_No'))
    Year_of_Training = db.Column(db.String(100))
    Rotation_Period = db.Column(db.String(100))
    Name_of_Evaluation_Form = db.Column(db.String(100))
    Question_Number = db.Column(db.String(100))
    Score = db.Column(db.String(100))
    Evaluator = db.Column(db.String(100))
    Service = db.Column(db.String(100))
    Answer = db.Column(db.String(100))

    __mapper_args__ = {
        'polymorphic_identity': 'Evaluations'
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


class TrgExtRem_History(db.Model):
    __tablename__ = 'TrgExtRem_History'
    id=db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    MCR_No = db.Column(db.String(100),  db.ForeignKey('Personal_Details.MCR_No'))
    LOAPIP = db.Column(db.String(100))

    StartDate = db.Column(db.DateTime)
    EndDate = db.Column(db.DateTime)

    __mapper_args__ = {
        'polymorphic_identity': 'TrgExtRem_History'
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


class Projects(db.Model):
    __tablename__ = 'Projects'
    id=db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    MCR_No = db.Column(db.String(100),  db.ForeignKey('Personal_Details.MCR_No'))
    Project_Type = db.Column(db.String(100))
    Project_Title = db.Column(db.String(100))
    Project_ID=db.Column(db.String(100))
    Start_Date = db.Column(db.DateTime)
    End_Date = db.Column(db.DateTime)
    Date_of_QI_Certification= db.Column(db.String(100))
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


class Awards(db.Model):
    __tablename__ = 'Awards'
    id=db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    MCR_No = db.Column(db.String(100),  db.ForeignKey('Personal_Details.MCR_No'))
    Award_Category = db.Column(db.String(100))
    Name_of_Award = db.Column(db.String(100))

    FY_of_Award_Received = db.Column(db.String(100))
    Date_of_Award_Received = db.Column(db.String(100))
    Project_ID = db.Column(db.String(100))

    __mapper_args__ = {
        'polymorphic_identity': 'Awards'
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


class Grants(db.Model):
    __tablename__ = 'Grants'
    id=db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    MCR_No = db.Column(db.String(100),  db.ForeignKey('Personal_Details.MCR_No'))
    Name_of_Grant = db.Column(db.String(100))
    Project_Title = db.Column(db.String(100))
    Project_ID = db.Column(db.String(100))
    Grant_End_Date = db.Column(db.DateTime)
    Grant_Start_Date = db.Column(db.DateTime)

    __mapper_args__ = {
        'polymorphic_identity': 'Grants'
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


class IHI(db.Model):
    __tablename__ = 'IHI'
    id=db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    MCR_No = db.Column(db.String(100),  db.ForeignKey('Personal_Details.MCR_No'))
    Completion_of_Emodules = db.Column(db.String(100))
    Date = db.Column(db.String(100))

    __mapper_args__ = {
        'polymorphic_identity': 'IHI'
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


class Involvement(db.Model):
    __tablename__ = 'Involvement'
    id=db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    Involvement_Type = db.Column(db.String(100))
    MCR_No = db.Column(db.String(100),  db.ForeignKey('Personal_Details.MCR_No'))
    Event = db.Column(db.String(100))
    Role = db.Column(db.String(100))
    Start_Date = db.Column(db.DateTime)
    End_Date = db.Column(db.DateTime)

    __mapper_args__ = {
        'polymorphic_identity': 'Involvement'
    }

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

# https://fsymbols.com/generators/tarty/
# ============================
# █▀█ █▀▀ █▀█ █▀ █▀█ █▄░█ ▄▀█ █░░   █▀▄ █▀▀ ▀█▀ ▄▀█ █ █░░ █▀
# █▀▀ ██▄ █▀▄ ▄█ █▄█ █░▀█ █▀█ █▄▄   █▄▀ ██▄ ░█░ █▀█ █ █▄▄ ▄█
# █▀ ▀█▀ ▄▀█ █▀█ ▀█▀
# ▄█ ░█░ █▀█ █▀▄ ░█░
# ============================
# AKA Personal_Details table routes:
# Read Existing personaldetails (R)
@app.route("/personaldetails")
def read_personaldetails():
    pdList = Personal_Details.query.all()
    return jsonify(
        {
            "data": [pd.to_dict()
                    for pd in pdList]
        }
    ), 200

# Read PersonalDetails field/column name (R)
@app.route('/personal_details_fields', methods=['GET'])
def get_personal_details_fields():
    fields = {}
    for column in Personal_Details.__table__.columns:
        fields[column.name] = str(column.type)
    return jsonify(fields)

# Add personaldetails
@app.route('/add_personal_detail', methods=['POST'])
def create_personal_detail():
    data = request.get_json()
    print(data)
    if not all(key in data.keys() for key in ('Employee_ID', 'MCR_No', "Staff_Name" , "Designation" , "Programme",
                "Year_of_Training" , "Academic_Year" , "Department" , "Institution" , 
                "Academic_Clinical_Programme" , "Employment_Status" , "Nationality" ,"Date_of_Birth" , "Gender",
                "Registration_Type", "House_Blk_No" , "Street" , "Building_Name" , "Unit_No" , "Postal_Code" ,"Contact_No_Work",
                "Contact_No_Personal", "Email_Official" ,"Email_Personal", "BCLS_Expiry_Date","ACLS_Expiry_Date",
                "Covid_19_Vaccination_Status" , "Date_of_First_Dose" ,"Date_of_Second_Dose" ,"Vaccination_Remarks"
                )):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    personalDetails = Personal_Details(**data)
    try:
        db.session.add(personalDetails)
        db.session.commit()
        return jsonify(personalDetails.to_dict()), 201
    except Exception as e:
        print("An error occurred:", e)
        print("Stack trace:")
        traceback.print_exc()
    # except Exception:
    #     return jsonify({
    #         "message": "Unable to commit to database."
    #     }), 500


# ============================
# █▀▀ █▄░█ █▀▄
# ██▄ █░▀█ █▄▀
# ============================

# ============================
# █ █▄░█ █░█ █▀█ █░░ █░█ █▀▀ █▀▄▀█ █▀▀ █▄░█ ▀█▀
# █ █░▀█ ▀▄▀ █▄█ █▄▄ ▀▄▀ ██▄ █░▀░█ ██▄ █░▀█ ░█░
# █▀ ▀█▀ ▄▀█ █▀█ ▀█▀
# ▄█ ░█░ █▀█ █▀▄ ░█░
# ============================
# AKA Involvement table routes:
# Read Existing involvement (R)
@app.route("/involvement")
def read_involvement():
    involvementList = Involvement.query.all()
    return jsonify(
        {
            "data": [pd.to_dict()
                     for pd in involvementList]
        }
    ), 200
# Read Involvement field/column name (R)

@app.route('/involvement_fields', methods=['GET'])
def get_involvement_fields():
    fields = {}
    for column in Involvement.__table__.columns:
        fields[column.name] = str(column.type)
    return jsonify(fields)

# Read Existing by Person (R)
@app.route("/involvement/<id>")
def read_involvement_by_person(id):
    person = Personal_Details.query.get_or_404(id)
    involvements_of_person = person.involvements
    return jsonify(
        {
            "data": [pd.to_dict()
                    for pd in involvements_of_person]
        }
    ), 200
# ============================
# █▀▀ █▄░█ █▀▄
# ██▄ █░▀█ █▄▀
# ============================

# ============================
# █░█ █ █▀ ▀█▀ █▀█ █▀█ █▄█ ▄▄ █▀▀ █▀▄ █░█ █▀▀ ▄▀█ ▀█▀ █ █▀█ █▄░█
# █▀█ █ ▄█ ░█░ █▄█ █▀▄ ░█░ ░░ ██▄ █▄▀ █▄█ █▄▄ █▀█ ░█░ █ █▄█ █░▀█
# █▀ ▀█▀ ▄▀█ █▀█ ▀█▀
# ▄█ ░█░ █▀█ █▀▄ ░█░
# ============================
# AKA Education_History table routes:


# ============================
# █▀▀ █▄░█ █▀▄
# ██▄ █░▀█ █▄▀
# ============================

# ============================
# █░█ █ █▀ ▀█▀ █▀█ █▀█ █▄█ ▄▄ █▀█ █▀█ █▀ ▀█▀ █ █▄░█ █▀▀
# █▀█ █ ▄█ ░█░ █▄█ █▀▄ ░█░ ░░ █▀▀ █▄█ ▄█ ░█░ █ █░▀█ █▄█
# █▀ ▀█▀ ▄▀█ █▀█ ▀█▀
# ▄█ ░█░ █▀█ █▀▄ ░█░
# ============================
# AKA Posting_History table routes:
# Read Existing  (R)
@app.route("/postinghistory")
def read_postinghistory():
    pdList = Posting_History.query.all()
    return jsonify(
        {
            "data": [pd.to_dict()
                    for pd in pdList]
        }
    ), 200

# Read Existing by Person (R)
@app.route("/postinghistory/<id>")
def read_postinghistory_by_person(id):
    person = Personal_Details.query.get_or_404(id)
    presentation_of_person = person.posting_histories
    return jsonify(
        {
            "data": [pd.to_dict()
                    for pd in presentation_of_person]
        }
    ), 200


# ============================
# █▀▀ █▄░█ █▀▄
# ██▄ █░▀█ █▄▀
# ============================

# ============================
# █░█ █ █▀ ▀█▀ █▀█ █▀█ █▄█ ▄▄ █▀▀ ▀▄▀ ▄▀█ █▀▄▀█
# █▀█ █ ▄█ ░█░ █▄█ █▀▄ ░█░ ░░ ██▄ █░█ █▀█ █░▀░█
# █▀ ▀█▀ ▄▀█ █▀█ ▀█▀
# ▄█ ░█░ █▀█ █▀▄ ░█░
# ============================
# AKA history_exam table routes:


# ============================
# █▀▀ █▄░█ █▀▄
# ██▄ █░▀█ █▄▀
# ============================


# ============================
# █▀▀ ▀▄▀ ▄▀█ █▀▄▀█   █░█ █ █▀ ▀█▀ █▀█ █▀█ █▄█
# ██▄ █░█ █▀█ █░▀░█   █▀█ █ ▄█ ░█░ █▄█ █▀▄ ░█░
# █▀ ▀█▀ ▄▀█ █▀█ ▀█▀
# ▄█ ░█░ █▀█ █▀▄ ░█░
# ============================
# AKA exam_history table routes:

# Read Existing ExamHistory (R)
@app.route("/examhistory")
def read_examhistory():
    examhistoryList = Exam_History.query.all()
    return jsonify(
        {
            "data": [pd.to_dict()
                     for pd in examhistoryList]
        }
    ), 200

# Read ExamHistory field/column name (R)
@app.route('/exam_history_fields', methods=['GET'])
def get_exam_history_fields():
    fields = {}
    for column in Exam_History.__table__.columns:
        fields[column.name] = str(column.type)
    return jsonify(fields)

# Read Existing by Person (R)
@app.route("/examhistory/<id>")
def read_proceSSdurelog_by_person(id):
    person = Personal_Details.query.get_or_404(id)
    examhistory_of_person = person.exam_histories
    return jsonify(
        {
            "data": [pd.to_dict()
                    for pd in examhistory_of_person]
        }
    ), 200


# ============================
# █▀▀ █▄░█ █▀▄
# ██▄ █░▀█ █▄▀
# ============================

# ============================
# █░█ █ █▀ ▀█▀ █▀█ █▀█ █▄█ ▄▄ ▀█▀ █▀▀ █▀█
# █▀█ █ ▄█ ░█░ █▄█ █▀▄ ░█░ ░░ ░█░ ██▄ █▀▄
# █▀ ▀█▀ ▄▀█ █▀█ ▀█▀
# ▄█ ░█░ █▀█ █▀▄ ░█░
# ============================
# AKA  table routes:


# ============================
# █▀▀ █▄░█ █▀▄
# ██▄ █░▀█ █▄▀
# ============================

# ============================
# █▀▀ █▀█ ▄▀█ █▄░█ ▀█▀ █▀
# █▄█ █▀▄ █▀█ █░▀█ ░█░ ▄█
# █▀ ▀█▀ ▄▀█ █▀█ ▀█▀
# ▄█ ░█░ █▀█ █▀▄ ░█░
# ============================
# AKA grants table routes:
# Read Existing grants (R)
@app.route("/grants")
def read_grants():
    grantsList = Grants.query.all()
    return jsonify(
        {
            "data": [pd.to_dict()
                     for pd in grantsList]
        }
    ), 200

# Read Grants field/column name (R)
@app.route('/grants_fields', methods=['GET'])
def get_grants_fields():
    fields = {}
    for column in Grants.__table__.columns:
        fields[column.name] = str(column.type)
    return jsonify(fields)

# Read Existing by Person (R)
@app.route("/grants/<id>")
def read_grants_by_person(id):
    person = Personal_Details.query.get_or_404(id)
    grants_of_person = person.grants
    return jsonify(
        {
            "data": [pd.to_dict()
                    for pd in grants_of_person]
        }
    ), 200

# ============================
# █▀▀ █▄░█ █▀▄
# ██▄ █░▀█ █▄▀
# ============================

# ============================
# ▄▀█ █░█░█ ▄▀█ █▀█ █▀▄ █▀
# █▀█ ▀▄▀▄▀ █▀█ █▀▄ █▄▀ ▄█
# █▀ ▀█▀ ▄▀█ █▀█ ▀█▀
# ▄█ ░█░ █▀█ █▀▄ ░█░
# ============================
# AKA awards table routes:
# Read Existing awards (R)
@app.route("/awards")
def read_awards():
    awardsList = Awards.query.all()
    return jsonify(
        {
            "data": [pd.to_dict()
                     for pd in awardsList]
        }
    ), 200

# Read Awards field/column name (R)
@app.route('/awards_fields', methods=['GET'])
def get_awards_fields():
    fields = {}
    for column in Awards.__table__.columns:
        fields[column.name] = str(column.type)
    return jsonify(fields)

# Read Existing by Person (R)
@app.route("/awards/<id>")
def read_awards_by_person(id):
    person = Personal_Details.query.get_or_404(id)
    awards_of_person = person.awards
    return jsonify(
        {
            "data": [pd.to_dict()
                    for pd in awards_of_person]
        }
    ), 200

# Add awards
@app.route('/add_award', methods=['POST'])
def create_award():
    data = request.get_json()
    print(data)
    # MCR_No, Award_Category, Name_of_Award, FY_of_Award_Received, Date_of_Award_Received, Project_ID
    # if not all(key in data.keys() for key in ('MCR_No', 'Award_ID', 'Employee_id', "Award_Category" , "Name_of_Award" , "FY_of_Award_Received",
    #             "Date_of_Award_Received" , "Project_ID_Ref" 
    #             )):
    if not all(key in data.keys() for key in ('MCR_No', "Award_Category" , "Name_of_Award" , "FY_of_Award_Received",
                "Date_of_Award_Received" , "Project_ID" 
                )):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    awards = Awards(**data)
    try:
        db.session.add(awards)
        print("committing")
        db.session.commit()
        print("commited")
        return jsonify(awards.to_dict()), 201
    except Exception as e:
        print("An error occurred:", e)
        print("Stack trace:")
        traceback.print_exc()
    # except Exception:
    #     return jsonify({
    #         "message": "Unable to commit to database."
    #     }), 500


# ============================
# █▀▀ █▄░█ █▀▄
# ██▄ █░▀█ █▄▀
# ============================

# ============================
# █▀▄ █ █▀▄ ▄▀█ █▀▀ ▀█▀ █ █▀▀   ▄▀█ ▀█▀ ▀█▀ █▀▀ █▄░█ █▀▄ ▄▀█ █▄░█ █▀▀ █▀▀
# █▄▀ █ █▄▀ █▀█ █▄▄ ░█░ █ █▄▄   █▀█ ░█░ ░█░ ██▄ █░▀█ █▄▀ █▀█ █░▀█ █▄▄ ██▄
# █▀ ▀█▀ ▄▀█ █▀█ ▀█▀
# ▄█ ░█░ █▀█ █▀▄ ░█░
# ============================
# AKA didactic_attendance table routes:

# # Read Awards field/column name (R)
# @app.route('/didactic_attendance', methods=['GET'])
# def get_didactic_attendance():
#     daList = Didactic_Attendance.query.all()
#     return jsonify(
#         {
#             "data": [pd.to_dict()
#                      for pd in daList]
#         }
#     ), 200


# ============================
# █▀▀ █▄░█ █▀▄
# ██▄ █░▀█ █▄▀
# ============================

# ============================
# █▀█ █░█ █▄▄ █░░ █ █▀▀ ▄▀█ ▀█▀ █ █▀█ █▄░█ █▀
# █▀▀ █▄█ █▄█ █▄▄ █ █▄▄ █▀█ ░█░ █ █▄█ █░▀█ ▄█
# █▀ ▀█▀ ▄▀█ █▀█ ▀█▀
# ▄█ ░█░ █▀█ █▀▄ ░█░
# ============================
# AKA publications table routes:

# Read Existing  (R)
@app.route("/publications")
def read_publications():
    pdList = Publications.query.all()
    print (pdList,'oierjngosenrboaeir!!!!!!!!!!!!!!!!!!!!!!OSJNWOJN')
    return jsonify(
        {
            "data": [pd.to_dict()
                    for pd in pdList]
        }
    ), 200

# Read Existing by Person (R)
@app.route("/publications/<id>")
def read_publications_by_person(id):
    person = Personal_Details.query.get_or_404(id)
    publications_of_person = person.publications
    return jsonify(
        {
            "data": [pd.to_dict()
                    for pd in publications_of_person]
        }
    ), 200


# ============================
# █▀▀ █▄░█ █▀▄
# ██▄ █░▀█ █▄▀
# ============================

# ============================
# █▀█ █▀█ █▀█ ░░█ █▀▀ █▀▀ ▀█▀ █▀
# █▀▀ █▀▄ █▄█ █▄█ ██▄ █▄▄ ░█░ ▄█
# █▀ ▀█▀ ▄▀█ █▀█ ▀█▀
# ▄█ ░█░ █▀█ █▀▄ ░█░
# ============================
# AKA projects table routes:
# Read Existing personaldetails (R)
@app.route("/projects")
def read_projects():
    pdList = Projects.query.all()
    return jsonify(
        {
            "data": [pd.to_dict()
                    for pd in pdList]
        }
    ), 200

# Read Existing by Person (R)
@app.route("/projects/<id>")
def read_projects_by_person(id):
    person = Personal_Details.query.get_or_404(id)
    projects_of_person = person.projects
    return jsonify(
        {
            "data": [pd.to_dict()
                    for pd in projects_of_person]
        }
    ), 200


# ============================
# █▀▀ █▄░█ █▀▄
# ██▄ █░▀█ █▄▀
# ============================

# ============================
# █ █░█ █
# █ █▀█ █
# █▀ ▀█▀ ▄▀█ █▀█ ▀█▀
# ▄█ ░█░ █▀█ █▀▄ ░█░
# ============================
# AKA IHI table routes:

# Read Existing  (R)
@app.route("/ihi")
def read_ihi():
    pdList = IHI.query.all()
    return jsonify(
        {
            "data": [pd.to_dict()
                    for pd in pdList]
        }
    ), 200

# Read Existing by Person (R)
@app.route("/ihi/<id>")
def read_ihi_by_person(id):
    person = Personal_Details.query.get_or_404(id)
    ihis_of_person = person.ihis
    return jsonify(
        {
            "data": [pd.to_dict()
                    for pd in ihis_of_person]
        }
    ), 200



# ============================
# █▀▀ █▄░█ █▀▄
# ██▄ █░▀█ █▄▀
# ============================

# ============================
# █▀▄ █░█ ▀█▀ █▄█   █░█ █▀█ █░█ █▀█   █░░ █▀█ █▀▀
# █▄▀ █▄█ ░█░ ░█░   █▀█ █▄█ █▄█ █▀▄   █▄▄ █▄█ █▄█
# █▀ ▀█▀ ▄▀█ █▀█ ▀█▀
# ▄█ ░█░ █▀█ █▀▄ ░█░
# ============================
# AKA Duty_Hour_Log table routes:

# Read duty Hour field/column name (R)
@app.route('/duty_hour_log', methods=['GET'])
def get_duty_hour_log():
    dutyList = Duty_Hour_Log.query.all()
    return jsonify(
        {
            "data": [pd.to_dict()
                     for pd in dutyList]
        }
    ), 200

# Read Existing by Person (R)
@app.route("/dutyhour/<id>")
def read_dutyhourlogs_by_person(id):
    person = Personal_Details.query.get_or_404(id)
    dutyhourlogs_of_person = person.duty_hour_logs
    return jsonify(
        {
            "data": [pd.to_dict()
                    for pd in dutyhourlogs_of_person]
        }
    ), 200

# Add duty hour 
@app.route('/add_duty_hour', methods=['POST'])
def create_duty_hour():
    data = request.get_json()
    print('hello')
    print(data)
    if not all(key in data.keys() for key in ('MCR_No', 'Level' , 'Submitted' , 'Submitted_Proportion'  , 'MMYYYY' , 
    'Logged_for_month' 
                )):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    duty_hour_log = Duty_Hour_Log(**data)
    try:
        db.session.add(duty_hour_log)
        db.session.commit()
        return jsonify(duty_hour_log.to_dict()), 201
    except Exception as e:
        print("An error occurred:", e)
        print("Stack trace:")
        traceback.print_exc()

@app.route('/duty_hour_log/<int:id>', methods=['PUT'])
def update_duty_hour_log(id):
    user = Duty_Hour_Log.query.get(id)
    if not user:
        return 'Duty Hour Log not found', 404

    data = request.get_json()
    user.MCR_No = data['MCR_No']
    user.Level = data['Level']
    user.Submitted = data['Submitted']
    user.Submitted_Proportion = data['Submitted_Proportion']
    user.MMYYYY = data['MMYYYY']
    user.Logged_for_month = data['Logged_for_month']

    db.session.commit()
    return 'Duty Hour Log updated', 200
# from sqlalchemy import create_engine
# from sqlalchemy import inspect
# engine = create_engine('mysql+pymysql://root:root@localhost/SingHealth?charset=utf8')
# insp = inspect(engine)
# connection = engine.connect()
# print(insp.get_table_names())
# @app.route('/get_all_tables', methods=['GET'])
# def get_all_tables():
#     res = {}
#     for table_name in insp.get_table_names():
#         res[table_name]=[]
#         for column in insp.get_columns(table_name):
#             res[table_name].append(column['name'])
    
#     return jsonify(
#         {
#             "data":res
#         }
#     ), 200
#     print(insp.get_table_names(),'OSJVGNWOEVNWOECNVWEOICMWEOI')
# ============================
# █▀▀ █▄░█ █▀▄
# ██▄ █░▀█ █▄▀
# ============================

# ============================
# █▀█ █▀█ █▀█ █▀▀ █▀▀ █▀▄ █░█ █▀█ █▀▀
# █▀▀ █▀▄ █▄█ █▄▄ ██▄ █▄▀ █▄█ █▀▄ ██▄
# █▀ ▀█▀ ▄▀█ █▀█ ▀█▀
# ▄█ ░█░ █▀█ █▀▄ ░█░
# ============================
# AKA Procedure_Log table routes:
# Read Existing procedure log (R)
@app.route("/procedure_log")
def read_procedure_log():
    res = Procedure_Log.query.all()
    return jsonify(
        {
            "data": [r.to_dict()
                     for r in res]
        }
    ), 200

# Read Existing by Person (R)
@app.route("/procedurelog/<id>")
def read_procedurelog_by_person(id):
    person = Personal_Details.query.get_or_404(id)
    caselogs_of_person = person.procedure_logs
    return jsonify(
        {
            "data": [pd.to_dict()
                    for pd in caselogs_of_person]
        }
    ), 200


# ============================
# █▀▀ █▄░█ █▀▄
# ██▄ █░▀█ █▄▀
# ============================

# ============================
# █▀▀ ▄▀█ █▀ █▀▀   █░░ █▀█ █▀▀
# █▄▄ █▀█ ▄█ ██▄   █▄▄ █▄█ █▄█
# █▀ ▀█▀ ▄▀█ █▀█ ▀█▀
# ▄█ ░█░ █▀█ █▀▄ ░█░
# ============================
# AKA Case_log table routes:
# Read Existing caselog (R)
@app.route("/case_log")
def read_case_log():
    res = Case_Log.query.all()
    return jsonify(
        {
            "data": [r.to_dict()
                    for r in res]
        }
    ), 200

# Read Existing by Person (R)
@app.route("/caselogs/<id>")
def read_caselogs_by_person(id):
    person = Personal_Details.query.get_or_404(id)
    caselogs_of_person = person.case_logs
    return jsonify(
        {
            "data": [pd.to_dict()
                    for pd in caselogs_of_person]
        }
    ), 200

# ============================
# █▀▀ █▄░█ █▀▄
# ██▄ █░▀█ █▄▀
# ============================

# ============================
# █▀▀ █░█ ▄▀█ █░░ █░█ ▄▀█ ▀█▀ █ █▀█ █▄░█
# ██▄ ▀▄▀ █▀█ █▄▄ █▄█ █▀█ ░█░ █ █▄█ █░▀█
# █▀ ▀█▀ ▄▀█ █▀█ ▀█▀
# ▄█ ░█░ █▀█ █▀▄ ░█░
# ============================
# AKA Evaluation table routes:

# Read Existing by Person (R)
@app.route("/evaluations/<id>")
def read_evaluations_by_person(id):
    person = Personal_Details.query.get_or_404(id)
    evaluations_of_person = person.evaluations
    return jsonify(
        {
            "data": [pd.to_dict()
                    for pd in evaluations_of_person]
        }
    ), 200

# Read Existing evaluations (R)
@app.route("/evaluation")
def read_evaluation():
    res = Evaluations.query.all()
    return jsonify(
        {
            "data": [r.to_dict()
                     for r in res]
        }
    ), 200


# ============================
# █▀▀ █▄░█ █▀▄
# ██▄ █░▀█ █▄▀
# ============================

# AKA TrgExtRem_History table routes:

# Read Existing  (R)
@app.route("/trgextremhistory")
def read_trgextrem_history():
    pdList = TrgExtRem_History.query.all()
    return jsonify(
        {
            "data": [pd.to_dict()
                    for pd in pdList]
        }
    ), 200

# Read Existing by Person (R)
@app.route("/trgextremhistory/<id>")
def read_trgextrem_history_by_person(id):
    person = Personal_Details.query.get_or_404(id)
    trgextremhistory_of_person = person.trgExtRem_Histories
    return jsonify(
        {
            "data": [pd.to_dict()
                    for pd in trgextremhistory_of_person]
        }
    ), 200

# ============================
# █▀▀ █▄░█ █▀▄
# ██▄ █░▀█ █▄▀
# ============================

# AKA Presentations table routes:

# Read Existing  (R)
@app.route("/presentations")
def read_presentations():
    pdList = Presentations.query.all()
    return jsonify(
        {
            "data": [pd.to_dict()
                    for pd in pdList]
        }
    ), 200

# Read Existing by Person (R)
@app.route("/presentations/<id>")
def read_presentations_by_person(id):
    person = Personal_Details.query.get_or_404(id)
    presentation_of_person = person.presentations
    return jsonify(
        {
            "data": [pd.to_dict()
                    for pd in presentation_of_person]
        }
    ), 200

# Add duty hour 
@app.route('/add_presentation', methods=['POST'])
def create_presentation():
    data = request.get_json()
    # cannot add if person not present in database:
    if "MCR_No" in data.keys():
        person = Personal_Details.query.get_or_404(id)
    else:
        return jsonify(
        {
            "Error Msg": "Person not present in database"
        }
    ), 404
    print('hello')
    print(data)
    if not all(key in data.keys() for key in ('MCR_No', 'Level' , 'Submitted' , 'Submitted_Proportion'  , 'MMYYYY' , 
    'Logged_for_month' 
                )):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    presentation = Presentations(**data)
    try:
        db.session.add(presentation)
        db.session.commit()
        return jsonify(presentation.to_dict()), 201
    except Exception as e:
        print("An error occurred:", e)
        print("Stack trace:")
        traceback.print_exc()


from sqlalchemy import insert,text
# Read Awards field/column name (R)
@app.route('/create_resident', methods=['POST'])
def create_resident():
    data = request.get_json()
    personal_details_query=f'INSERT INTO Personal_Details VALUES ('
    for column in data['Personal_Details']:
        value_to_insert=data['Personal_Details'][column]
        personal_details_query+="'" + value_to_insert+"',"
    personal_details_query=personal_details_query[:-3]
    personal_details_query+="'0'"
    personal_details_query+=')'
    connection.execute(personal_details_query)

    #remove personal details from data
    del data['Personal_Details']
    print(data,'data now is what')


    for table in data:
        query = f'INSERT INTO {table} VALUES ('
        query_string_values=''
        for col in data[table]:
            value_to_insert=data[table][col]
            query_string_values+="'" + value_to_insert+"',"
        query_string_values=query_string_values[:-3]
        query_string_values+="'0'"
        query_string_values+=')'
        query+= query_string_values
        connection.execute(query)

        
db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011, debug=True)

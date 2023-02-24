from sqlalchemy import insert, text, create_engine,inspect, select
from flask import abort
from flask import Flask, request, jsonify, render_template, send_file, redirect, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json
import pandas as pd
import traceback
import werkzeug.exceptions as ex
from sqlalchemy.sql import exists
# from flask_login import login_required, current_user

app = Flask(__name__)

# db = SQLAlchemy(app)

# CORS(app)
app = Flask(__name__)
app.app_context().push()

if __name__ == '__main__':
#     # Mac user -------------------------------------------------------------------
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root' + \
                                        '@localhost:3306/SingHealth'
    engine = create_engine('mysql+pymysql://root:root@localhost/SingHealth?charset=utf8')

    # --------------------------------------------------------------------------------

    # # Windows user -------------------------------------------------------------------
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:' + \
    #                                         '@localhost:3306/SingHealth'
    # engine = create_engine('mysql+pymysql://root:@localhost/SingHealth?charset=utf8')

    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
    #                                         'pool_recycle': 280}
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)

# Read PersonalDetails field/column name (R)


@app.route('/', methods=['GET'])
def display():
    return render_template('personal_details2.html')

@app.route('/personal_details', methods=['GET'])
def displaypersonal():
    return render_template('personal_details2.html')

@app.route('/involvement', methods=['GET'])
def displayinvolvement():
    return render_template('involvement.html')

@app.route('/presentations', methods=['GET'])
def displaypresentations():
    return render_template('presentations.html')

@app.route('/profiles', methods=['GET'])
def displayprofile():
    return render_template('resident_profile.html')

# @app.route('/<path:filename>', methods=['GET'])
@app.route('/v', methods=['GET'])
def displayv():
    return render_template('vuepage.html')
    # return app.send_static_file(filename)

# @app.route('/tab/', methods=['GET'])
# def displayprojects():
#     return render_template('personal_details2.html')


class Personal_Details(db.Model):
    __tablename__ = 'Personal_Details'
    Employee_ID = db.Column(db.String(50))
    MCR_No = db.Column(db.String(50), primary_key=True)
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

    presentations = db.relationship(
        'Presentations', backref='Personal_Details')
    posting_histories = db.relationship(
        'Posting_History', backref='Personal_Details')
    duty_hour_logs = db.relationship(
        'Duty_Hour_Log', backref='Personal_Details')
    case_logs = db.relationship('Case_Log', backref='Personal_Details')
    procedure_logs = db.relationship(
        'Procedure_Log', backref='Personal_Details')
    exam_histories = db.relationship(
        'Exam_History', backref='Personal_Details')
    publications = db.relationship('Publications', backref='Personal_Details')
    evaluations = db.relationship('Evaluations', backref='Personal_Details')
    trgExtRem_Histories = db.relationship(
        'TrgExtRem_History', backref='Personal_Details')
    projects = db.relationship('Projects', backref='Personal_Details')
    awards = db.relationship('Awards', backref='Personal_Details')
    
    grants = db.relationship('Grants', backref='Personal_Details')
    ihis = db.relationship('IHI', backref='Personal_Details')
    involvements = db.relationship('Involvement', backref='Personal_Details')
    didactic_attendance = db.relationship('Didactic_Attendance', backref='Personal_Details')
    education_history = db.relationship('Education_History', backref='Personal_Details')

    __mapper_args__ = {
        'polymorphic_identity': 'Personal_Details'
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


class Presentations(db.Model):
    __tablename__ = 'Presentations'
    # 'MCR_No', 'Title', 'Conference_Name', 'Type', 'Project_ID', 'Country', 'Presentation_Date'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    MCR_No = db.Column(db.String(100),  db.ForeignKey(
        'Personal_Details.MCR_No'))
    Title = db.Column(db.String(300))
    Conference_Name = db.Column(db.String(100))
    Type = db.Column(db.String(200))
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
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result


class Posting_History(db.Model):
    __tablename__ = 'Posting_History'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    MCR_No = db.Column(db.String(100),  db.ForeignKey(
        'Personal_Details.MCR_No'))
    # 'Posting_Institution', 'Posting_Department', 'Posting_StartDate', 'Posting_EndDate'
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
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result


class Duty_Hour_Log(db.Model):
    __tablename__ = 'Duty_Hour_Log'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    MCR_No = db.Column(db.String(100),  db.ForeignKey(
        'Personal_Details.MCR_No'))
    
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
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result


class Case_Log(db.Model):
    __tablename__ = 'Case_Log'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    MCR_No = db.Column(db.String(100),  db.ForeignKey(
        'Personal_Details.MCR_No'))
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
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result


class Procedure_Log(db.Model):
    __tablename__ = 'Procedure_Log'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    MCR_No = db.Column(db.String(100),  db.ForeignKey(
        'Personal_Details.MCR_No'))
    Procedure_Name = db.Column(db.String(100))
    Date_of_Completion = db.Column(db.String(100))
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
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result


class Exam_History(db.Model):
    __tablename__ = 'Exam_History'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    MCR_No = db.Column(db.String(100),  db.ForeignKey(
        'Personal_Details.MCR_No'))
    
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
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result


class Publications(db.Model):
    __tablename__ = 'Publications'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    MCR_No = db.Column(db.String(100),  db.ForeignKey(
        'Personal_Details.MCR_No'))
    
    Publication_Title = db.Column(db.String(200))
    Journal_Title = db.Column(db.String(200))

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
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result


class Evaluations(db.Model):
    __tablename__ = 'Evaluations'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    MCR_No = db.Column(db.String(100),  db.ForeignKey(
        'Personal_Details.MCR_No'))
    
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
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result


class TrgExtRem_History(db.Model):
    __tablename__ = 'TrgExtRem_History'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    MCR_No = db.Column(db.String(100),  db.ForeignKey(
        'Personal_Details.MCR_No'))
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
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class Education_History(db.Model):
    __tablename__= "Education_History"
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    MCR_No = db.Column(db.String(100),  db.ForeignKey(
        'Personal_Details.MCR_No'))

    Year_of_Graduation = db.Column(db.String(50))
    Date_of_Graduation = db.Column(db.String(50))
    Basic_Qualification =  db.Column(db.String(50))
    Medical_School = db.Column(db.String(50))
    Country_of_Graduation = db.Column(db.String(50))
    IM_Residency_Start_Date= db.Column(db.String(50))
    IM_Residency_End_Date= db.Column(db.String(50))
    SR_Residency_Programme= db.Column(db.String(50))
    SR_Residency_Start_Date= db.Column(db.String(50))
    SR_Residency_End_Date= db.Column(db.String(50))
    PG_Year =db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'Education_History'
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

class Projects(db.Model):
    __tablename__ = 'Projects'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    MCR_No = db.Column(db.String(100),  db.ForeignKey(
        'Personal_Details.MCR_No'))
    'Project_Type', 'Project_Title', 'Project_ID', 'Start_Date', 
    'End_Date', 'Date_of_QI_Certification', 'PMID'
    Project_Type = db.Column(db.String(100))
    Project_Title = db.Column(db.String(300))
    Project_ID = db.Column(db.String(100))
    Start_Date = db.Column(db.String(100))
    End_Date = db.Column(db.String(100))
    Date_of_QI_Certification = db.Column(db.String(100))
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
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result


class Awards(db.Model):
    __tablename__ = 'Awards'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    MCR_No = db.Column(db.String(100),  db.ForeignKey(
        'Personal_Details.MCR_No'))
    Award_Category = db.Column(db.String(150))
    Name_of_Award = db.Column(db.String(100))

    FY_of_Award_Received = db.Column(db.String(100))
    Date_of_Award_Received = db.Column(db.String(100))
    Project_ID = db.Column(db.String(150))

    __mapper_args__ = {
        'polymorphic_identity': 'Awards'
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


class Grants(db.Model):
    __tablename__ = 'Grants'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    MCR_No = db.Column(db.String(100),  db.ForeignKey(
        'Personal_Details.MCR_No'))
        
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
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result


class IHI(db.Model):
    __tablename__ = 'IHI'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    MCR_No = db.Column(db.String(100),  db.ForeignKey(
        'Personal_Details.MCR_No'))
    
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
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result


class Involvement(db.Model):
    __tablename__ = 'Involvement'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    
    Involvement_Type = db.Column(db.String(100))
    MCR_No = db.Column(db.String(100),  db.ForeignKey(
        'Personal_Details.MCR_No'))
    Event = db.Column(db.String(400))
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


class Didactic_Attendance(db.Model):
    __tablename__ = 'Didactic_Attendance'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    MCR_No = db.Column(db.String(100),  db.ForeignKey('Personal_Details.MCR_No'))
    
    Month = db.Column(db.String(100))
    Total_tracked_sessions = db.Column(db.String(100))
    Number_of_sessions_attended = db.Column(db.String(100))
    MmYyyy = db.Column(db.String(100))
    Percentage_of_sessions_attended= db.Column(db.String(100))
    Compliance_or_Not = db.Column(db.String(100))

    __mapper_args__ = {
        'polymorphic_identity': 'Didactic_Attendance'
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
    if not all(key in data.keys() for key in ('Employee_ID', 'MCR_No', "Staff_Name", "Designation", "Programme",
                                              "Year_of_Training", "Academic_Year", "Department", "Institution",
                                              "Academic_Clinical_Programme", "Employment_Status", "Nationality", "Date_of_Birth", "Gender",
                                              "Registration_Type", "House_Blk_No", "Street", "Building_Name", "Unit_No", "Postal_Code", "Contact_No_Work",
                                              "Contact_No_Personal", "Email_Official", "Email_Personal", "BCLS_Expiry_Date", "ACLS_Expiry_Date",
                                              "Covid_19_Vaccination_Status", "Date_of_First_Dose", "Date_of_Second_Dose", "Vaccination_Remarks"
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


@app.route('/import', methods=['POST'])
def view():
    file = request.files['file']
    file.save(file.filename)
    # personal details
    personalDetails = pd.read_excel(
        file, sheet_name="Personal Details", dtype=str)
    personalDetails.columns = ['Employee_ID', 'MCR_No', 'Staff_Name', 'Designation',
                            'Programme', 'Year_of_Training', 'Academic_Year', 'Department',
                            'Institution', 'Academic_Clinical_Programme', 'Employment_Status',
                            'Nationality', 'Date_of_Birth', 'Gender', 'Registration_Type',
                            'House_Blk_No', 'Street', 'Building_Name', 'Unit_No', 'Postal_Code',
                            'Contact_No_Work', 'Contact_No_Personal', 'Email_Official',
                            'Email_Personal', 'BCLS_Expiry_Date', 'ACLS_Expiry_Date',
                            'Covid_19_Vaccination_Status', 'Date_of_First_Dose',
                            'Date_of_Second_Dose', 'Vaccination_Remarks']
    # Involvement
    involvement = pd.read_excel(
        file, sheet_name="Involvement", dtype=str)
    involvement.columns = ['Involvement_Type', 'MCR_No',
                        'Event', 'Role', 'Start_Date', 'End_Date']
    
    #history-education
    history_education = pd.read_excel(
        file, sheet_name="History - Education", dtype=str)
    history_education.columns = ['MCR_No' , 'Year_of_Graduation' , 'Date_of_Graduation' , 'Basic_Qualification' , 'Medical_School' , 'Country_of_Graduation' , 'IM_Residency_Start_Date' , 
    'IM_Residency_End_Date', 'SR_Residency_Programme', 'SR_Residency_Start_Date', 'SR_Residency_End_Date','PG_Year']

    #history-posting
    history_posting = pd.read_excel(
        file, sheet_name="History - Posting", dtype=str)
    history_posting.columns = [ 'MCR_No', 'Posting_Institution' , 'Posting_Department' , 'Posting_StartDate' , 'Posting_EndDate']

    #history-exam
    history_exam = pd.read_excel(
        file, sheet_name="History - Exam", dtype=str)
    history_exam.columns = [ 'MCR_No', 'Name_of_Exam' , 'Date_of_Attempt' , 'Exam_Status']

    #histroy-trg
    history_trg = pd.read_excel(
        file, sheet_name="History - Trg Ext.&Remediation", dtype=str)
    history_trg.columns = [ 'MCR_No', 'LOAPIP' , 'StartDate' , 'EndDate']

    #grants
    grants = pd.read_excel(
        file, sheet_name="Grants", dtype=str)
    grants.columns = [ 'MCR_No', 'Name_of_Grant' , 'Project_Title' , 'Project_ID' , 'Grant_End_Date' , 'Grant_Start_Date']

    #awards
    awards = pd.read_excel(
        file, sheet_name="Awards", dtype=str)
    awards.columns = [ 'MCR_No', 'Award_Category' , 'Name_of_Award' , 'FY_of_Award_Received' , 'Date_of_Award_Received' , 'Project_ID']

    #publications
    publlications = pd.read_excel(
        file, sheet_name="Publications", dtype=str)
    publlications.columns = [ 'MCR_No', 'Publication_Title' , 'Journal_Title' , 'PMID' , 'Publication_Date' ]

    #presentations
    presentations = pd.read_excel(
        file, sheet_name="Presentations", dtype=str)
    presentations.columns = [ 'MCR_No', 'Title' , 'Type' , 'Project_ID' , 'Conference_Name' , 'Country' , 'Presentation_Date' ]

    #project
    project = pd.read_excel(
        file, sheet_name="Projects", dtype=str)
    project.columns = [ 'MCR_No', 'Project_Type' ,'Project_Title' ,'Project_ID' ,'Start_Date' , 'End_Date' , 'Date_of_QI_Certification' , 'PMID' ]

    #IHI
    ihi = pd.read_excel(
        file, sheet_name="IHI", dtype=str)
    ihi.columns = [ 'MCR_No', 'Completion_of_Emodules' , 'Date' ]

    #didatic attendance
    didatic_attendance = pd.read_excel(
        file, sheet_name="Didactic Attendance", dtype=str)
    didatic_attendance.columns = [ 'MCR_No', 'Month' , 'Total_tracked_sessions' , 'Number_of_sessions_attended'  , 'MmYyyy' , 'Posting_Institution' , 'Posting_Department' , 'Scheduled_Teachings' 'Compliance_or_Not' , "Percentage_of_sessions_attended"]

    if didatic_attendance.duplicated().any() or didatic_attendance['MCR_No'].isnull().sum() > 0 or ihi['MCR_No'].isnull().sum() > 0 or ihi.duplicated().any() or project['MCR_No'].isnull().sum() > 0 or project.duplicated().any() or presentations['MCR_No'].isnull().sum() > 0 or presentations.duplicated().any() or publlications['MCR_No'].isnull().sum() > 0 or publlications.duplicated().any() or awards['MCR_No'].isnull().sum() > 0 or awards.duplicated().any() or grants['MCR_No'].isnull().sum() > 0 or grants.duplicated().any() or personalDetails['MCR_No'].isnull().sum() > 0 or personalDetails['Employee_ID'].isnull().sum() > 0 or personalDetails.duplicated().any() or involvement['MCR_No'].isnull().sum() > 0 or (involvement.duplicated().any()) or history_education['MCR_No'].isnull().sum() > 0 or (history_education.duplicated().any()) or history_posting['MCR_No'].isnull().sum() > 0 or history_posting.duplicated().any() or history_exam['MCR_No'].isnull().sum() > 0 or history_exam.duplicated().any() or history_trg['MCR_No'].isnull().sum() > 0 or history_trg.duplicated().any():
        writer = pd.ExcelWriter("error.xlsx", engine='xlsxwriter')
        workbook = writer.book
        format1 = workbook.add_format({'bg_color': '#FF8080'})

        ## personal_DETAILS
        if personalDetails['MCR_No'].isnull().sum() > 0 or personalDetails['Employee_ID'].isnull().sum() > 0 or personalDetails.duplicated().any():
            personalDetails.to_excel(writer, sheet_name='Personal_Details_error')
            worksheet = writer.sheets['Personal_Details_error']
            nullrows_mcr_no = personalDetails[personalDetails[[
                "MCR_No"]].isnull().any(axis=1)]
            nullrows_ID = personalDetails[personalDetails[[
                "Employee_ID"]].isnull().any(axis=1)]
            duplicate_row_bool = personalDetails.duplicated()
            for i in range(len(duplicate_row_bool)):
                if (duplicate_row_bool[i] == True):
                    ran = "A" + str(i+2) + ":BA" + str(i+2)
                    worksheet.conditional_format(ran,
                                            {'type':     'cell',
                                            'criteria': 'not equal to',
                                            'value': '"o1"',
                                            'format':   format1})
            
            for row in nullrows_mcr_no.index:
                ran = "A" + str(row+2) + ":BA" + str(row+2)
                worksheet.conditional_format(ran,
                                            {'type':     'cell',
                                            'criteria': 'not equal to',
                                            'value': '"o1"',
                                            'format':   format1})
            for row in nullrows_ID.index:
                ran = "A" + str(row+2) + ":BA" + str(row+2)
                worksheet.conditional_format(ran,
                                            {'type':     'cell',
                                            'criteria': 'not equal to',
                                            'value': '"o1"',
                                            'format':   format1})
        ## involvement
        if involvement['MCR_No'].isnull().sum() > 0 or involvement.duplicated().any():
            involvement.to_excel(writer, sheet_name='involvement_error')
            workbook = writer.book
            worksheet = writer.sheets['involvement_error']
            format1 = workbook.add_format({'bg_color': '#FF8080'})
            nullrows = involvement[involvement[[
            "MCR_No"]].isnull().any(axis=1)]
            duplicate_row_bool = involvement.duplicated()
            for i in range(len(duplicate_row_bool)):
                if (duplicate_row_bool[i] == True):
                    ran = "A" + str(i+2) + ":BA" + str(i+2)
                    worksheet.conditional_format(ran,
                                            {'type':     'cell',
                                            'criteria': 'not equal to',
                                            'value': '"o1"',
                                            'format':   format1})

            for row in nullrows.index:
                ran = "A" + str(row+2) + ":BA" + str(row+2)
                worksheet.conditional_format(ran,
                                                {'type':     'cell',
                                                'criteria': 'not equal to',
                                                'value': '"o1"',
                                                'format':   format1})
        ## history_education
        if history_education['MCR_No'].isnull().sum() > 0 or history_education.duplicated().any():
            history_education.to_excel(
                writer, sheet_name='history_education_error')
            workbook = writer.book
            worksheet = writer.sheets['history_education_error']
            format1 = workbook.add_format({'bg_color': '#FF8080'})
            nullrows = history_education[history_education[[
            "MCR_No"]].isnull().any(axis=1)]
            duplicate_row_bool = history_education.duplicated()
            for i in range(len(duplicate_row_bool)):
                if (duplicate_row_bool[i] == True):
                    ran = "A" + str(i+2) + ":BA" + str(i+2)
                    worksheet.conditional_format(ran,
                                            {'type':     'cell',
                                            'criteria': 'not equal to',
                                            'value': '"o1"',
                                            'format':   format1})

            for row in nullrows.index:
                ran = "A" + str(row+2) + ":BA" + str(row+2)
                worksheet.conditional_format(ran,
                                                {'type':     'cell',
                                                'criteria': 'not equal to',
                                                'value': '"o1"',
                                                'format':   format1})
            
        ## history_posting 
        if history_posting['MCR_No'].isnull().sum() > 0 or history_posting.duplicated().any():
            history_posting.to_excel(
                writer, sheet_name='history_posting_error')
            workbook = writer.book
            worksheet = writer.sheets['history_posting_error']
            format1 = workbook.add_format({'bg_color': '#FF8080'})
            nullrows = history_posting[history_posting[[
            "MCR_No"]].isnull().any(axis=1)]
            duplicate_row_bool = history_posting.duplicated()
            for i in range(len(duplicate_row_bool)):
                if (duplicate_row_bool[i] == True):
                    ran = "A" + str(i+2) + ":BA" + str(i+2)
                    worksheet.conditional_format(ran,
                                            {'type':     'cell',
                                            'criteria': 'not equal to',
                                            'value': '"o1"',
                                            'format':   format1})
            for row in nullrows.index:
                ran = "A" + str(row+2) + ":BA" + str(row+2)
                worksheet.conditional_format(ran,
                                                {'type':     'cell',
                                                'criteria': 'not equal to',
                                                'value': '"o1"',
                                                'format':   format1})
            
        ## history exam
        if history_exam['MCR_No'].isnull().sum() > 0 or history_exam.duplicated().any():
            history_exam.to_excel(
                writer, sheet_name='history_exam_error')
            workbook = writer.book
            worksheet = writer.sheets['history_exam_error']
            format1 = workbook.add_format({'bg_color': '#FF8080'})
            nullrows = history_exam[history_exam[[
            "MCR_No"]].isnull().any(axis=1)]
            duplicate_row_bool = history_exam.duplicated()
            for i in range(len(duplicate_row_bool)):
                if (duplicate_row_bool[i] == True):
                    ran = "A" + str(i+2) + ":BA" + str(i+2)
                    worksheet.conditional_format(ran,
                                            {'type':     'cell',
                                            'criteria': 'not equal to',
                                            'value': '"o1"',
                                            'format':   format1})
            for row in nullrows.index:
                ran = "A" + str(row+2) + ":BA" + str(row+2)
                worksheet.conditional_format(ran,
                                                {'type':     'cell',
                                                'criteria': 'not equal to',
                                                'value': '"o1"',
                                                'format':   format1})
        
        ## history trg
        if history_trg['MCR_No'].isnull().sum() > 0 or history_trg.duplicated().any():
            history_trg.to_excel(
                writer, sheet_name='history_trg_error')
            workbook = writer.book
            worksheet = writer.sheets['history_trg_error']
            format1 = workbook.add_format({'bg_color': '#FF8080'})
            nullrows = history_trg[history_trg[[
            "MCR_No"]].isnull().any(axis=1)]
            duplicate_row_bool = history_trg.duplicated()
            for i in range(len(duplicate_row_bool)):
                if (duplicate_row_bool[i] == True):
                    ran = "A" + str(i+2) + ":BA" + str(i+2)
                    worksheet.conditional_format(ran,
                                            {'type':     'cell',
                                            'criteria': 'not equal to',
                                            'value': '"o1"',
                                            'format':   format1})
            for row in nullrows.index:
                ran = "A" + str(row+2) + ":BA" + str(row+2)
                worksheet.conditional_format(ran,
                                                {'type':     'cell',
                                                'criteria': 'not equal to',
                                                'value': '"o1"',
                                                'format':   format1})
        
        ## grants
        if grants['MCR_No'].isnull().sum() > 0 or grants.duplicated().any():
            grants.to_excel(
                writer, sheet_name='grants_error')
            workbook = writer.book
            worksheet = writer.sheets['grants_error']
            format1 = workbook.add_format({'bg_color': '#FF8080'})
            nullrows = grants[grants[[
            "MCR_No"]].isnull().any(axis=1)]
            duplicate_row_bool = grants.duplicated()
            for i in range(len(duplicate_row_bool)):
                if (duplicate_row_bool[i] == True):
                    ran = "A" + str(i+2) + ":BA" + str(i+2)
                    worksheet.conditional_format(ran,
                                            {'type':     'cell',
                                            'criteria': 'not equal to',
                                            'value': '"o1"',
                                            'format':   format1})
            for row in nullrows.index:
                ran = "A" + str(row+2) + ":BA" + str(row+2)
                worksheet.conditional_format(ran,
                                                {'type':     'cell',
                                                'criteria': 'not equal to',
                                                'value': '"o1"',
                                                'format':   format1})
            
        ## awards
        if awards['MCR_No'].isnull().sum() > 0 or awards.duplicated().any():
            awards.to_excel(
                writer, sheet_name='awards_error')
            workbook = writer.book
            worksheet = writer.sheets['awards_error']
            format1 = workbook.add_format({'bg_color': '#FF8080'})
            nullrows = awards[awards[[
            "MCR_No"]].isnull().any(axis=1)]
            duplicate_row_bool = awards.duplicated()
            for i in range(len(duplicate_row_bool)):
                if (duplicate_row_bool[i] == True):
                    ran = "A" + str(i+2) + ":BA" + str(i+2)
                    worksheet.conditional_format(ran,
                                            {'type':     'cell',
                                            'criteria': 'not equal to',
                                            'value': '"o1"',
                                            'format':   format1})
            for row in nullrows.index:
                ran = "A" + str(row+2) + ":BA" + str(row+2)
                worksheet.conditional_format(ran,
                                                {'type':     'cell',
                                                'criteria': 'not equal to',
                                                'value': '"o1"',
                                                'format':   format1})
        
        ## publications
        if publlications['MCR_No'].isnull().sum() > 0 or publlications.duplicated().any():
            publlications.to_excel(
                writer, sheet_name='publlications_error')
            workbook = writer.book
            worksheet = writer.sheets['publlications_error']
            format1 = workbook.add_format({'bg_color': '#FF8080'})
            nullrows = publlications[publlications[[
            "MCR_No"]].isnull().any(axis=1)]
            duplicate_row_bool = publlications.duplicated()
            for i in range(len(duplicate_row_bool)):
                if (duplicate_row_bool[i] == True):
                    ran = "A" + str(i+2) + ":BA" + str(i+2)
                    worksheet.conditional_format(ran,
                                            {'type':     'cell',
                                            'criteria': 'not equal to',
                                            'value': '"o1"',
                                            'format':   format1})
            for row in nullrows.index:
                ran = "A" + str(row+2) + ":BA" + str(row+2)
                worksheet.conditional_format(ran,
                                                {'type':     'cell',
                                                'criteria': 'not equal to',
                                                'value': '"o1"',
                                                'format':   format1})
        
        ## presentations
        if presentations['MCR_No'].isnull().sum() > 0 or presentations.duplicated().any():
            presentations.to_excel(
                writer, sheet_name='presentations_error')
            workbook = writer.book
            worksheet = writer.sheets['presentations_error']
            format1 = workbook.add_format({'bg_color': '#FF8080'})
            nullrows = presentations[presentations[[
            "MCR_No"]].isnull().any(axis=1)]
            duplicate_row_bool = presentations.duplicated()
            for i in range(len(duplicate_row_bool)):
                if (duplicate_row_bool[i] == True):
                    ran = "A" + str(i+2) + ":BA" + str(i+2)
                    worksheet.conditional_format(ran,
                                            {'type':     'cell',
                                            'criteria': 'not equal to',
                                            'value': '"o1"',
                                            'format':   format1})
            for row in nullrows.index:
                ran = "A" + str(row+2) + ":BA" + str(row+2)
                worksheet.conditional_format(ran,
                                                {'type':     'cell',
                                                'criteria': 'not equal to',
                                                'value': '"o1"',
                                                'format':   format1})
            
        ## project
        if project['MCR_No'].isnull().sum() > 0 or project.duplicated().any():
            project.to_excel(
                writer, sheet_name='project_error')
            workbook = writer.book
            worksheet = writer.sheets['project_error']
            format1 = workbook.add_format({'bg_color': '#FF8080'})
            nullrows = project[project[[
            "MCR_No"]].isnull().any(axis=1)]
            duplicate_row_bool = project.duplicated()
            for i in range(len(duplicate_row_bool)):
                if (duplicate_row_bool[i] == True):
                    ran = "A" + str(i+2) + ":BA" + str(i+2)
                    worksheet.conditional_format(ran,
                                            {'type':     'cell',
                                            'criteria': 'not equal to',
                                            'value': '"o1"',
                                            'format':   format1})
            for row in nullrows.index:
                ran = "A" + str(row+2) + ":BA" + str(row+2)
                worksheet.conditional_format(ran,
                                                {'type':     'cell',
                                                'criteria': 'not equal to',
                                                'value': '"o1"',
                                                'format':   format1})
        
        ## ihi
        if ihi.duplicated().any() or ihi['MCR_No'].isnull().sum() > 0:
            ihi.to_excel(
                writer, sheet_name='ihi_error')
            workbook = writer.book
            worksheet = writer.sheets['ihi_error']
            format1 = workbook.add_format({'bg_color': '#FF8080'})
            nullrows = ihi[ihi[[
            "MCR_No"]].isnull().any(axis=1)]
            duplicate_row_bool = ihi.duplicated()
            for i in range(len(duplicate_row_bool)):
                if (duplicate_row_bool[i] == True):
                    ran = "A" + str(i+2) + ":BA" + str(i+2)
                    worksheet.conditional_format(ran,
                                            {'type':     'cell',
                                            'criteria': 'not equal to',
                                            'value': '"o1"',
                                            'format':   format1})
            for row in nullrows.index:
                ran = "A" + str(row+2) + ":BA" + str(row+2)
                worksheet.conditional_format(ran,
                                                {'type':     'cell',
                                                'criteria': 'not equal to',
                                                'value': '"o1"',
                                                'format':   format1})
            
        ## didactic attendance 
        if didatic_attendance.duplicated().any() or didatic_attendance['MCR_No'].isnull().sum() > 0:
            didatic_attendance.to_excel(
                writer, sheet_name='didatic_attendance_error')
            workbook = writer.book
            worksheet = writer.sheets['didatic_attendance_error']
            format1 = workbook.add_format({'bg_color': '#FF8080'})
            nullrows = awards[awards[[
            "MCR_No"]].isnull().any(axis=1)]
            duplicate_row_bool = didatic_attendance.duplicated()
            for i in range(len(duplicate_row_bool)):
                if (duplicate_row_bool[i] == True):
                    ran = "A" + str(i+2) + ":BA" + str(i+2)
                    worksheet.conditional_format(ran,
                                            {'type':     'cell',
                                            'criteria': 'not equal to',
                                            'value': '"o1"',
                                            'format':   format1})
            for row in nullrows.index:
                ran = "A" + str(row+2) + ":BA" + str(row+2)
                worksheet.conditional_format(ran,
                                                {'type':     'cell',
                                                'criteria': 'not equal to',
                                                'value': '"o1"',
                                                'format':   format1})
                
        writer.save()

        # with open('/backend/error.xlsx' , 'rb') as f: 
        #     data
        # myio.write(data)
        # myio.seek(0)
        # send_file(, download_name="error.xlsx" , as_attachment=True)
        abort(404, description='Invalid Excel submitted')


    ### personal details
    personalDetails = personalDetails.fillna('')
    for i in range(len(personalDetails)):
        data = dict(personalDetails.iloc[i])
        presentation = Personal_Details(**data)
        try:
            if Personal_Details.query.filter_by(MCR_No=data["MCR_No"]).first() != None:
                Personal_Details.query.filter_by(
                    MCR_No=data["MCR_No"]).update(data)
            else:
                db.session.add(presentation)
                db.session.commit()

        except Exception as e:
            print("An error occurred:", e)
            print("Stack trace:")
            traceback.print_exc()

    ### involvement
    involvement = involvement.fillna('')
    for i in range(len(involvement)):
        data = dict(involvement.iloc[i])
        presentation2 = Involvement(**data)
        try:
            exist = db.session.query(exists().where(Involvement.MCR_No == data['MCR_No'] , Involvement.Event == data['Event'],Involvement.Start_Date == data['Start_Date'])).scalar()
            if exist == False:
                db.session.add(presentation2)
                db.session.commit()

        except Exception as e:
            print("An error occurred:", e)
            print("Stack trace:")
            traceback.print_exc()

    ### history_education
    history_education = history_education.fillna('')
    for i in range(len(history_education)):
        data = dict(history_education.iloc[i])
        presentation3 = Education_History(**data)
        try:
            exist = db.session.query(exists().where(Education_History.MCR_No == data['MCR_No'] , Education_History.Medical_School == data['Medical_School'],Education_History.Year_of_Graduation == data['Year_of_Graduation'])).scalar()
            if exist == False:
                db.session.add(presentation3)
                db.session.commit()

        except Exception as e:
            print("An error occurred:", e)
            print("Stack trace:")
            traceback.print_exc()

    ### history_posting
    history_posting= history_posting.fillna('')
    for i in range(len(history_posting)):
        data = dict(history_posting.iloc[i])
        presentation4 = Posting_History(**data)
        try:
            exist = db.session.query(exists().where(Posting_History.MCR_No == data['MCR_No'] , Posting_History.Posting_Department == data['Posting_Department'],Posting_History.Posting_StartDate == data['Posting_StartDate'])).scalar()
            if exist == False:
                db.session.add(presentation4)
                db.session.commit()

        except Exception as e:
            print("An error occurred:", e)
            print("Stack trace:")
            traceback.print_exc()

    ### history-exam
    history_exam= history_exam.fillna('')
    for i in range(len(history_exam)):
        data = dict(history_exam.iloc[i])
        presentation5 = Exam_History(**data)
        try:
            exist = db.session.query(exists().where(Exam_History.MCR_No == data['MCR_No'] , Exam_History.Name_of_Exam == data['Name_of_Exam'],Exam_History.Date_of_Attempt == data['Date_of_Attempt'])).scalar()
            if exist == False:
                db.session.add(presentation5)
                db.session.commit()

        except Exception as e:
            print("An error occurred:", e)
            print("Stack trace:")
            traceback.print_exc()

    ### history trg
    history_trg= history_trg.fillna('')
    for i in range(len(history_trg)):
        data = dict(history_trg.iloc[i])
        presentation6 = TrgExtRem_History(**data)
        try:
            exist = db.session.query(exists().where(TrgExtRem_History.MCR_No == data['MCR_No'] , TrgExtRem_History.StartDate == data['StartDate'],TrgExtRem_History.EndDate == data['EndDate'] ,TrgExtRem_History.LOAPIP == data['LOAPIP'] )).scalar()
            if exist == False:
                db.session.add(presentation6)
                db.session.commit()

        except Exception as e:
            print("An error occurred:", e)
            print("Stack trace:")
            traceback.print_exc()

    ### grants
    grants= grants.fillna('')
    for i in range(len(grants)):
        data = dict(grants.iloc[i])
        presentation7 = Grants(**data)
        try:
            exist = db.session.query(exists().where(Grants.MCR_No == data['MCR_No'] , Grants.Name_of_Grant == data['Name_of_Grant'],Grants.Grant_Start_Date == data['Grant_Start_Date'] ,Grants.Project_Title == data['Project_Title'] )).scalar()
            if exist == False:
                db.session.add(presentation7)
                db.session.commit()

        except Exception as e:
            print("An error occurred:", e)
            print("Stack trace:")
            traceback.print_exc()

    ### Awards
    awards= awards.fillna('')
    for i in range(len(awards)):
        data = dict(awards.iloc[i])
        presentation8 = Awards(**data)
        try:
            exist = db.session.query(exists().where(Awards.MCR_No == data['MCR_No'] , Awards.Date_of_Award_Received == data['Date_of_Award_Received'])).scalar()
            if exist == False:
                db.session.add(presentation8)
                db.session.commit()

        except Exception as e:
            print("An error occurred:", e)
            print("Stack trace:")
            traceback.print_exc()     

    ### publications
    publlications= publlications.fillna('')
    for i in range(len(publlications)):
        data = dict(publlications.iloc[i])
        presentation10 = Publications(**data)
        try:
            exist = db.session.query(exists().where(Publications.MCR_No == data['MCR_No'] , Publications.Publication_Title == data['Publication_Title'])).scalar()
            if exist == False:
                db.session.add(presentation10)
                db.session.commit()

        except Exception as e:
            print("An error occurred:", e)
            print("Stack trace:")
            traceback.print_exc()  

    ### presentations
    presentations= presentations.fillna('')
    for i in range(len(presentations)):
        data = dict(presentations.iloc[i])
        presentation11 = Presentations(**data)
        try:
            exist = db.session.query(exists().where(Presentations.MCR_No == data['MCR_No'] , Presentations.Title == data['Title'], Presentations.Conference_Name == data['Conference_Name'] ,Presentations.Presentation_Date == data['Presentation_Date'])).scalar()
            if exist == False:
                db.session.add(presentation11)
                db.session.commit()

        except Exception as e:
            print("An error occurred:", e)
            print("Stack trace:")
            traceback.print_exc()     

    ###project
    project= project.fillna('')
    for i in range(len(project)):
        data = dict(project.iloc[i])
        presentation12 = Projects(**data)
        try:
            exist = db.session.query(exists().where(Projects.MCR_No == data['MCR_No'] , Projects.Project_Title == data['Project_Title'], Projects.Start_Date == data['Start_Date'] ,Projects.End_Date == data['End_Date'])).scalar()
            if exist == False:
                db.session.add(presentation12)
                db.session.commit()

        except Exception as e:
            print("An error occurred:", e)
            print("Stack trace:")
            traceback.print_exc()    
    
    ### ihi
    ihi= ihi.fillna('')
    for i in range(len(ihi)):
        data = dict(ihi.iloc[i])
        presentation13 = IHI(**data)
        try:
            exist = db.session.query(exists().where(IHI.MCR_No == data['MCR_No'] ,IHI.Completion_of_Emodules== data['Completion_of_Emodules'], IHI.Date == data['Date'])).scalar()
            if exist == False:
                db.session.add(presentation13)
                db.session.commit()

        except Exception as e:
            print("An error occurred:", e)
            print("Stack trace:")
            traceback.print_exc()   

    ### didatic attendance 
    didatic_attendance= didatic_attendance.fillna('')
    for i in range(len(didatic_attendance)):
        data = dict(didatic_attendance.iloc[i])
        presentation9 = Didactic_Attendance(**data)
        try:
            exist = db.session.query(exists().where(Didactic_Attendance.MCR_No == data['MCR_No'] ,Didactic_Attendance.MmYyyy == data['MmYyyy'], Didactic_Attendance.Percentage_of_sessions_attended == data['Percentage_of_sessions_attended'] , Didactic_Attendance.Number_of_sessions_attended == data['Number_of_sessions_attended'])).scalar()
            if exist == False:
                db.session.add(presentation9)
                db.session.commit()

        except Exception as e:
            print("An error occurred:", e)
            print("Stack trace:")
            traceback.print_exc()   

    return redirect("http://localhost/FYP-GoodHealth/tab_pages/personal_details.html", code=302)


def getList(items):
    list_ = []
    for i in items:
        list_.append(i.to_dict())
    return list_


@app.route("/profile/<id>")
def read_personaldetailssd(id):
    person = Personal_Details.query.get_or_404(id)

    return jsonify(
        {
            "data": {
                "personaldetails": person.to_dict(),
                "presentations": getList(person.presentations),
                "posting_histories": getList(person.posting_histories),
                "duty_hour_logs": getList(person.duty_hour_logs),
                "case_logs": getList(person.case_logs),
                "procedure_logs": getList(person.procedure_logs),
                "exam_histories": getList(person.exam_histories),
                "publications": getList(person.publications),
                "evaluations": getList(person.evaluations),
                "trgExtRem_Histories": getList(person.trgExtRem_Histories),
                "projects": getList(person.projects),
                "awards": getList(person.awards),
                "grants": getList(person.grants),
                "ihis": getList(person.ihis),
                "involvements": getList(person.involvements),
                "didactic_attendance": getList(person.didactic_attendance),
            }
        }
    ), 200


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

# update involvement
@app.route('/involvement/<int:id>', methods=['PUT'])
def update_involvement(id):
    user = Involvement.query.get(id)
    if not user:
        return 'Involvement not found', 404

    data = request.get_json()
    user.MCR_No = data['MCR_No']
    user.Involvement_Type = data['Involvement_Type']
    user.Event = data['Event']
    user.Role = data['Role']
    user.Start_Date= data['Start_Date']
    user.End_Date = data['End_Date']

    db.session.commit()
    return 'Involvement updated', 200

# remove duty hour log
@app.route('/involvement/<int:id>', methods=['DELETE'])
def delete_involvement(id):
    row = Involvement.query.get(id)
    if not row:
        return 'Involvement not found', 404

    db.session.delete(row)
    db.session.commit()
    return 'Involvement deleted', 200




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
# Read Existing history education (R)
@app.route("/history_education")
def read_history_education():
    history_education_List = Education_History.query.all()
    return jsonify(
        {
            "data": [pd.to_dict()
                     for pd in history_education_List]
        }
    ), 200

# Read History Education field/column name (R)
@app.route('/history_education', methods=['GET'])
def get_history_education_fields():
    fields = {}
    for column in Education_History.__table__.columns:
        fields[column.name] = str(column.type)
    return jsonify(fields)

# Read Existing by Person (R)
@app.route("/history_education/<id>")
def read_histpry_education_by_person(id):
    person = Personal_Details.query.get_or_404(id)
    history_education__of_person = person.hisotry_education
    return jsonify(
        {
            "data": [pd.to_dict()
                     for pd in history_education__of_person]
        }
    ), 200

# update history_education
@app.route('/history_education/<int:id>', methods=['PUT'])
def update_history_education(id):
    user = Education_History.query.get(id)
    if not user:
        return 'History Education not found', 404

    data = request.get_json()
    user.MCR_No = data['MCR_No']
    user.Year_of_Graduation = data['Year_of_Graduation']
    user.Date_of_Graduation = data['Date_of_Graduation']
    user.Basic_Qualification = data['Basic_Qualification']
    user.Medical_School = data['Medical_School']
    user.Country_of_Graduation= data['Country_of_Graduation']
    user.IM_Residency_Start_Date = data['IM_Residency_Start_Date']
    user.IM_Residency_End_Date = data['IM_Residency_End_Date']
    user.SR_Residency_Programme = data['SR_Residency_Programme']
    user.SR_Residency_Start_Date  = data['SR_Residency_Start_Date']
    user.SR_Residency_End_Date  = data['SR_Residency_End_Date']
    user.PG_Year = data['PG_Year']

    db.session.commit()
    return 'History Education updated', 200

# remove history education
@app.route('/history_education/<int:id>', methods=['DELETE'])
def delete_history_education(id):
    row = Education_History.query.get(id)
    if not row:
        return 'History Education not found', 404

    db.session.delete(row)
    db.session.commit()
    return 'History Education deleted', 200

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
# Read Existing  (R)
@app.route("/history_posting")
def read_postinghistory():
    pdList = Posting_History.query.all()
    return jsonify(
        {
            "data": [pd.to_dict()
                     for pd in pdList]
        }
    ), 200

# Read Existing by Person (R)
@app.route("/history_posting/<id>")
def read_postinghistory_by_person(id):
    person = Personal_Details.query.get_or_404(id)
    presentation_of_person = person.posting_histories
    return jsonify(
        {
            "data": [pd.to_dict()
                     for pd in presentation_of_person]
        }
    ), 200

# update history posting
@app.route('/history_posting/<int:id>', methods=['PUT'])
def update_history_posting(id):
    user = Posting_History.query.get(id)
    if not user:
        return 'History Posting not found', 404

    data = request.get_json()
    user.MCR_No = data['MCR_No']
    user.Posting_Institution = data['Posting_Institution']
    user.Posting_Department = data['Posting_Department']
    user.Posting_StartDate = data['Posting_StartDate']
    user.Posting_EndDate = data['Posting_EndDate']

    db.session.commit()
    return 'History Posting updated', 200

# remove history posting
@app.route('/history_posting<int:id>', methods=['DELETE'])
def delete_history_posting(id):
    row = Posting_History.query.get(id)
    if not row:
        return 'History Posting not found', 404

    db.session.delete(row)
    db.session.commit()
    return 'History Posting deleted', 200


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
# Read Existing ExamHistory (R)
@app.route("/history_exam")
def read_examhistory():
    examhistoryList = Exam_History.query.all()
    return jsonify(
        {
            "data": [pd.to_dict()
                     for pd in examhistoryList]
        }
    ), 200

# Read Existing procedure logs with personal details Programme and Year_of_Training (R)
@app.route("/history_exams")
def read_history_exams():
    print("fetching history_exams")
    userList = Exam_History.query\
        .join(Personal_Details, Exam_History.MCR_No == Personal_Details.MCR_No)\
        .add_columns(Personal_Details.Programme)\
        .paginate(1, 50, True)

    combinedProcedureLogs = []
    for i in userList.iter_pages():
        for item in userList.items:
            procedurelog = item[0].to_dict()
            procedurelog["Programme"] = item[1]
            # procedurelog["Year_of_Training"] = item[2]
            combinedProcedureLogs.append(procedurelog)

    return jsonify(
        {
            "data": combinedProcedureLogs
        }), 200

# Read ExamHistory field/column name (R)
@app.route('/history_exam_fields', methods=['GET'])
def get_exam_history_fields():
    fields = {}
    for column in Exam_History.__table__.columns:
        fields[column.name] = str(column.type)
    return jsonify(fields)

# Read Existing by Person (R)
@app.route("/history_exam/<id>")
def read_historyexam_by_person(id):
    person = Personal_Details.query.get_or_404(id)
    examhistory_of_person = person.exam_histories
    return jsonify(
        {
            "data": [pd.to_dict()
                     for pd in examhistory_of_person]
        }
    ), 200

# update history exam
@app.route('/history_exam/<int:id>', methods=['PUT'])
def update_history_exam(id):
    user = Exam_History.query.get(id)
    if not user:
        return 'History Exam not found', 404

    data = request.get_json()
    user.MCR_No = data['MCR_No']
    user.Name_of_Exam = data['Name_of_Exam']
    user.Date_of_Attempty = data['Date_of_Attempt']
    user.Exam_Status = data['Exam_Status']

    db.session.commit()
    return 'History Exam updated', 200

# remove history exam
@app.route('/history_exam/<int:id>', methods=['DELETE'])
def delete_history_exam(id):
    row = Exam_History.query.get(id)
    if not row:
        return 'History Exam not found', 404

    db.session.delete(row)
    db.session.commit()
    return 'History Exam deleted', 200


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
# Read Existing ExamHistory (R)
@app.route("/history_trg")
def read_trghistory():
    trghistoryList =TrgExtRem_History.query.all()
    return jsonify(
        {
            "data": [pd.to_dict()
                    for pd in trghistoryList]
        }
    ), 200

# Read ExamHistory field/column name (R)
@app.route('/history_trg_fields', methods=['GET'])
def get_trg_history_fields():
    fields = {}
    for column in TrgExtRem_History.__table__.columns:
        fields[column.name] = str(column.type)
    return jsonify(fields)

# Read Existing by Person (R)
@app.route("/history_trg/<id>")
def read_historytrg_by_person(id):
    person = Personal_Details.query.get_or_404(id)
    examhistory_of_person = person.exam_histories
    return jsonify(
        {
            "data": [pd.to_dict()
                    for pd in examhistory_of_person]
        }
    ), 200

# update history exam
@app.route('/history_trg/<int:id>', methods=['PUT'])
def update_history_training(id):
    user = TrgExtRem_History.query.get(id)
    if not user:
        return 'History Training not found', 404

    data = request.get_json()
    user.MCR_No = data['MCR_No']
    user.LOAPIP = data['LOAPIP']
    user.StartDate = data['StartDate']
    user.EndDate = data['EndDate']

    db.session.commit()
    return 'History Exam updated', 200

# remove history exam
@app.route('/history_trg/<int:id>', methods=['DELETE'])
def delete_history_training(id):
    row = TrgExtRem_History.query.get(id)
    if not row:
        return 'History Training not found', 404

    db.session.delete(row)
    db.session.commit()
    return 'History Training deleted', 200


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

# update grants
@app.route('/grants/<int:id>', methods=['PUT'])
def update_grants(id):
    user = Grants.query.get(id)
    if not user:
        return 'Grants not found', 404

    data = request.get_json()
    user.MCR_No = data['MCR_No']
    user.Name_of_Grant = data['Name_of_Grant']
    user.Project_Title = data['Project_Title']
    user.Grant_Start_Date = data['Grant_Start_Date']
    user.Grant_End_Date = data['Grant_End_Date']

    db.session.commit()
    return 'Grants updated', 200

# remove grants
@app.route('/grants/<int:id>', methods=['DELETE'])
def delete_grants(id):
    row = Grants.query.get(id)
    if not row:
        return 'Grants not found', 404

    db.session.delete(row)
    db.session.commit()
    return 'Grants deleted', 200



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

# update awards
@app.route('/awards/<int:id>', methods=['PUT'])
def update_awards(id):
    user = Awards.query.get(id)
    if not user:
        return 'Awards not found', 404

    data = request.get_json()
    user.MCR_No = data['MCR_No']
    user.Award_Category = data['Award_Category']
    user.Name_of_Award = data['Name_of_Award']
    user.FY_of_Award_Received = data['FY_of_Award_Received']
    user.Date_of_Award_Received = data['Date_of_Award_Received']
    user.Project_ID = data['Project_ID']

    db.session.commit()
    return 'Awards updated', 200

# remove awards
@app.route('/awards/<int:id>', methods=['DELETE'])
def delete_awards(id):
    row = Awards.query.get(id)
    if not row:
        return 'Awards not found', 404

    db.session.delete(row)
    db.session.commit()
    return 'Awards deleted', 200


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

# Read Awards field/column name (R)
@app.route('/didactic_attendance', methods=['GET'])
def get_didactic_attendance():
    daList = Didactic_Attendance.query.all()
    return jsonify(
        {
            "data": [pd.to_dict()
                     for pd in daList]
        }
    ), 200


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

# Update publications
@app.route('/publication/<int:id>', methods=['PUT'])
def update_publication(id):
    user = Publications.query.get(id)
    if not user:
        return 'Publication not found', 404

    data = request.get_json()
    user.MCR_No = data['MCR_No']
    user.Journal_Title = data['Journal_Title']
    user.PMID = data['PMID']
    user.Publication_Date = data['Publication_Date']
    user.Publication_Title = data['Publication_Title']
    user.id = data['id']

    db.session.commit()
    return 'Publication Log updated', 200

# Delete publications
@app.route('/publication/<int:id>', methods=['DELETE'])
def delete_publication(id):
    row = Publications.query.get(id)
    if not row:
        return 'Publications not found', 404

    db.session.delete(row)
    db.session.commit()
    return 'Publications deleted', 200

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

# Update project
@app.route('/project/<int:id>', methods=['PUT'])
def update_project(id):
    user = Projects.query.get(id)
    if not user:
        return 'Project not found', 404

    data = request.get_json()
    user.MCR_No = data['MCR_No']
    user.Date_of_QI_Certification = data['Date_of_QI_Certification']
    user.End_Date = data['End_Date']
    user.PMID = data['PMID']
    user.Project_ID = data['Project_ID']
    user.Project_Title = data['Project_Title']
    user.Project_Type = data['Project_Type']
    user.Start_Date = data['Start_Date']
    user.id = data['id']

    db.session.commit()
    return 'Project ', id, ' updated', 200

# Delete project
@app.route('/project/<int:id>', methods=['DELETE'])
def delete_project(id):
    row = Projects.query.get(id)
    if not row:
        return 'Project not found', 404

    db.session.delete(row)
    db.session.commit()
    return 'Project ', id, ' deleted', 200


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

# Update ihi
@app.route('/ihi/<int:id>', methods=['PUT'])
def update_ihi(id):
    user = IHI.query.get(id)
    if not user:
        return 'IHI not found', 404

    data = request.get_json()
    user.MCR_No = data['MCR_No']
    user.Completion_of_Emodules = data['Completion_of_Emodules']
    user.Date = data['Date']
    user.id = data['id']

    db.session.commit()
    return 'IHI updated', 200

# Delete IHI
@app.route('/ihi/<int:id>', methods=['DELETE'])
def delete_IHI(id):
    row = IHI.query.get(id)
    if not row:
        return 'IHI not found', 404

    db.session.delete(row)
    db.session.commit()
    return 'IHI deleted', 200
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
    if not all(key in data.keys() for key in ('MCR_No', 'Level', 'Submitted', 'Submitted_Proportion', 'MMYYYY',
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

# update duty hour log
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

# remove duty hour log
@app.route('/duty_hour_log/<int:id>', methods=['DELETE'])
def delete_duty_hour_log(id):
    row = Duty_Hour_Log.query.get(id)
    if not row:
        return 'Duty Hour Log not found', 404

    db.session.delete(row)
    db.session.commit()
    return 'Duty Hour Log deleted', 200

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
    logs = Procedure_Log.query.all()
    return jsonify(
        {
            "data": [pd.to_dict()
                     for pd in logs]
        }
    ), 200

# Read Existing procedure logs with personal details Programme and Year_of_Training (R)
@app.route("/procedure_logs")
def read_procedure_logs():
    userList = Procedure_Log.query\
        .join(Personal_Details, Procedure_Log.MCR_No == Personal_Details.MCR_No)\
        .add_columns(Personal_Details.Programme, Personal_Details.Year_of_Training)\
        .paginate(1, 50, True)

    combinedProcedureLogs = []
    for i in userList.iter_pages():
        for item in userList.items:
            procedurelog = item[0].to_dict()
            procedurelog["Programme"] = item[1]
            procedurelog["Year_of_Training"] = item[2]
            combinedProcedureLogs.append(procedurelog)

    return jsonify(
        {
            "data": combinedProcedureLogs
        }), 200

# Add procedure log
@app.route('/add_procedure_log', methods=['POST'])
def create_procedure_log():
    data = request.get_json()
    if not all(key in data.keys() for key in ('MCR_No', 'Procedure_Name', 'CPT', 'Date of Completion', 'Total',
                                            'Performed' , 'Observed' , 'Verified' , 'Certified'
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

# Update procedure log
@app.route('/procedurelog/<int:id>', methods=['PUT'])
def update_procedure_log(id):
    user = Procedure_Log.query.get(id)
    if not user:
        return 'Procedure Log not found', 404

    data = request.get_json()
    user.MCR_No = data['MCR_No']
    user.Certified = data['Certified']
    user.Date_of_Completion = data['Date_of_Completion']
    user.Observed = data['Observed']
    user.Performed = data['Performed']
    user.Procedure_Name = data['Procedure_Name']
    user.Total = data['Total']
    user.Verified = data['Verified']


    db.session.commit()
    return 'Procedure Log updated', 200

# Delete procedure log
@app.route('/procedurelog/<int:id>', methods=['DELETE'])
def delete_procedure_log(id):
    row = Procedure_Log.query.get(id)
    if not row:
        return 'Procedure Log not found', 404

    db.session.delete(row)
    db.session.commit()
    return 'Procedure Log deleted', 200

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
@app.route("/case_logs")
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

# Update caselog
@app.route('/caselog/<int:id>', methods=['PUT'])
def update_caselog(id):
    user = Case_Log.query.get(id)
    if not user:
        return 'caselog not found', 404

    data = request.get_json()
    user.MCR_No = data['MCR_No']
    user.CPT = data['CPT']
    user.Case_Name = data['Case_Name']
    user.Certified = data['Certified']
    user.Date_of_Log = data['Date_of_Log']
    user.Observed = data['Observed']
    user.Performed = data['Performed']
    user.Subspecialty = data['Subspecialty']
    user.Total = data['Total']
    user.Type_of_Case_Log = data['Type_of_Case_Log']
    user.Verified = data['Verified']
    db.session.commit()
    return 'caselog updated', 200

# Delete IHI
@app.route('/caselog/<int:id>', methods=['DELETE'])
def delete_caselog(id):
    row = Case_Log.query.get(id)
    if not row:
        return 'caselog not found', 404

    db.session.delete(row)
    db.session.commit()
    return 'caselog deleted', 200
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


@app.route("/evaluations")
def read_evaluation():
    res = Evaluations.query.all()
    return jsonify(
        {
            "data": [r.to_dict()
                     for r in res]
        }
    ), 200

# Update Evaluation
@app.route('/evaluation/<int:id>', methods=['PUT'])
def update_evaluation(id):
    user = Evaluations.query.get(id)
    if not user:
        return 'evaluation not found', 404

    data = request.get_json()
    user.MCR_No = data['MCR_No']
    user.Answer = data['Answer']
    user.Evaluator = data['Evaluator']
    user.Name_of_Evaluation_Form = data['Name_of_Evaluation_Form']
    user.Question_Number = data['Question_Number']
    user.Rotation_Period = data['Rotation_Period']
    user.Score = data['Score']
    user.Service = data['Service']
    user.Year_of_Training = data['Year_of_Training']

    db.session.commit()
    return 'evaluation updated', 200

# Delete Evaluation
@app.route('/evaluation/<int:id>', methods=['DELETE'])
def delete_evaluation(id):
    row = Evaluations.query.get(id)
    if not row:
        return 'evaluation not found', 404

    db.session.delete(row)
    db.session.commit()
    return 'evaluation deleted', 200


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
        person = Personal_Details.query.get_or_404(data["MCR_No"])
    else:
        return jsonify(
            {
                "Error Msg": "MCR_No not present in database"
            }
        ), 404
    if not all(key in data.keys() for key in ('MCR_No', 'Title', 'Conference_Name', 'Type',
                                              'Project_ID', 'Country', 'Presentation_Date')):
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


@app.route('/presentation/<int:id>', methods=['PUT'])
def update_presentation(id):
    user = Presentations.query.get(id)
    if not user:
        return 'Presentation not found', 404

    data = request.get_json()
    user.MCR_No = data['MCR_No']
    user.Conference_Name = data['Conference_Name']
    user.Country = data['Country']
    user.Presentation_Date = data['Presentation_Date']
    user.Project_ID = data['Project_ID']
    user.Title = data['Title']
    user.Type = data['Type']
    user.id = data['id']

    db.session.commit()
    return 'Presentation updated', 200

@app.route('/presentation/<int:id>', methods=['DELETE'])
def delete_presentation(id):
    row = Presentations.query.get(id)
    if not row:
        return 'presentation not found', 404

    db.session.delete(row)
    db.session.commit()
    return 'presentation deleted', 200




# import pdfkit
# from pdfkit.api import configuration

# wkhtml_path = pdfkit.configuration(wkhtmltopdf = r"C:\Users\feryo\OneDrive\Documents\GitHub\wkhtmltopdf\bin\wkhtmltopdf.exe")  #by using configuration you can add path value.



# ============================
# CV TEMPLATE SECTION
# ============================
# Generate CV word
@app.route("/cv_word/<id>")
def pdf_to_doc(id):
    generatepdf(id)
    from pdf2docx import parse
    folder = "./cv/"
    pdf_file = folder + 'cv.pdf'
    docx_file = folder + 'cv.docx'

    # convert pdf to docx
    parse(pdf_file, docx_file)
    import os
    path = os.getcwd() + "/cv/cv.docx"
    return send_file(path, as_attachment=True)

from helper import  getAwardsRows, getProjectRows, getEducationalInvolvement, \
    getCommunityInvolvement, getLeadershipInvolvment, getProcedureLogs, getPostingRows,\
    getEducationRows, getPresentationRows,getTeachingPresentationRows,getPublications,getPage,\
    getQIPatientSafetyRows

# Generate CV pdf:
@app.route("/cv_pdf/<id>")
def generate_cv(id):
    generatepdf(id)
    import os
    path = os.getcwd() + "/cv/cv.pdf"
    return send_file(path, as_attachment=True)

def generatepdf(id):
    person = Personal_Details.query.get_or_404(id)
    presentations = person.presentations
    posting_histories = person.posting_histories
    duty_hour_logs = person.duty_hour_logs
    case_logs = person.case_logs
    procedure_logs = person.procedure_logs
    exam_histories = person.exam_histories
    publications = person.publications
    evaluations = person.evaluations
    trgExtRem_Histories = person.trgExtRem_Histories
    projects = person.projects
    awards = person.awards
    grants = person.grants
    ihis = person.ihis
    involvements = person.involvements
    mcrno = person.MCR_No
    name = person.Staff_Name
    education_histories = person.education_history
    
    awardsRows = getAwardsRows(awards)
    projectRows = getProjectRows(projects)
    educationalInvolvements = getEducationalInvolvement(involvements)
    communityInvolvements = getCommunityInvolvement(involvements)
    leadershipInvolvements =  getLeadershipInvolvment(involvements)
    procedureLogsRows = getProcedureLogs(procedure_logs)
    postingRows = getPostingRows(posting_histories)
    educationRows = getEducationRows(exam_histories)
    teachingPresentationRows=getTeachingPresentationRows(presentations)
    presentationRows=getPresentationRows(presentations)
    publicationRows=getPublications(publications)
    patientSafetyQIRows=getQIPatientSafetyRows(projects)
    
    page = getPage(name, mcrno, awardsRows, projectRows, educationalInvolvements, communityInvolvements,
        leadershipInvolvements, procedureLogsRows, postingRows, educationRows,presentationRows,teachingPresentationRows,
        publicationRows,patientSafetyQIRows)

    folder = "./cv/"
    html_file_name = folder + "cv.html"
    Func = open(html_file_name,"w")
    Func.write(page)
    Func.close()
    import pdfkit
    from pathlib import Path
    input = Path(html_file_name)
    pdfkit.from_file(html_file_name, folder +'cv.pdf')

db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011, debug=True)

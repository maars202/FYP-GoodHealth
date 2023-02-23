from sqlalchemy import insert, text, create_engine,inspect
from flask import abort
from flask import Flask, request, jsonify, render_template, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json
import pandas as pd
import traceback
import werkzeug.exceptions as ex
# Read PersonalDetails field/column name (R)
########################################################################################
from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from __init__ import create_app, db

# ########################################################################################

# app = Blueprint('app', __name__)
app = Flask(__name__)

# db = SQLAlchemy(app)

# CORS(app)
# app = Flask(__name__)
app.app_context().push()

if __name__ == '__main__':
    # Mac user -------------------------------------------------------------------
    # app.config['SECRET_KEY'] = 'secret-key-goes-here' # it is used by Flask and extensions to keep data safe
    import os
    app.config["SECRET_KEY"] = os.environ.get(
    "SECRET_KEY", "0aedgaii451cef0af8bd6432ec4b317c8999a9f8g77f5f3cb49fb9a8acds51d"
)   
    import os
    app.config["SECURITY_PASSWORD_SALT"] = os.environ.get(
        "SECURITY_PASSWORD_SALT",
        "ab3d3a0f6984c4f5hkao41509b097a7bd498e903f3c9b2eea667h16",
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root' + \
                                           '@localhost:3306/SingHealth'
    engine = create_engine('mysql+pymysql://root:root@localhost/SingHealth?charset=utf8')

    # --------------------------------------------------------------------------------

    # # Windows user -------------------------------------------------------------------
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root' + \
    #                                         '@localhost:3306/SingHealth'
    # engine = create_engine('mysql+pymysql://root:root@localhost/SingHealth?charset=utf8')

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                            'pool_recycle': 280}
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)

########################################################################################
# our main blueprint
main = Blueprint('main', __name__)

@main.route('/') # home page that return 'index'
def index():
    return render_template('base.html')

@main.route('/profile2', methods=['GET'])
@login_required
def display():
    # return render_template('profile2.html', name=current_user.name)
    return render_template('profile2.html', name=current_user.username)
    # return "hello"

@main.route('/r', methods=['GET'])
# @login_required
def display2():
    return render_template('hello.html')

from flask_security import roles_accepted
@main.route('/homepage', methods=['GET'])
# @login_required
@roles_accepted('Admin')
def homepage():
    return render_template('homepage2.html')


from flask_login import UserMixin
# from __init__ import db

# class User2(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
#     email = db.Column(db.String(100), unique=True)
#     password = db.Column(db.String(100))
#     name = db.Column(db.String(1000))


from flask_login import LoginManager

login_manager = LoginManager() # Create a Login Manager instance
login_manager.login_view = 'auth.login' # define the redirection path when login required and we attempt to access without being logged in
# login_mgr.login_view = 'login'
login_manager.refresh_view = 'auth.login'
login_manager.needs_refresh_message = (u"Session timedout, please re-login")
login_manager.needs_refresh_message_category = "info"

login_manager.init_app(app) # configure it for login

# added:
from flask_security import SQLAlchemySessionUserDatastore, Security
from models import User, Role
user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)

# blueprint for auth routes in our app
# blueprint allow you to orgnize your flask app
from auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)
# blueprint for non-auth parts of app
# from main import main as main_blueprint
app.register_blueprint(main)
print("registerddd")


security = Security(app, user_datastore)
from models import User
@login_manager.user_loader
def load_user(user_id): #reload user object from the user ID stored in the session
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))


from flask import session
from datetime import timedelta
@app.before_request
def before_request():
    print("before request")
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=1)

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
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    MCR_No = db.Column(db.String(100),  db.ForeignKey(
        'Personal_Details.MCR_No'))
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
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result


class Posting_History(db.Model):
    __tablename__ = 'Posting_History'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    MCR_No = db.Column(db.String(100),  db.ForeignKey(
        'Personal_Details.MCR_No'))
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
    Project_Type = db.Column(db.String(100))
    Project_Title = db.Column(db.String(100))
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
    didatic_attendance.columns = [ 'MCR_No', 'Billing Name', 'Month' , 'Total_tracked_sessions' , 'Number_of_sessions_attended'  , 'Percentage_of_sessions_attended', 'MmYyyy' , 'Posting Institution', 'Posting Department',	'Scheduled Teachings', 'Compliance_or_Not' , "Percentage_of_sessions_attended"]

    if didatic_attendance['MCR_No'].isnull().sum() > 0 or ihi['MCR_No'].isnull().sum() > 0 or ihi.duplicated().any() or project['MCR_No'].isnull().sum() > 0 or project.duplicated().any() or presentations['MCR_No'].isnull().sum() > 0 or presentations.duplicated().any() or publlications['MCR_No'].isnull().sum() > 0 or publlications.duplicated().any() or awards['MCR_No'].isnull().sum() > 0 or awards.duplicated().any() or grants['MCR_No'].isnull().sum() > 0 or grants.duplicated().any() or personalDetails['MCR_No'].isnull().sum() > 0 or personalDetails['Employee_ID'].isnull().sum() > 0 or (personalDetails.duplicated().any()) or involvement['MCR_No'].isnull().sum() > 0 or (involvement.duplicated().any()) or history_education['MCR_No'].isnull().sum() > 0 or (history_education.duplicated().any()) or history_posting['MCR_No'].isnull().sum() > 0 or history_posting.duplicated().any() or history_exam['MCR_No'].isnull().sum() > 0 or history_exam.duplicated().any() or history_trg['MCR_No'].isnull().sum() > 0 or history_trg.duplicated().any():
        writer = pd.ExcelWriter("error.xlsx", engine='xlsxwriter')
        workbook = writer.book
        format1 = workbook.add_format({'bg_color': '#FF8080'})
        ## personal_DETAILS
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
        didatic_attendance.to_excel(
            writer, sheet_name='didatic_attendance_error')
        workbook = writer.book
        worksheet = writer.sheets['didatic_attendance_error']
        format1 = workbook.add_format({'bg_color': '#FF8080'})
        nullrows = awards[awards[[
        "MCR_No"]].isnull().any(axis=1)]

        for row in nullrows.index:
            ran = "A" + str(row+2) + ":BA" + str(row+2)
            worksheet.conditional_format(ran,
                                            {'type':     'cell',
                                            'criteria': 'not equal to',
                                            'value': '"o1"',
                                            'format':   format1})
            
        writer.save()
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
            db.session.add(presentation9)
            db.session.commit()

        except Exception as e:
            print("An error occurred:", e)
            print("Stack trace:")
            traceback.print_exc()   

    

    return history_posting.to_html()



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
    if not all(key in data.keys() for key in ('MCR_No', 'Award_ID', 'Employee_id', "Award_Category", "Name_of_Award", "FY_of_Award_Received",
                                            "Date_of_Award_Received", "Project_ID_Ref"
                                            )):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    awards = Awards(**data)
    try:
        db.session.add(awards)
        db.session.commit()
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


@app.route('/duty_hour_log/<int:id>', methods=['DELETE'])
def delete_duty_hour_log(id):
    row = Duty_Hour_Log.query.get(id)
    if not row:
        return 'Duty Hour Log not found', 404

    db.session.delete(row)
    db.session.commit()
    return 'Duty Hour Log deleted', 200

# insp = inspect(engine)
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
        

        
@app.route('/edit_field_value', methods=['POST'])
def edit_field_value():
    data = request.get_json()
    table=data['Table']
    field = data['Field']
    value=data['Value']
    row=data['Row']
    connection = engine.connect()
    update_query=f'UPDATE {table} SET {field} = \'{value}\' WHERE MCR_No = \'{row}\''
    try:
        connection.execute(update_query)
        return jsonify(data.to_dict()), 201
    except Exception as e:
        print("An error occurred:", e)
        traceback.print_exc()
        return jsonify(
            {
                "Error Msg": "error occured"
            }
        ), 404
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

# ============================
# CV TEMPLATE SECTION
# ============================
# Generate CV word
@app.route("/worddoc/<id>")
def pdf_to_doc(id):
    generate_cv(id)
    from pdf2docx import parse

    pdf_file = './cv/cv.pdf'
    docx_file = './cv/cv.docx'

    # convert pdf to docx
    parse(pdf_file, docx_file)
    return "done"

from helper import  getAwardsRows, getProjectRows, getEducationalInvolvement, \
    getCommunityInvolvement, getLeadershipInvolvment, getProcedureLogs, getPostingRows,\
    getEducationRows, getPage

# Generate CV pdf:
@app.route("/personaldetails_cv_generate/<id>")
def generate_cv(id):
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
    
    page = getPage(name, mcrno, awardsRows, projectRows, educationalInvolvements, communityInvolvements,
        leadershipInvolvements, procedureLogsRows, postingRows, educationRows)

    html_file_name = "./cv/cv.html"
    Func = open(html_file_name,"w")
    Func.write(page)
    Func.close()
    import pdfkit
    from pathlib import Path
    input = Path(html_file_name)
    pdfkit.from_file(html_file_name, 
    './cv/cv.pdf')
    return "done"


db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011, debug=True)

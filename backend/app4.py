import os
from flask import Flask, render_template, request, redirect, url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
# basedir = os.path.abspath(os.path.dirname(__file__))

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] =\
#            'sqlite:///' + os.path.join(basedir, 'database.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app = Flask(__name__)
app.app_context().push()

if __name__ == '__main__':
    # Mac user -------------------------------------------------------------------
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root' + \
                                            '@localhost:3306/Posts'
    # --------------------------------------------------------------------------------

    # # Windows user -------------------------------------------------------------------
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root' + \
    #                                         '@localhost:3306/SingHealth'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
    #                                         'pool_recycle': 280}
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)

class Personal_Details(db.Model):
    __tablename__ = 'Personal_Details'
    Employee_id = db.Column(db.String(50), primary_key=True)
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
    Personal_Details_deleted = db.Column(db.Boolean(), default=False, nullable=False)

    didactic_attendence = db.relationship('Didactic_Attendance', backref='Personal_Details')
    duty_hour_log = db.relationship('Duty_Hour_Log', backref='Personal_Details')
    education_history = db.relationship('Education_History', backref='Personal_Details')
    evaluations = db.relationship('Evaluations', backref='Personal_Details')
    exam_history = db.relationship('Exam_History', backref='Personal_Details')
    grants = db.relationship('Grants', backref='Personal_Details')
    IHIs = db.relationship('IHI', backref='Personal_Details')
    involvements = db.relationship('Involvement', backref='Personal_Details')
    procedure_logs = db.relationship('Procedure_Log', backref='Personal_Details')
    projects = db.relationship('Projects', backref='Personal_Details')
    publications = db.relationship('Publications', backref='Personal_Details')
    trgextremhistory = db.relationship('TrgExtRemHistory', backref='Personal_Details')

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

class Didactic_Attendance(db.Model):
    __tablename__ = 'Didactic_Attendance'
    id = db.Column(db.Integer, primary_key=True)
    Employee_id = db.Column(db.String(100), db.ForeignKey('Personal_Details.Employee_id'))
    BillingName = db.Column(db.String(100))
    Month = db.Column(db.String(100))
    Total_tracked_sessions = db.Column(db.String(100))
    Number_of_sessions_attended = db.Column(db.String(100))
    Percentage_of_sessions_attended = db.Column(db.String(100))
    MmYyyy = db.Column(db.String(100))
    Posting_Institution = db.Column(db.String(100))
    Posting_Department = db.Column(db.String(100))
    Scheduled_Teachings = db.Column(db.String(100))
    Compliance_or_Not = db.Column(db.String(100))
    Didactic_Attendance_deleted = db.Column(db.Boolean(), default=False, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'Didactic_Attendance'
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
    id = db.Column(db.Integer, primary_key=True)
    Employee_id = db.Column(db.String(100), db.ForeignKey('Personal_Details.Employee_id'))
    Level = db.Column(db.String(100))
    Submitted = db.Column(db.String(100))
    Submitted_Proportion = db.Column(db.String(100))
    MMYYYY = db.Column(db.String(100))
    Logged_for_month = db.Column(db.String(100))
    Duty_Hour_Log_deleted = db.Column(db.Boolean(), default=False, nullable=False)

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

class Education_History(db.Model):
    __tablename__ = 'Education_History'
    id = db.Column(db.Integer, primary_key=True)
    Employee_id = db.Column(db.String(100), db.ForeignKey('Personal_Details.Employee_id'))
    Year_of_Graduation = db.Column(db.String(50))
    Date_of_Graduation = db.Column(db.String(50))
    Basic_Qualification = db.Column(db.String(50))
    Medical_School = db.Column(db.String(50))
    Country_of_Graduation = db.Column(db.String(50))
    IM_Residency_Start_Date = db.Column(db.String(50))
    IM_Residency_End_Date = db.Column(db.String(50))
    SR_Residency_Programme = db.Column(db.String(50))
    SR_Residency_Start_Date = db.Column(db.String(50))
    SR_Residency_End_Date = db.Column(db.String(50))
    PG_Year = db.Column(db.String(50))
    Education_History_deleted=db.Column(db.Boolean(), default=False, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'Education_History'
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
    id = db.Column(db.Integer, primary_key=True)
    Employee_id = db.Column(db.String(100), db.ForeignKey('Personal_Details.Employee_id'))
    Year_of_Training = db.Column(db.String(50))
    Rotation_Period = db.Column(db.String(50))
    Name_of_Evaluation_Form = db.Column(db.String(50))
    Question_Number = db.Column(db.String(50))
    Score = db.Column(db.String(50))
    Evaluator = db.Column(db.String(50))
    Service = db.Column(db.String(50))
    Answer = db.Column(db.String(50))
    Evaluations_deleted = db.Column(db.Boolean(), default=False, nullable=False)

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

class Exam_History(db.Model):
    __tablename__ = 'Exam_History'
    id = db.Column(db.Integer, primary_key=True)
    Employee_id = db.Column(db.String(100), db.ForeignKey('Personal_Details.Employee_id'))
    Name_of_Exam = db.Column(db.String(50))
    Date_of_Attempt = db.Column(db.String(50))
    Exam_Status = db.Column(db.String(50))
    Exam_History_deleted = db.Column(db.Boolean(), default=False, nullable=False)

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

class Grants(db.Model):
    __tablename__ = 'Grants'
    id = db.Column(db.Integer, primary_key=True)
    Employee_id = db.Column(db.String(100), db.ForeignKey('Personal_Details.Employee_id'))
    Name_of_Grant = db.Column(db.String(50))
    Project_Title = db.Column(db.String(50))
    Project_ID = db.Column(db.String(50))
    Grant_End_Date = db.Column(db.String(50))
    Grant_Start_Date = db.Column(db.String(50))
    Grants_deleted = db.Column(db.Boolean(), default=False, nullable=False)

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
    id = db.Column(db.Integer, primary_key=True)
    Employee_id = db.Column(db.String(100), db.ForeignKey('Personal_Details.Employee_id'))
    Completion_of_Emodules = db.Column(db.String(50))
    Date = db.Column(db.String(50))
    IHI_deleted = db.Column(db.Boolean(), default=False, nullable=False)

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
    id = db.Column(db.Integer, primary_key=True)
    Employee_id = db.Column(db.String(100), db.ForeignKey('Personal_Details.Employee_id'))
    Involvement_Type = db.Column(db.String(50))
    Event = db.Column(db.String(50))
    Role = db.Column(db.String(50))
    Start_Date = db.Column(db.String(50))
    End_Date = db.Column(db.String(50))
    Involvement_deleted = db.Column(db.Boolean(), default=False, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'Involvement'
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
    id = db.Column(db.Integer, primary_key=True)
    Employee_id = db.Column(db.String(100), db.ForeignKey('Personal_Details.Employee_id'))
    Procedure_Name = db.Column(db.String(50))
    Date_of_Completion = db.Column(db.String(50))
    CPT = db.Column(db.String(50))
    Total = db.Column(db.String(50))
    Performed = db.Column(db.String(50))
    Observed = db.Column(db.String(50))
    Verified = db.Column(db.String(50))
    Certified = db.Column(db.String(50))
    Procedure_Log_deleted = db.Column(db.Boolean(), default=False, nullable=False)

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

class Projects(db.Model):
    __tablename__ = 'Projects'
    id = db.Column(db.Integer, primary_key=True)
    Employee_id = db.Column(db.String(100), db.ForeignKey('Personal_Details.Employee_id'))
    Project_Type = db.Column(db.String(50))
    Project_Title = db.Column(db.String(50))
    Project_ID = db.Column(db.String(50))
    Start_Date = db.Column(db.String(50))
    End_Date = db.Column(db.String(50))
    Date_of_QI_Certification = db.Column(db.String(50))
    PMID = db.Column(db.String(50))
    Project_deleted = db.Column(db.Boolean(), default=False, nullable=False)

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


class Publications(db.Model):
    __tablename__ = 'Publications'
    id = db.Column(db.Integer, primary_key=True)
    Employee_id = db.Column(db.String(100), db.ForeignKey('Personal_Details.Employee_id'))
    Publication_Title = db.Column(db.String(50))
    Journal_Title = db.Column(db.String(50))
    PMID = db.Column(db.String(50))
    Publication_Date = db.Column(db.String(50))
    Publication_deleted = db.Column(db.Boolean(), default=False, nullable=False)

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

class TrgExtRemHistory(db.Model):
    __tablename__ = 'TrgExtRemHistory'
    id = db.Column(db.Integer, primary_key=True)
    Employee_id = db.Column(db.String(100), db.ForeignKey('Personal_Details.Employee_id'))
    LOAPIP = db.Column(db.String(50))
    StartDate = db.Column(db.String(50))
    EndDate = db.Column(db.String(50))
    TrgExtRemHistory_deleted = db.Column(db.Boolean(), default=False, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'TrgExtRemHistory'
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

@app.route('/')
def index():
    posts = Personal_Details.query.all()
    # return render_template('index.html', posts=posts)
    return jsonify(
        {
            "data": [pd.to_dict()
                     for pd in posts]
        }
    ), 200


@app.route('/id')
def index2():
    post_id = "one111"
    post = Personal_Details.query.get_or_404(post_id)
    postcomments = post.didactic_attendence
    # return render_template('index.html', posts=posts)
    return jsonify(
        {
            "data": [i.to_dict() for i in postcomments]
        }
    ), 200


def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d


@app.route('/didactic_attendance_table')
def index4():

    posts = Personal_Details.query.all()
    combined = []
    for post in posts:
        for i in post.didactic_attendence:
            combined.append({**(post.to_dict()), **(i.to_dict())})
    return jsonify(
        {
            "data": combined
        }
    ), 200

@app.route('/duty_Hour_log_table')
def index5():

    posts = Personal_Details.query.all()
    combined = []
    for post in posts:
        for i in post.duty_hour_log:
            combined.append({**(post.to_dict()), **(i.to_dict())})
    return jsonify(
        {
            "data": combined
        }
    ), 200

@app.route('/education_history_table')
def get_education_history_table():

    posts = Personal_Details.query.all()
    combined = []
    for post in posts:
        for i in post.education_history:
            combined.append({**(post.to_dict()), **(i.to_dict())})
    return jsonify(
        {
            "data": combined
        }
    ), 200

@app.route('/evaluations_table')
def get_evaluations_table():

    posts = Personal_Details.query.all()
    combined = []
    for post in posts:
        for i in post.evaluations:
            combined.append({**(post.to_dict()), **(i.to_dict())})
    return jsonify(
        {
            "data": combined
        }
    ), 200

@app.route('/exam_history_table')
def get_exam_history_table():

    posts = Personal_Details.query.all()
    combined = []
    for post in posts:
        for i in post.exam_history:
            combined.append({**(post.to_dict()), **(i.to_dict())})
    return jsonify(
        {
            "data": combined
        }
    ), 200


@app.route('/grants_table')
def get_exam_grants_table():

    posts = Personal_Details.query.all()
    combined = []
    for post in posts:
        for i in post.grants:
            combined.append({**(post.to_dict()), **(i.to_dict())})
    return jsonify(
        {
            "data": combined
        }
    ), 200

@app.route('/ihi_table')
def get_ihi_table():

    posts = Personal_Details.query.all()
    combined = []
    for post in posts:
        for i in post.IHIs:
            combined.append({**(post.to_dict()), **(i.to_dict())})
    return jsonify(
        {
            "data": combined
        }
    ), 200

@app.route('/involvement_table')
def get_involvement_table():

    posts = Personal_Details.query.all()
    combined = []
    for post in posts:
        for i in post.involvements:
            combined.append({**(post.to_dict()), **(i.to_dict())})
    return jsonify(
        {
            "data": combined
        }
    ), 200

    # procedure_logs
@app.route('/procedure_logs_table')
def get_procedure_logs_table():

    posts = Personal_Details.query.all()
    combined = []
    for post in posts:
        for i in post.procedure_logs:
            combined.append({**(post.to_dict()), **(i.to_dict())})
    return jsonify(
        {
            "data": combined
        }
    ), 200

@app.route('/projects_table')
def get_projects_table():

    posts = Personal_Details.query.all()
    combined = []
    for post in posts:
        for i in post.projects:
            combined.append({**(post.to_dict()), **(i.to_dict())})
    return jsonify(
        {
            "data": combined
        }
    ), 200


@app.route('/publications_table')
def get_publications_table():

    posts = Personal_Details.query.all()
    combined = []
    for post in posts:
        for i in post.publications:
            combined.append({**(post.to_dict()), **(i.to_dict())})
    return jsonify(
        {
            "data": combined
        }
    ), 200

@app.route('/trgextremhistory_table')
def get_trgextremhistory_table():

    posts = Personal_Details.query.all()
    combined = []
    for post in posts:
        for i in post.trgextremhistory:
            combined.append({**(post.to_dict()), **(i.to_dict())})
    return jsonify(
        {
            "data": combined
        }
    ), 200


db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)
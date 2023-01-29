from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
# # Mac user ====================================================================
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:' + \
                                        '@localhost:3306/SingHealth'
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
    print("herrr")
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)

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

class Awards(db.Model):
    __tablename__ = 'Awards'
    Award_ID = db.Column(db.String(100))
    Employee_id = db.Column(db.String(100), primary_key=True)
    Award_Category = db.Column(db.String(100))
    Name_of_Award = db.Column(db.String(100))

    FY_of_Award_Received = db.Column(db.String(100))
    Date_of_Award_Received = db.Column(db.DateTime)
    Project_ID_Ref = db.Column(db.String(100))

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

class ExamHistory(db.Model):
    __tablename__ = 'ExamHistory'
    Exam_ID = db.Column(db.String(100))
    Employee_id = db.Column(db.String(100), primary_key=True)
    Name_of_Exam = db.Column(db.String(100))
    Date_of_Attempts = db.Column(db.String(100))
    Exam_Status = db.Column(db.String(100))

    __mapper_args__ = {
        'polymorphic_identity': 'ExamHistory'
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
    Grant_ID = db.Column(db.String(100))
    Employee_id = db.Column(db.String(100), primary_key=True)
    Name_of_Grant = db.Column(db.String(100))
    Project_Title = db.Column(db.String(100))
    Project_ID = db.Column(db.String(100))
    Grant_End_Date = db.Column(db.DateTime)

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


class Involvement(db.Model):
    __tablename__ = 'Involvement'
    Involvement_No = db.Column(db.Integer)
    Involvement_Type = db.Column(db.String(100))
    Employee_id = db.Column(db.String(100), primary_key=True)
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


# Read Existing examhistory (R)
@app.route("/examhistory")
def read_examhistory():
    examhistoryList = ExamHistory.query.all()
    return jsonify(
        {
            "data": [pd.to_dict()
                    for pd in examhistoryList]
        }
    ), 200

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




db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)
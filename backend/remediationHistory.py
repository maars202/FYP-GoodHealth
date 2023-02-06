from flask import request, jsonify
from app import app,db
# from __main__ import app,db


class RemediationHistory(db.Model):
    __tablename__ = 'TrgExtRemHistory'

    Remediation_ID= db.Column(db.String(100), primary_key=True)
    Employee_ID = db.Column(db.String(100),  db.ForeignKey('PersonalDetails.Employee_id'))
    
    Exam_Name = db.Column(db.String(100))
    LOAPIP = db.Column(db.String(100))
    
    StartDate = db.Column(db.DateTime)
    EndDate = db.Column(db.DateTime)


    __mapper_args__ = {
        'polymorphic_identity': 'TrgExtRemHistory'
    }

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        # print(f"columns: {columns}")
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

# Read Existing personaldetails (R)
@app.route("/remediationhistory")
def read_remediationhistory():
    pdList = RemediationHistory.query.all()
    print (pdList,'oierjngosenrboaeir!!!!!!!!!!!!!!!!!!!!!!OSJNWOJN')
    return jsonify(
        {
            "data": [pd.to_dict()
                    for pd in pdList]
        }
    ), 200
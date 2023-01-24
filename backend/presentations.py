from flask import request, jsonify
from __main__ import app,db


class Presentation(db.Model):
    __tablename__ = 'Presentations'

    Presentation_ID= db.Column(db.String(100), primary_key=True)
    Employee_ID = db.Column(db.String(100),  db.ForeignKey('PersonalDetails.Employee_id'))
    Title = db.Column(db.String(100))
    Conference_Name = db.Column(db.String(100))
    Type = db.Column(db.String(100))
    Conference_Name = db.Column(db.DateTime)
    Country = db.Column(db.DateTime)
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

# Read Existing personaldetails (R)
@app.route("/presentations")
def read_presentations():
    pdList = Presentation.query.all()
    print (pdList,'oierjngosenrboaeir!!!!!!!!!!!!!!!!!!!!!!OSJNWOJN')
    return jsonify(
        {
            "data": [pd.to_dict()
                    for pd in pdList]
        }
    ), 200
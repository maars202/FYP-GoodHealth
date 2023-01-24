from flask import request, jsonify
from __main__ import app,db


class Publications(db.Model):
    __tablename__ = 'Publications'

    Publication_ID= db.Column(db.String(100), primary_key=True)
    Employee_ID = db.Column(db.String(100),  db.ForeignKey('PersonalDetails.Employee_id'))
    
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

# Read Existing personaldetails (R)
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
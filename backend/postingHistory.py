
from flask import request, jsonify
from app import app,db
# from __main__ import app,db
from sqlalchemy import create_engine
import os, fileinput
  
user, password, host, database = 'root', 'root', 'localhost', 'SingHealth'
engine = create_engine(
    url=f'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8')
  
connection = engine.connect()

metadata_obj = db.MetaData()

class PostingHistory(db.Model):
    __tablename__ = 'PostingHistory'

    Posting_ID= db.Column(db.String(100), primary_key=True)
    Employee_ID = db.Column(db.String(100),  db.ForeignKey('PersonalDetails.Employee_id'))
    Designation= db.Column(db.String(100))

    Posting_Institution = db.Column(db.String(100))
    Posting_Department = db.Column(db.DateTime)
    Posting_StartDate = db.Column(db.DateTime)
    Posting_EndDate = db.Column(db.String(100))


    __mapper_args__ = {
        'polymorphic_identity': 'PostingHistory'
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

# Read Existing  (R)
@app.route("/postinghistory")
def read_postinghistory():
    pdList = PostingHistory.query.all()
    print (pdList,'oierjngosenrboaeir!!!!!!!!!!!!!!!!!!!!!!OSJNWOJN')
    return jsonify(
        {
            "data": [pd.to_dict()
                    for pd in pdList]
        }
    ), 200


### ADD COLUMN, NOT YET OFFICIAL FUNCTION
@app.route("/postinghistory/addcolumn",methods=['POST'])
def add_posting_column():
    data = request.get_json()
    column=data['column']
    table_name = 'PostingHistory'
    
    query = f'ALTER TABLE {table_name} ADD {column} VARCHAR(50) ;'
    connection.execute(query)
    for line in fileinput.FileInput('postingHistory.py', inplace=True):
        
        if line.startswith('    __tablename__'):
            line += '    '+column+"=db.Column(db.String(100))"+ os.linesep
            
        print(line, end="")

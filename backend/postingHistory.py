
from flask import request, jsonify
from __main__ import app,db
from sqlalchemy import create_engine
  
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

# Read Existing personaldetails (R)
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

@app.route("/postinghistory/addcolumn")
def add_posting_column():
    table_name = 'PostingHistory'
    
    query = f'ALTER TABLE {table_name} ADD pootpoot VARCHAR(50) ;'
    connection.execute(query)


@app.route("/createtable")
def create_table():
    profile = db.Table(
    'profile',                                        
    metadata_obj,                                    
    db.Column('email', db.String(50), primary_key=True),  
    db.Column('name', db.String(50)),                    
    db.Column('contact', db.String(50)),                
    )
  
    # Create the profile table
    metadata_obj.create_all(engine)
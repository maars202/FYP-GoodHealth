from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
import os, fileinput


from sqlalchemy import create_engine

app = Flask(__name__)

# Remember to add/remove the app config with your php password
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get(
    'dbURL') or 'mysql+mysqlconnector://root:root@localhost:3306/SingHealth'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

  
user, password, host, database = 'root', 'root', 'localhost', 'SingHealth'
engine = create_engine(
    url=f'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8')
  
connection = engine.connect()



db = SQLAlchemy(app)
metadata_obj = db.MetaData()

CORS(app)

import projects
import postingHistory
import presentations
import publications
import remediationHistory


### CREATE NEW TABLE, NOT YET OFFICIAL FUNCTION
@app.route("/createtable",methods=['POST'])
def create_table():
    # CREATE THE SQL TABLE #
    data = request.get_json()
    table=data['TableName']
    columns=data['Columns']

    createdTable = db.Table(
    table,                                        
    metadata_obj,
    db.Column(columns[0], db.String(50))                    
    )
    metadata_obj.create_all(engine)
    for i in range(1,len(columns)):
        query = f'ALTER TABLE {table} ADD {columns[i]} VARCHAR(50) ;'
        connection.execute(query)
    
    # CREATE THE PY FILE WITH THE FLASK DATABASE OBJECT #
    fname = table + ".py"
    pagedata = '''
from flask import request, jsonify
from __main__ import app,db
from sqlalchemy import create_engine



class '''+table+'''(db.Model):
    __tablename__ = "'''+table+'''"
    '''+columns[0]+'''=db.Column(db.String(100),primary_key=True)\n'''
    
    for i in range(1,len(columns)):
        pagedata += '''    '''+columns[i]+'''=db.Column(db.String(100))\n'''
    pagedata+='''\n
    __mapper_args__ = {
    'polymorphic_identity': "'''+table+'''"
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

    @app.route("/'''+table+'''")
    def read_'''+table+'''():
        pdList = '''+table+'''.query.all()
        print (pdList,'oierjngosenrboaeir!!!!!!!!!!!!!!!!!!!!!!OSJNWOJN')
        return jsonify(
            {
                "data": [pd.to_dict()
                        for pd in pdList]
            }
        ), 200
    '''
    with open(fname, 'w') as f:
        f.write(pagedata)
    for line in fileinput.FileInput('app.py', inplace=True):
        
        if line.startswith('import projects'):
            line += 'import ' +table+ os.linesep
            
        print(line, end="")
    return data


db.create_all()


if __name__ == '__main__':
    app.run(port=5010, debug=True)

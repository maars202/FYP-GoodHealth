

from app import app,db
# from __main__ import app,db
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy

class Didactic_Attendance(db.Model):
    __tablename__ = 'Didactic_Attendance'
    Employee_id = db.Column(db.String(100), primary_key=True)
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

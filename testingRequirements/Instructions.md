Dependencies:
Flask
Flask SQLAlchemy
Flask CORS
pandas
WAMP (Windows) / Mamp (Mac)
Steps to set up:
Windows

Username: root
Password is empty
Mac

Username: root
Password: root
Turn on WAMP/MAMP
Load ljms.sql file into phpMyAdmin


Setting up the environment

Please install the packages by running:
```npm install```
```python3 -m venv env```
```source env/bin/activate```
```pip install -r requirements.txt```


Run backend/app.py under flask folder with commands: 
```python backend/app.py```

http://127.0.0.1:5010/:
similar to image img/homepage.png


http://127.0.0.1:5010/didactic_attendance: 
similar to image img/didactic_attendance_result.png

{
  "data": [
    {
      "BillingName": "SGHGasEnt",
      "Compliance_or_Not": "",
      "Didactic_Attendance_deleted": false,
      "Employee_id": "MOM12390",
      "MmYyyy": "",
      "Month": "July",
      "Number_of_sessions_attended": "14",
      "Percentage_of_sessions_attended": "100%",
      "Posting_Department": "",
      "Posting_Institution": "",
      "Scheduled_Teachings": "",
      "Total_tracked_sessions": "14"
    },....
    ]}


THE END
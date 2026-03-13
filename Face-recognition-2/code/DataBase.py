import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("code/service1.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://face-recognition2-de7c9-default-rtdb.firebaseio.com/'

})

ref = db.reference("Students")  # directory creation

data = {
    "11051": {
        "name": "Nicola Tesla",
        "major": "Electronics",
        "starting_year": 1918,
        "total_attendance ": 0,
        "standing": "A",
        "year": 4,
        "last_attendance_time": "2024-06-01 10:00:00"
    },
    "11052": {
        "name": "Albert Einstein",
        "major": "Physics",
        "starting_year": 1916,
        "total_attendance ": 0,
        "standing": "B",
        "year": 4,
        "last_attendance_time": "2024-06-01 10:00:00"
    },
    "11053": {
        "name": "Oppenheimer",
        "major": "Physics",
        "starting_year": 1920,
        "total_attendance ": 0,
        "standing": "C",
        "year": 4,
        "last_attendance_time": "2024-06-01 10:00:00"
    },
    "25026": {
        "name": "Garvit Saxena",
        "major": "CSE",
        "starting_year": 2024,
        "total_attendance ": 0,
        "standing": "A+",
        "year": 2,
        "last_attendance_time": "2024-06-01 10:00:00"
    },
    "25067": {
        "name": "Vaibhav",
        "major": "CSE",
        "starting_year": 2024,
        "total_attendance ": 0,
        "standing": "A",
        "year": 2,
        "last_attendance_time": "2024-06-01 10:00:00"
    },
    "25061": {
        "name": "Shivin Agrawal",
        "major": "LeetCode",
        "starting_year": 2024,
        "total_attendance ": 0,
        "standing": "A",
        "year": 2,
        "last_attendance_time": "2024-06-01 10:00:00"
    },
    "25017": {
        "name": "Arjun Rawat",
        "major": "CSE",
        "starting_year": 2024,
        "total_attendance ": 0,
        "standing": "A+",
        "year": 2,
        "last_attendance_time": "2024-06-01 10:00:00"
    }
}

# Sending my data to firebase

for key, value in data.items():
    ref.child(key).set(value)
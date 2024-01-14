import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : "https://faceattendancerealtime-7f62a-default-rtdb.firebaseio.com/"
})

ref = db.reference("Students")

data = {
    "1": 
    {
        "name" : "Vedanta Hazra",
        "major": "Mathematics and Computing",
        "total_attendance" : 6,
        "last_attendance_time" : "2024-01-01 00:54:34",
        "starting_year" : 2022,
        "year" : 2
    },
    "2": 
    {
        "name" : "Elon Musk",
        "major": "Aerospace",
        "total_attendance" : 4,
        "last_attendance_time" : "2024-01-01 00:54:34",
        "starting_year" : 2022,
        "year" : 2
    },
    "3": 
    {
        "name" : "Jeff Bezoz",
        "major": "Humanities",
        "total_attendance" : 8,
        "last_attendance_time" : "2024-01-01 00:54:34",
        "starting_year" : 2022,
        "year" : 2
    },
    "4": 
    {
        "name" : "Ambani",
        "major": "Business",
        "total_attendance" : 4,
        "last_attendance_time" : "2024-01-01 00:54:34",
        "starting_year" : 2022,
        "year" : 2
    }

}

for key,value in data.items():
    ref.child(key).set(value)
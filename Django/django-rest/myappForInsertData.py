import json
import requests

URL = "http://127.0.0.1:8000/Addstudent/"

#    data in python
data = {
    'RollNo' : 64,
    'Name'   : "sumit",
    'City'   : "Ranchi",
}

# converting python data into json data

json_data = json.dumps(data)

# send to URL
r = requests.post(url=URL,data=json_data)
data = r.json()
print("data :  ",data)  
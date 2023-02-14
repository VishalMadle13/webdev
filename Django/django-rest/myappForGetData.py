
import requests

url = "http://127.0.0.1:8000/studentData/1"

res = requests.get(url=url)
data = res.json()
print(data)
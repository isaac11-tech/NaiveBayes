import json

import requests

data_file = "../data.csv"  #input("enter data path ")
target_column ="buy_computer" #input("enter target_column")
data_point =  '{"age_group": "30+", "status": "student"}'#input("enter data point as JSON like: {age_group: 30+, status: student}")

try:
    data_point = json.loads(data_point)
except json.JSONDecodeError:
    print("Incorrect json structure")
    exit()


payload = {
    "data_file": data_file,
    "target_column": target_column,
    "data_point": data_point
}


try:
    response = requests.post("http://127.0.0.1:8000/loadData", json=payload)
    print("== Server response ==")
    print(f"status: {response.status_code}")
    print(response.json())

    response = requests.get("http://127.0.0.1:8000/result")
    print(response.json())
except requests.exceptions.ConnectionError:
    print("Unable to connect to the server. Make sure your server is running at http://127.0.0.1:8000")
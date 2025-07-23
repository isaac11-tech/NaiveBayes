import json


data_point = '{"age_group": "30+", "status": "student"}'  # input("enter data point as JSON like: {age_group: 30+, status: student}")
try:
    data_point = json.loads(data_point)
except json.JSONDecodeError:
    print("Incorrect json structure")
    exit()
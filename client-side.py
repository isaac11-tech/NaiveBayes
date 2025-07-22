import json
import requests

from collections import defaultdict
import numpy as np

from classifier import NaiveBayesPredictor

data_file = "C:/Users/itzch/NaiveBayes/data.csv"  # input("enter data path ")
target_column = "buy_computer"  # input("enter target_column")
data_point = '{"age_group": "30+", "status": "student"}'  # input("enter data point as JSON like: {age_group: 30+, status: student}")
try:
    data_point = json.loads(data_point)
except json.JSONDecodeError:
    print("Incorrect json structure")
    exit()

payload = {
    "data_file": data_file,
    "target_column": target_column,
}

# loding data and bild the model
try:
    response = requests.post("http://127.0.0.1:8000/loadData", json=payload)
    print("== Server response ==")
    print(f"status: {response.status_code}")
    print(response.text)

    response = requests.get("http://127.0.0.1:8000/getModel")
    model_data = response.json()
    print(response.text)
except requests.exceptions.ConnectionError:
    print("Unable to connect to the server. Make sure your server is running at http://127.0.0.1:8000")


# return the classifier
def unpack_model_data(data: dict):
    class_counts = defaultdict(int, data["class_counts"])

    feature_counts = defaultdict(lambda: defaultdict(int), {
        k: defaultdict(int, v) for k, v in data["feature_counts"].items()
    })

    feature_values = defaultdict(set, {
        k: set(v) for k, v in data["feature_values"].items()
    })

    labels = np.array(data["labels"])

    return class_counts, feature_counts, feature_values, labels


class_counts, feature_counts, feature_values, labels = unpack_model_data(model_data)

predictor = NaiveBayesPredictor(class_counts, feature_counts, feature_values, labels)

prediction = predictor.predict(data_point)
print(prediction)

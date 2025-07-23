# classifier_management.py
import json
import requests
from collections import defaultdict
import numpy as np
from classifier import NaiveBayesPredictor

data_point = {"age_group": "30+", "status": "student"}


def load_create_data(data_path="model_server/data/data.csv", target_column="buy_computer"):
    payload = {
        "data_file": data_path,
        "target_column": target_column,
    }

    try:
        # load data
        response = requests.post("http://127.0.0.1:8000/loadData", json=payload)
        print("== Server response ==")
        print(f"status: {response.status_code}")
        print(response.text)

        # get trained model
        response = requests.get("http://127.0.0.1:8000/getModel")
        model_data = response.json()
        print(response.text)
    except requests.exceptions.ConnectionError:
        print("Unable to connect to the model server.")
        return None

    return model_data


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


def get_prediction():
    model_data = load_create_data()
    if not model_data:
        return {"error": "Failed to load model"}

    class_counts, feature_counts, feature_values, labels = unpack_model_data(model_data)
    predictor = NaiveBayesPredictor(class_counts, feature_counts, feature_values, labels)
    prediction = predictor.predict(data_point)
    return {"prediction": prediction}

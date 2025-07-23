# server.py
from fastapi import FastAPI
from classifier_management import get_prediction

app = FastAPI()

@app.get("/get_classifier")
def get_classifier():
    result = get_prediction()
    return result



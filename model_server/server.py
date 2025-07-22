from fastapi import FastAPI
from model_server.DataLoader import DataLoader
from model_server.data_cleaning import DataCleaning
from  model_server.models import LoadData
from model_server.naive_Bayes_Trainer import NaiveBayesTrainer

app = FastAPI()

trained = None

@app.post("/loadData")
def load_data(data: LoadData):
    global trained
    data_path = data.data_file
    target_column = data.target_column
    #loading data
    df = DataLoader.load_file(data_path)
    #cleanung data
    df = DataCleaning.cleaning(df)
    #trainer data
    trained = NaiveBayesTrainer().fit(df,target_column)

    return {
        "message": "Data initialized successfully",
        "data_file": str(data_path),
        "target_column": target_column,
    }


@app.get("/getModel")
def get_model():
    return trained




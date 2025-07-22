from fastapi import FastAPI,HTTPException
from model_server.data_cleaning import DataCleaning
from model_server.DataLoader import DataLoader
from model_server.naive_Bayes_Trainer import NaiveBayesTrainer
from classifier import NaiveBayesPredictor
from model_server.models import *

app = FastAPI()

#object that save the path and the target to the data
data_manager = DataManager()

@app.post("/loadData")
def load_data(data: LoadData):
    file_path = Path(data.data_file)
    if not file_path.exists():
        raise HTTPException(status_code=400, detail="File path does not exist")
    data_manager.data_file = file_path
    data_manager.target_column = data.target_column
    data_manager.data_point = data.data_point
    return {
        "message": "Data initialized successfully",
        "data_file": str(file_path),
        "target_column": data.target_column,
    }


def calculating_probability(data_file,target_column,data_point):
    df = DataLoader.load_file(data_file)
    DataCleaning.cleaning(df)
    trainer = NaiveBayesTrainer()
    practiced = trainer.fit(df, target_column)
    predictor = NaiveBayesPredictor(practiced.class_counts, practiced.feature_counts, practiced.feature_values,
                                    practiced.labels)
    prediction = predictor.predict(data_point)
    return prediction

@app.get("/result")
def result():
    return calculating_probability( data_manager.data_file,data_manager.target_column, data_manager.data_point)




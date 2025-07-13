from data_cleaning import DataCleaning
from DataLoader import DataLoader
from naive_Bayes_Trainer import NaiveBayesTrainer
from naive_bayes_predictor import NaiveBayesPredictor


print("enter data path")
data_file = input()
print("enter target_column")
target_column = input()
df = DataLoader.load_file(data_file)
DataCleaning.cleaning(df)
trainer = NaiveBayesTrainer()
practiced = trainer.fit(df,target_column)
predictor = NaiveBayesPredictor(practiced.class_counts,practiced.feature_counts,practiced.feature_values,practiced.labels)
prediction = predictor.predict({"age_group": "30+", "status": "student"})
print(prediction)

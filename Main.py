import pandas as pd
from Naive_Bayes_Trainer import NaiveBayesTrainer

df = pd.DataFrame([
    {"age_group": "30+", "status": "student", "buy_computer": "yes"},
    {"age_group": "20-", "status": "worker", "buy_computer": "no"},
    {"age_group": "30+", "status": "worker", "buy_computer": "yes"},
    {"age_group": "20-", "status": "student", "buy_computer": "no"},
    {"age_group": "30+", "status": "student", "buy_computer": "yes"},
])

trainer = NaiveBayesTrainer()
predictor = trainer.fit(df, target_column="buy_computer")

prediction = predictor.predict({"age_group": "30+", "status": "student"})
print(prediction)

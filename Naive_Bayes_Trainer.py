import pandas as pd
from collections import defaultdict
from naive_bayes_predictor import NaiveBayesPredictor

class NaiveBayesTrainer:

    def __init__(self):
        self.class_counts = {}
        self.feature_counts = {}
        self.feature_values = defaultdict(set)
        self.total_count = 0
        self.labels = set()
        self.target_column = None

    def fit(self, df: pd.DataFrame, target_column: str):
        self.target_column = target_column
        self.total_count = len(df)
        self.labels = df[target_column].unique()

        #  P(class)
        class_counts_series = df[target_column].value_counts(normalize=True)
        self.class_counts = class_counts_series.to_dict()

        #  P(value | class)
        self.feature_counts = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

        for feature in df.columns:
            if feature == target_column:
                continue

            self.feature_values[feature] = set(df[feature].unique())
            grouped = df.groupby([feature, target_column]).size()

            for (value, label), count in grouped.items():
                self.feature_counts[feature][value][label] = count

        # החזרת מופע של NaiveBayesPredictor
        return NaiveBayesPredictor(
            class_counts=self.class_counts,
            feature_counts=self.feature_counts,
            feature_values=self.feature_values,
            labels=self.labels
        )

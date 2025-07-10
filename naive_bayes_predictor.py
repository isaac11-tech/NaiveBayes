class NaiveBayesPredictor:
    def __init__(self, class_counts, feature_counts, feature_values, labels):
        self.class_counts = class_counts
        self.feature_counts = feature_counts
        self.feature_values = feature_values
        self.labels = labels

    def predict(self, data_point: dict) -> dict:
        probs = {}

        for label in self.labels:
            prob = self.class_counts.get(label, 1e-6)

            for feature, value in data_point.items():
                value_count = self.feature_counts[feature][value].get(label, 0)
                total_for_class = sum(self.feature_counts[feature][v].get(label, 0)
                                      for v in self.feature_values[feature])
                num_unique_values = len(self.feature_values[feature])

                # Laplace smoothing
                smoothed_prob = (value_count + 1) / (total_for_class + num_unique_values)
                prob *= smoothed_prob

            probs[label] = prob


        total = sum(probs.values())
        if total > 0:
            for label in probs:
                probs[label] /= total

        return probs

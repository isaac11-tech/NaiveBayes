# NaiveBayes
# Naive Bayes Classifier Project

## 📚 Project Overview

This project implements a **Naïve Bayes classifier** from scratch, following Object-Oriented Programming principles. The classifier is designed to perform supervised classification tasks on datasets in CSV format, using **Laplacian smoothing** to handle zero probabilities.  

The program builds a statistical model from training data, then allows the user to classify new data points or evaluate model accuracy on a labeled dataset.

---

## 🎯 Objectives

- Understand and apply the **Naïve Bayes algorithm** with Laplace correction.
- Practice **Object-Oriented Design** for structuring ML workflows.
- Read, process, and classify data from external CSV files.
- Evaluate the classifier's accuracy using a labeled test set.

---

## 🛠 Features

- Loads dataset from a CSV file.
- Splits dataset into training (70%) and testing (30%) parts.
- Builds conditional probability tables for each feature.
- Supports classification of:
  - A dataset with missing labels (accuracy evaluation).
  - A single input record (manual test).
- Outputs accuracy statistics based on test results.

---

## 🧱 Code Structure

The project is modular and consists of several classes:

- **DataLoader**  
  Handles loading and parsing of CSV files.

- **NaiveBayesTrainer**  
  Builds the statistical model based on training data.

- **NaiveBayesPredictor**  
  Uses the model to classify new samples.

- **DataCleaning**  
  Handles missing values by filling numerical columns with mean and categorical ones with mode.

- **Main**  
  Initializes components and provides the main interface.

---

## 📊 Example Datasets

You can experiment with open datasets such as:

- [UCI Mushroom Dataset](https://archive.ics.uci.edu/ml/datasets/mushroom)
- [Phishing Websites Dataset (Kaggle)](https://www.kaggle.com/eswarchandt/phishing-website-detector?select=phishing.csv)

---

## 🔧 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/isaac11-tech/NaiveBayes.git
   cd NaiveBayes

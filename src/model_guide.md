# Predicting heart disease using the Machine Learning

This Notebook looks into using the  various Python-based Machine Learning and Data science libreries in an attempt to build a mchine leaning model capable of redicting whether the patient has the heart disease or not based on their medical attributes

We're going to take the following approach :
1. [Problem Defination](#1.-Problem-Defination)
2. [Data Gathering](#2.-Data)
3. [Evaluation](#3.-Evaluation)
4. [Modelling](#4.-Features)
5. Experimenting

## 1. Problem Defination
In a statement,
> Given clinical parameters about a patient can we predict whether the patient have the heart disease or not.

## 2. Data
The original came from the cleavland data from the [UCI Machine Repository](https://archive.ics.uci.edu/dataset/45/heart+disease).

**Note** These version is also available on the [Kaggle Heart Disease Dataset](https://www.kaggle.com/datasets/redwankarimsony/heart-disease-data)

## 3. Evaluation
> if we can reach above or equal 85% accuracy at predicting whether or not a patient has heart disease during the proof of concept, we will pursue the project as it is critical project.

## 4. Features

* age (Age of the patient in years)
* sex (Male/Female)
* cp chest pain type ([typical angina, atypical angina, non-anginal, asymptomatic])
* trestbps resting blood pressure (resting blood pressure (in mm Hg on admission to the hospital))
* chol (serum cholesterol in mg/dl)
* fbs (if fasting blood sugar > 120 mg/dl)
* restecg (resting electrocardiographic results) -- Values: [normal, stt abnormality, lv hypertrophy]
* thalach: maximum heart rate achieved
* exang: exercise-induced angina (True/ False)
* oldpeak: ST depression induced by exercise relative to rest
* slope: the slope of the peak exercise ST segment
* ca: number of major vessels (0-3) colored by fluoroscopy
* thal: [normal; fixed defect; reversible defect]
* target (1 for `having heart disease` 0 for `not having heart disease`)
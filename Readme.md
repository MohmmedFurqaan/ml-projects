# Heart Disease Prediction

## Table of content

1. [Installation Guide](#Installation)
2. [About The Project](#About)
3. [Data Insights](#Data-Insights)
   * [3.1 Heart disease class distribution](#3.1-Heart-disease-total-classes)
   * [3.2 Heart Disease Gender based frequence](#3.2-Heart-Disease-Gender-based-frequence)
   * [3.3 Heart disease age distribution](#3.3-Age-Distribution)
   * [3.4 Max Heart Rate v/s Age](#3.4-Maximum-heart-beat-Rate-V/S-Age)
   * [3.5 Chest Pain Type heart Disease Analysis](#3.5-Chest-Pain-Type-heart-Disease-Analysis)
4. [Modelling](#4.-Modelling)
## Installation

1. clone the repository in your local directory of your machine 

```code
git clone https://github.com/MohmmedFurqaan/ml-projects.git
```

2. Let's setup the envinoment

In the project root directory, You will find the `envirnoment.yml` file. These file contains the envirnoment dependencies you can setup the envirnoment by the following :

```code 
conda env create -f environment.yml
```

Then 

```code
conda activate my_ml_env
```

## About 

This project is a **machine learning practice project** focused on building an end-to-end classification workflow for predicting the presence of heart disease from patient-related features.

The project is built primarily to strengthen my understanding and practical implementation of the **complete machine learning workflow**, including data preprocessing, exploratory data analysis, model training, evaluation, and hyperparameter tuning.

The dataset and problem are based on an existing heart disease prediction task. **I did not create the underlying medical dataset or invent the problem; this project is my own implementation and practice exercise using an existing dataset.**

## Data Insights

Exploratory Data Analysis is the important part of the machine learning. As just training and evaluating the Machine learning is not just a way to get the best Model. 

The ML Engineer must also have the knowledge about the data below are some of the insights i caught from the data to find the pattern's bettween the data

#### 3.1 Heart disease total classes 
> **Purpose** based on the below graph we can identify the class imbalancing in the data set that we have.
![Class weight Graph](images/eda/001_class_weight_graph.png))


#### 3.2 Heart Disease Gender based frequence
> **Purpose** Based on the below graph we can identify the ratio of the male and female of having the heart disease.
![Gender Based frequency](images/eda/002_gender_based_heart_disease_analysis.png)

### 3.3 Age Distribution
> **Purpose** The purpose of the graph is to find how the data is distributed and to find out is it there any outlier's
![Age Distribution](images/eda/003_age_distribution.png)

### 3.4 Maximum heart beat Rate V/S Age
> **Purpose** Based on the below graph we can observe the pattern at what parameter based on the age and Max Heart patient are postive heart disease patient.
![Postitive Patient](images/eda/004_thelach_age_heart_patient.png)

> **Purpose** Based on the below graph we can observe the pattern at what parameter based on the age and Max Heart patient are not heart disease patient.
![Negative Patient](images/eda/005_thelach_age_not_heart_patient.png)


### 3.5 Chest Pain Type heart Disease Analysis
> **Purpose** The Purpose of the graph is to find which of the chest pain type have the most affected patient and which are the negative patient based on our current dataset.
![Chest pain heart patient analysis](images/eda/006_heart_disease_chest_pain_type.png)


### 3.6 Correlation between the individual label and the target label
> **Purpose** The purpose of the correlation is to find the relation between the One feature vaiable with the target and other feature's present in the dataset.
![correlation between the data](images/eda/007_heat_map_correlation.png)

**Note for correlation**

`1 (Perfect Positive Correlation)`: As one variable increases, the other variable increases proportionally.

`0 (No Correlation)`: There is no linear or predictable relationship between the variables.

`-1 (Perfect Negative Correlation)`: As one variable increases, the other variable decreases proportionally

## 4. Modelling 

**What Modelling is** 

> Modelling means preapring our model to get deep dive into the model to build the model based on the [Provided Scikit learn estimator](https://scikit-learn.org/stable/machine_learning_map.html) to preare the best model.

### 4.1 KNeighborsClassifier

> After tunning the parameter's of the KNN (for parameter's negihbours), which ranges from 1 to 21 i found that it achived the `max accuracy score to the : 75.41%` which is not satisified see the below graph :
![Hypertunning of KNN Classifier](images/modelling/002_knn_model_tunning.png)

 
### 4.2 RandomForestClassifier 
> After tunning the parmaeter's for the RandomForest i got the score accracy `86.68%` then the baseline model of the RandomForeset which was `83.60%`

![Randomforest Model](images/modelling/003_random_forest_score.png)

### 4.3 LogisticRegression
> After tunning the LogisticregRessor model the model reaced the `max accuracy 88.52%` which is max among all of them.

I choose the [Logistic Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) estimator for the [Heart Disease Predictor](https://github.com/MohmmedFurqaan/ml-projects.git) based on the below graph as the [Logistic Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) achieved the acuracy around 88% for the baseline model you can see it below : 
![Sklearn Model Comparision](images/modelling/001_different_modell_score.png)

## Important Disclaimer

This project is developed **for educational and machine learning practice purposes only**. It is **not a medical diagnostic tool** and should not be used to make real-world medical decisions. The model has not been clinically validated and should not replace professional medical advice.

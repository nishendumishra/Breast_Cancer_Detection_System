# Breast_Cancer_Detection_System

## Problem Statement
Breast cancer is a critical global health concern affecting millions of individuals each year. Early and accurate detection of breast cancer plays a pivotal role in improving patient outcomes and reducing mortality rates. Traditional methods of breast cancer detection, such as mammography, can be time-consuming and may have limitations in sensitivity and specificity. Leveraging the power of machine learning techniques, this project aims to develop a robust and efficient breast cancer detection model that can assist healthcare professionals in identifying potential malignancies from data collected from medical images.

## Objective:
Design and implement a machine learning model capable of accurately classifying breast tissue as benign or malignant based on digital mammogram or biopsy images.

## Dataset Used
The dataset used is breast_cancer dataset which is inbuilt in sklearn.datasets library and other links from it can be downloaded is [Kaggle Website](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data?select=data.csv) and also on [UCI Machine Learning Repo](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29).

Details about Dataset:

* Attribute Information:

1) ID number
2) Diagnosis (M = malignant, B = benign)
3-32)

* Ten real-valued features are computed for each cell nucleus:

a) radius (mean of distances from center to points on the perimeter)
b) texture (standard deviation of gray-scale values)
c) perimeter
d) area
e) smoothness (local variation in radius lengths)
f) compactness (perimeter^2 / area - 1.0)
g) concavity (severity of concave portions of the contour)
h) concave points (number of concave portions of the contour)
i) symmetry
j) fractal dimension ("coastline approximation" - 1)

* The mean, standard error and "worst" or largest (mean of the three
largest values) of these features were computed for each image,
resulting in 30 features. For instance, field 3 is Mean Radius, field
13 is Radius SE, field 23 is Worst Radius.

* All feature values are recoded with four significant digits.

* Missing attribute values: none

* Class distribution: 357 benign, 212 malignant


## Work Flow

Step-1: First the data is imported from the sklearn.datasets library, and create a dataframe from the dataset. Some preprocessing and data analysis is done. \
Step-2: This dataset is divided into two dataset x and y , x containing the features values and y containing the target.\
Step-3: Since the x data is imbalanced, therefore StandardScaler is used, to standardize the data.\
Step-3: This data is now splited using train_test_split() in training and testing data. Using the training data the Logistic Regression model is fitted.\
Step-4: Finding the accuracy of the model on training data and testing data both in order to check for Overfit or Underfit.\
Step-5: Building a Predictive System.

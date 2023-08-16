# -*- coding: utf-8 -*-
"""Breast_Cancer_Classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19iSQ8T5xB-TN95hvGkhPytZiZsYwLlBz

Name: Nishendu Mishra

Topic: Breast Cancer Detection System

Email: nishendumishra73@gmail.com
"""

import numpy as np
import pandas as pd
import sklearn.datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

"""#Data Collection and processing"""

#loading the data from sklearn

bcd = sklearn.datasets.load_breast_cancer()

print(bcd)

#loading a data to apandas dataframe

bcdf = pd.DataFrame(bcd.data, columns = bcd.feature_names)

#print the first five rows
bcdf.head()

#adding the target column to the data frame

bcdf['Diagnosis'] = bcd.target

bcdf.tail()

#number of rows and columns in the dataset
bcdf.shape

bcdf.isnull().sum()

"""there is no blank values"""

bcdf.info()

# statistical measures about the data
bcdf.describe()

bcdf['Diagnosis'].value_counts()

"""1 --> Benign

0 --> Malignant
"""

bcdf.groupby('Diagnosis').mean()

"""all the values in Malignant(0) case is greater than Benign(1)"""

x = bcdf.drop(columns = 'Diagnosis', axis=1)
y = bcdf['Diagnosis']

print(x)
print(y)

bcd.data.std()

scaler = StandardScaler()

xt = scaler.fit_transform(x)

print(xt)

"""#Training and Testing

Splitting the data into data & training
"""

xt_train, xt_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state= 2)

print(xt.shape, xt_train.shape, xt_test.shape)

"""Model Training

Logistic Regression
"""

model =  LogisticRegression()

#training the Logistic Regression model

model.fit(xt_train, y_train)

"""#Model Evaluation

Accuracy Score
"""

# accuracy of the training data
x_train_prediction = model.predict(xt_train);
training_data_accuracy = accuracy_score(y_train, x_train_prediction)

print('Accuracy of the Training data: ', training_data_accuracy)

#accuracy of the testing data
x_test_prediction = model.predict(xt_test);
testing_data_accuracy = accuracy_score(y_test, x_test_prediction)

print('Accuracy of the Testing data: ', testing_data_accuracy)

"""#Build a predictive System"""

input_data =(13.53,10.94,87.91,559.2,0.1291,0.1047,0.06877,0.06556,0.2403,0.06641,0.4101,1.014,2.652,32.65,0.0134,0.02839,0.01162,0.008239,0.02572,0.006164,14.08,12.49,91.36,605.5,0.1451,0.1379,0.08539,0.07407,0.271,0.07191)

#change the input data to a numpy array
input_as_numpy_array = np.asarray(input_data)

#reshape the numpy array as we are predicting for one data point
input_reshaped = input_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_reshaped)

print(prediction)

if(prediction[0] == 0):
  print('The Breast Cancer is Malignant')
else:
  print('The Breast Cancer is Benign')
# -*- coding: utf-8 -*-
"""kfold-breast-cancer-dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oxys1sQ6LmddaXDoJ-W4H6NLKlKWOsKY
"""

import pandas as pd
data = pd.read_csv("wdbc.data" , header = None)

y = data[1]
x = data.drop(columns=[1])

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x = sc.fit_transform(x)
encoder = LabelEncoder()
y = encoder.fit_transform(y)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x ,y , test_size = 0.3, random_state = 0)

from sklearn.model_selection import cross_val_score
import keras
from keras.layers import Dense
from keras.models import Sequential
from keras.wrappers.scikit_learn import KerasClassifier

def built_Classifier():
    classifier = Sequential()
    classifier.add(Dense(16, activation='relu', input_dim=31))
    classifier.add(Dense(16, activation='relu'))
    classifier.add(Dense(1, activation='sigmoid'))
    classifier.compile(optimizer='Adam', loss='binary_crossentropy', metrics=['accuracy'])
    return classifier

model = KerasClassifier(build_fn = built_Classifier, batch_size = 100, epochs = 100)
accurices = cross_val_score(estimator= model, X=x_train, y=y_train, cv = 10, n_jobs = -1)

accurices.std()


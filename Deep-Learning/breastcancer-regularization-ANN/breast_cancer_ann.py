# -*- coding: utf-8 -*-
"""breast-cancer-ANN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g2jTFCx5uv8Jl_qqjzWJLJPdVd-AJJ1h
"""

#preprocessing data
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

data = pd.read_csv("wdbc.data", delimiter=",", header=None)

y = data[1]
x = data.drop(columns=[1])

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
y = labelencoder.fit_transform(y)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.7 , random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)

import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout

classifier = Sequential()
#regularization(Dropout Method)
classifier.add(Dense(16, activation='relu', input_dim=31))
classifier.add(Dropout(rate=0.1))

classifier.add(Dense(16, activation='relu'))
classifier.add(Dropout(rate=0.1))

classifier.add(Dense(1, activation='sigmoid'))
classifier.compile(optimizer='Adam', loss='binary_crossentropy', metrics=['accuracy'])

output = classifier.fit(x_train, y_train , batch_size=32, epochs=5)

y_pred = classifier.predict(x_test)
y_pred = (y_pred > 0.5)

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test,y_pred)
accuracy_score(y_test, y_pred)

import matplotlib.pyplot as plt

plt.plot(output.history['accuracy'])


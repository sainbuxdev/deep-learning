# -*- coding: utf-8 -*-
"""Iris-data-DeepLearning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ENvDne8xey8YnodVb-WdFZJWVEivnD7W
"""

import pandas as pd
data = pd.read_csv("iris.data", delimiter=',', header=None)

y = data[4]
x = data.drop(columns=[4])

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
y1 = labelencoder.fit_transform(y)
Y = pd.get_dummies(y1).values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x , Y , test_size = 0.2 , random_state = 0)



import keras
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()

model.add(Dense(8, input_shape = (4,), activation='relu'))
model.add(Dense(8, activation='relu' ))
model.add(Dense(3,  activation='softmax'))
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

output = model.fit(x_train, y_train, batch_size = 5, epochs=30)

y_pred = model.predict(x_test)
#y_pred = (y_pred > 5)

from sklearn.metrics import confusion_matrix, accuracy_score
import numpy as np
y_test_class = np.argmax(y_test, axis=1)
y_pred_class = np.argmax(y_pred, axis=1)
cm = confusion_matrix(y_test_class, y_pred_class)
accuracy_score(y_test_class, y_pred_class)

import matplotlib.pyplot as plt
plt.plot(output.history['accuracy'])
plt.plot(output.history['loss'])
plt.show()


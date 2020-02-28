# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 17:28:37 2019

@author: Dell
"""

import pandas as pd
import joblib

dataframe = pd.read_csv("csv/dataset.csv")
print(dataframe.head())

x = dataframe.drop(["Label"],axis=1)
y = dataframe["Label"]

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier ,AdaBoostClassifier
from sklearn import metrics 

x_train , x_test ,y_train ,y_test = train_test_split(x, y ,test_size=0.2 , random_state=4)

model = RandomForestClassifier(n_estimators = 100 , max_depth=5)
model.fit(x_train,y_train)

joblib.dump(model,"rf_malaria_100_5")

y_pred = model.predict(x_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

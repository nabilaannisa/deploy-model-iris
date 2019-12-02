

#Import library yang dibutuhkan
import numpy as np
import pandas as pd
import pickle
import requests
import json
from sklearn import tree
from sklearn.model_selection import train_test_split

#read the dataset
df = pd.read_csv('IRIS.csv')
#df = df.drop(['Id'], axis=1)

# Splitting the dataset into the Training set and Test set
x = df.iloc[:,:-1]
y = df.iloc[:,-1:]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=1/3)


## Fitting classifier to the Training set
from sklearn import tree
model = tree.DecisionTreeClassifier()
model = model.fit(x_train, y_train)
model.score(x,y)

# Predicting the Test set results
#y_pred = model.predict(x_test)

# Saving model using pickle
pickle.dump(model, open('iris_model.pkl','wb'))

# Loading model to compare the results
#model = pickle.load( open('iris_model.pkl','rb'))
#print(model.predict(np.array([5.4,3.9,1.7,0.3])))

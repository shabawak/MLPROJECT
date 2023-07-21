#use panda to read the data and also understand the data
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import GridSearchCV
import pickle

from sklearn import svm #support vector machine svm.SVC(kernel='linear')



#Load data from csv
data = pd.read_csv("water_potability.csv")

# print the data head
print(data.head())

# DATA PREPROCESSING

#fill all the nulls with the mean of that column
data.fillna(data.mean(),inplace = True) 

# EDA (Exploratory Data Analysis)

# MODEL TRAINING AND EVALUATION
# Partitioning Data into  input variable and output variable

# PARTITIONING
#Input data|Selecting independent and dependent variable
X = data.drop('Potability', axis=1) 

Y = data['Potability'] # Target variable or class {0 =>not portable, 1=> portable}

# splitting the data into training data (X_train, Y_train) and testing data (X_test, Y_test)
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2, shuffle=True, random_state=101)

#print('XTRAIN ',X_test)
#print('YTRAIN ', Y_test)
# NORMALIZING THE DATA | feature scaling
sc=StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# BUILDING THE MODEL

# using the KNN classifier

#instantiating the model
#knn=KNeighborsClassifier(metric='manhattan', n_neighbors=22)
knn_c = KNeighborsClassifier(metric= 'manhattan', n_neighbors= 22, weights= 'uniform')
# Fit the model
knn_c.fit(X_train,Y_train)

# Make pickle file of the model

pickle.dump(knn_c, open("model.pkl","wb"))



""" print('X ',X)
print('Y ', Y)

prediction_knn=knn_c.predict(X_test)
print('prediction\n',prediction_knn)
accuracy_knn=accuracy_score(Y_test,prediction_knn)*100
print('accuracy_score score     : ',accuracy_score(Y_test,prediction_knn)*100,'%')

confusion_matrix(prediction_knn,Y_test)
print(confusion_matrix(prediction_knn,Y_test)) """

#predict one data
#X_KNN=knn.predict([[6.552847474,198.8069397,34006.42073,8.691206175,274.9043512,477.1639068,14.36963009,78.17306259,4.687986155]])

#print('one data\n',X_KNN)
# MODEL OPTIMIZATION / HYPER PARAMETER TUNING







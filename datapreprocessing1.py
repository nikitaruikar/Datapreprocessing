import pandas as pd
import os
#importing dataset
student=pd.read_excel('D:\\cognitior\\Basics of data science\\student.xls')

student.isnull().sum()

#to check for the outerliers in dataset
import seaborn as sns
sns.boxplot(y='age',data=student)

sns.boxplot(y='study_time',data=student)

x=student.iloc[:,2:4].values
x
#for missing value trereatement by using mean
from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values='NaN',strategy='mean',axis=0)
imputer=imputer.fit(x[:,1:2])
x[:,1:6]=imputer.transform(x[:,1:2])
x
#for missing value treatment by using median
from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values='NaN',strategy='median',axis=0)
imputer=imputer.fit(x[:,1:2])
x[:,1:2]=imputer.transform(x[:,1:2])
pd.DataFrame(x)

#for categorical data
from sklearn.impute import SimpleImputer
imp=SimpleImputer(strategy='most_frequent')
x[:,1:2]=imp.fit_transform(x[:,1:2])
x

x=student.iloc[:,0:1].values
x
import pandas as pd
import os
os.chdir('D:\\cognitior\\Basics of data science')
dataset = pd.read_csv('data.csv')
dataset

x=dataset.iloc[:,:-1].values
x

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_x=LabelEncoder()
x[:,0]=labelencoder_x.fit_transform(x[:,0])

onehotencoder=OneHotEncoder(categorical_features=[0])
x=onehotencoder.fit_transform(x).toarray()
pd.DataFrame(x)

from sklearn.preprocessing import Normalizer
nm=Normalizer()
x=nm.fit_transform(x)
pd.DataFrame(x)
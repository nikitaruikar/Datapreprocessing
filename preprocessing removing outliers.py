#importing libraries
import pandas as pdimport os
os.chdir('D:\\cognitior\\Basics of data science')

#Importing the dataset
dataseto = pd.read_excel('OutlierData.xlsx')
dataseto

dataseto=dataseto.iloc[:,1:3]
dataseto
#checking for outliers
import seaborn as sns
sns.boxplot(y='Experience', data=dataseto)

#Removing outliers
Q1 = dataseto.quantile(0.25)
Q3 = dataseto.quantile(0.75)
IQR = Q3-Q1


dataset_out = dataseto[~((dataseto<(Q1-1.5*IQR))
                       | (dataseto>(Q3+1.5*IQR))).any(axis=1)]

dataset_out 

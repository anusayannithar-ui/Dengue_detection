import pandas as pd
from sklearn.model_selection import train_test_split


# dataset extraction

df = pd.read_csv('dengue_dataset.csv',sep=',',header=0)
df.head(n=3)

print(df.isnull().sum())

df['Platelet_Count'] = df['Platelet_Count'].fillna(df['Platelet_Count'].mean())


df['Joint_Pain'] = df['Joint_Pain'].fillna(df['Joint_Pain'].mode()[0])


X = df.drop(columns=['Patient_ID','Dengue_Positive'])

y = df['Dengue_Positive']

#----splitting  X:y = 80:20

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random=42)











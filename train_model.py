import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import joblib
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

df=pd.read_csv('Advertising_dataset.csv')
# print(df.head())   

# Feature
X=df.drop('sales', axis=1)
y=df['sales']

# Spliting 
X_train, X_test,y_train, y_test=train_test_split(X,y,test_size=0.3,random_state=42)
# scaling 
scaler=StandardScaler()
sX_train=scaler.fit_transform(X_train)
sX_test=scaler.transform(X_test)

# Model
model= LinearRegression()
model.fit(sX_train, y_train)

# save model and scaler
joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("Model and scaler save Successfully!")


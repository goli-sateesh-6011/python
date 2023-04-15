import pandas as pd
data=pd.read_csv("C://Users//SATISH_GOLI//Downloads//cars.csv")
#print(data)
print("Information of the data ",data.info())
print(data.columns)
print(data.describe())
print(data.head())

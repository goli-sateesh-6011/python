import pandas as pd
df=pd.read_csv('C:/Users/SATISH_GOLI/Desktop/JAVA/cars.csv')
#print(df)
#Slice the data
print(df.columns)
print(df[0:5])

######"
#print(df.loc[:,['Car']])
print(df.loc[2:6])
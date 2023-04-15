import pandas as pd
import numpy as np

df=pd.DataFrame(np.random.randn(5,3),index=['a','c','e','g','i'],columns=['one','two','Three'])


df=df.reindex(['a','b','c','d','e','f','g','h'])
print(df)

print(df['two'].isnull())
df=df.fillna(0)
print(df)
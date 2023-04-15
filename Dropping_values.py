import pandas as pd
import numpy as np

df=pd.DataFrame(np.random.randn(5,3),index=['a','c','e','g','i'],columns=['one','two','three'])

print(df)
df=df.reindex(['a','b','c','d','e','f','g','h','i'])
print(df)
print(df.dropna())
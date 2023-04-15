import pandas as pd
import numpy as np

data= {'one':[20,30,40,5000],'two':[20,50,60,9000]}
df=pd.DataFrame(data)
print(df)
df=df.replace({5000:50,9000:90})
print(df)
import numpy as np
a = np.array([[1,2],[3,4]])
print(a)

##------------------------------------
b=np.array([1,2,3],dtype = complex)
print(b)

############################
import pandas as pd
data = np.array(['a','b','c','d'])
print(pd.Series(data))

########################"""""""
data1 = {'name':['Tom','Jack','Steve','Ricky'],'Age':['23','25','27','29']}
df=pd.DataFrame(data1,index=['rank1','rank2','rank3','rank4'])
print(df)

###########################################

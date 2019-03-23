import numpy as np  
import pandas as pd  



df1=pd.DataFrame(np.arange(1,13).reshape(3,4),columns=list('abcd'))
df2=pd.DataFrame(np.arange(1,21).reshape(4,5),columns=list('abcde'))

df1.add(df2,fill_value=0)   #两个表相加



frame=pd.DataFrame(np.arange(1,13).reshap(4,3),columns=list('bde'),index=['Shenzhen','Guangzhou','Shanghai','Beijing'])


print(df1.add(df2,fill_value=0))

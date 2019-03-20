import pandas as pd 
import numpy as np  

data=pd.read_csv(r'数据阶段/3.18可视化/311-service-requests.csv')
data.head()
data.info()
data['Incident Zip'].unique()   #看看value 都有哪些

na_values=['NO CLUE','000000','00000','0']####把要变为nan的 value标记出来


data=pd.read_csv(r'数据阶段/3.18可视化/311-service-requests.csv',dtype={'Incident Zip':'str'},na_values=na_values)

data.iloc[:,8].unique()
data['Incident Zip']=data['Incident Zip'].str.slice(0,5) #截取前5位的数

is_zero=data['Incident Zip'].str.startswith('0',na=True)   #定位所有0开头的单位;当为’na'时，也是True

print(is_zero)
is_one=data['Incident Zip'].str.startswith('1',na=True)
is_three=data['Incident Zip'].str.startswith('3',na=True)
data.loc[~(is_zero | is_one | is_three),'Incident Zip']=np.nan





# print(data.iloc[:,8].unique())
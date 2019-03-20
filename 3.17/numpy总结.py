import pandas as pd
import numpy as np

s=pd.Series([1,3,5,np.nan,6,8],index=['a','b','c','d','e','f'])
s.index
s.values
s[2:5]
s.index.name='索引'
######Pandas的Dataframe类型
date=pd.date_range('20180101',periods=6)
df=pd.DataFrame(np.random.randn(6,4))
# df1=pd.DataFrame(np.random.randint(6,4))

####索引
arr=np.arange(32).reshape(8,4)
arr1=arr[1:3,1:3]  ###取定位行和列之间的区域
###花式索引
arr2=arr[[1,3],[1,3]]   ####g根据点的坐标定位
arr3=arr[[1,3]][:,[1,3]]    ####取定位的行和定位的列交叉的点
arr33=arr[[1,2,3]][:,[1,2,3]]


print(arr)
print('****************')
print(arr1)
print('****************')
print(arr2)
print('****************')
print(arr3)
print('****************')
print(arr33)
import numpy as np  
import pandas as pd 
import matplotlib.pyplot as plt  
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False 


data=pd.DataFrame(100*np.abs(np.random.rand(4,4)),index=['one','two','three','four'],columns=['HW','ZTE','ESSS','NOKIA'])

####线状图
data.plot(kind='line',figsize=(10,6),grid=True,ylim=(0,200))
#####柱状图（单个公司）
fig=plt.figure(figsize=(10,10))
ax=fig.subplots(2)
data['ZTE'].plot(kind='bar',ax=ax[0])###竖向柱状图
ax[0].set_xticklabels(labels=data['ZTE'].index,rotation=0)
data['ZTE'].plot(kind='barh',ax=ax[1])####横向柱状图

####柱状图2(所有公司)
fig1=plt.figure(figsize=(10,10))
ax1=fig1.subplots(1,2)
data.plot(kind='bar',ax=ax1[0])
data.T.plot(kind='bar',ax=ax1[1],stacked=True)

plt.show()

#####绘图
comp1 = np.random.normal(0,1,size=20000)
comp2 = np.random.normal(10,2,size=20000)
values = pd.Series(np.concatenate([comp1,comp2]))
values.plot(kind='hist',bins=50,density=True)
values.plot(kind='kde',style='r--')




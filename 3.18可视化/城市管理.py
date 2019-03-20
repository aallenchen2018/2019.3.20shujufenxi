import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False 

data=pd.read_csv('数据阶段/3.18可视化/311-service-requests.csv')
data.head()
data.shape
data.info()
data['Complaint Type'].unique()


plt.figure(figsize=(10,6))
top5_series=data['Complaint Type'].value_counts()[:5]
top5_series.plot(kind='bar',color=('r','b','#FFEC8B','#CD5C5C','#79CDCD'))
labels=['heat','gonggong','jiedao','wenhua','guandao']
plt.xticks(range(len(top5_series.index)),labels,rotation=30,fontsize=12)
plt.title('city complaint.Top5',fontsize=15)
x=range(len(top5_series.index))
y=list(top5_series.values)
for a,b in zip(x,y):

    plt.text(a,b+200,str(b),fontsize=10,horizontalalignment='center')
plt.savefig('../城市抱怨Top5.png',dpi=400)




plt.show()
# print(data['Complaint Type'].unique())

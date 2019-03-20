import matplotlib.pyplot as plt #载入matplotlib.pyplot模块
import pandas as pd
import numpy as np

fig=plt.figure(figsize=(10,15))
ax = fig.subplots(3,2)
x=np.random.normal(2,2,10000)
print(x)
ax[0][0].hist(x,bins=30,density=True,color='r',alpha=0.5)#直方图
y=np.random.normal(0,1,10000)
ax[0][0].hist(y,bins=30,density=True,color='b',alpha=0.5)#直方图

x1 = np.arange(1,21)
y1 = np.random.randint(1,10,20)
ax[0][1].scatter(x1,y1,marker='v',color='g',alpha=0.8)#散点图

x2 = np.arange(0,4,0.01)
y2 = np.cos(2*np.pi*x2)
ax[1][0].plot(x2,y2,color='g',linestyle='--',linewidth=2)

y3=[30,20,50,70]
ax[1][1].bar(['ZTE','NOKIA','ESSSSS','HUAWEI'],y3,color=['b','r'])#柱状图

y4 = [28,25,20,14,13]
label = ['HUAWEI','OPPO','VIVO','XIAOMI','OTHER']
explode=[0.05,0,0,0,0]
patches, texts, autotexts=ax[2][1].pie(y4,labels=label,autopct='%.2f%%',explode=explode,radius=2)
for tt in texts:
    tt.set_size(30)
for tt in autotexts:
    tt.set_size(20)

plt.savefig('./sin3.png',dpi=300)
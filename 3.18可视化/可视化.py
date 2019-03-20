import pandas as pd 
import numpy as np   
import matplotlib.pyplot  as plt  

####linux 环境：sudo apt-get install python3-tk

# plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


x=np.arange(0,4.01,0.01)
y=np.sin(2*np.pi*x)
plt.figure(figsize=(9,6))
plt.plot(x,y,linestyle=':',linewidth=3,color='r')
plt.xlim(0,4)
plt.ylim(-1,1)
plt.grid()
plt.xlabel('时间',fontsize=12)
plt.ylabel('电压',fontsize=12) 
plt.title('电压趋势图',fontsize=15)
plt.text(0.5,0.75,'插入文本',fontsize=20)
plt.savefig('sin1.png',dpi=300)

import pandas as pd 
import numpy as np  

data = {'id':[1001,1002,1003,1004,1005,1006], 
        'date':pd.date_range('20130102', periods=6),
        'city':['Beijing ', np.nan, ' guangzhou ', 'Shenzhen', ' SH  ', 'BEIJING '],
        'age':[23,44,54,32,34,32],
        'category':['100-A','100-B','110-A','110-C','210-A','130-F'],
        'price':[1200,np.nan,2133,5433,np.nan,4432]}


df=pd.DataFrame(data,columns=['id','date','city','category','age','price'],index=['one','two','three','four','five','sixx'])

df.iloc[0]=np.nan
# df.dropna(axis=1)# 当本列存在nan时，删除当列
df.dropna(how='all',axis=1) 
###填充
df.fillna({'price':14000,'city':'Chaozhou'})##不会保存
df.fillna(method='ffill',limit=1)  #向前填充
df.fillna(method='bfill')    #向后填充
#替代
df['price'].replace(np.nan,100000) #不会保存
df['city'].str.strip().replace('SH','shanghai')

#############字符串的处理############
#处理列表或者series,对他们里面的元素处理
s=pd.Series(['A','B','c','Aaba', 'Baca cca', np.nan, 'CABA', 'dog', 'cat'])
s.str.upper()
s.str.lower()
s.str.title() #第一个字母大写

idx = pd.Series(['\r\n\tjack'+'\n', '\rjill ', ' jesse ', 'fra nk'])
idx.str.strip()#去除两边空格

s2 = pd.Series(['acccc_b_c', 'c_d_a_e', np.nan, 'f_g_h','a'])
ss=s2.str.split('_')#拆分
ss.str.join('')#合并

s2.str.replace('_','') #替换

s2.str.contains('a',na=False) #判断是否包含某段字符串
s2.str.startswith('a',na=False)  #判断是否以‘a'开头
s2.str.slice(1,3)  #提取部分信息


######重命名索引  
data=pd.DataFrame(np.arange(12).reshape(3,4),index=['Shenzhen','Shanghai','Beijing'],columns=['one','two','three','four'])
data.index=data.index.str.upper() #索引大写
data.columns=list('abcd')

######离散化

########pandas.cut 等距离划分
arr=np.random.randn(10000)
pd.cut(arr,bins=11).value_counts()
##指定距离划分
arr = np.random.randint(20,60,10)
bins=[19,30,40,50,60]
pd.cut(arr,bins=bins).value_counts()#指定划分区域



#######pandas.qcut  等频（数量）划分
arr = np.random.randn(10000)
pd.qcut(arr,q=5).value_counts()
pd.qcut(arr,q=[0,0.2,0.5,1]).value_counts()#按分位数，指定划分占比



######重复项
data=pd.DataFrame({'k1':['one']*3+['two']*4,
                   'k2':[1,1,2,3,3,4,4],'k3':[1,2,3,4,5,6,7]})
data[['k1','k2']].duplicated()

##删除重复项
df=data['k1','k2']
df.drop_duplicates()


print(df.drop_duplicates())





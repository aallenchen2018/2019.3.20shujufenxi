import pandas as pd 
import numpy as np  

data=pd.DataFrame(np.arange(16).reshape(4,4),columns=['one','two','three','four'])

data.drop(['one'],axis=1)   #删除列
data.drop([0,1],axis=0)    #删除行



#映射 

data=pd.DataFrame(np.random.randn(3,4),columns=list('abcd'))
np.abs(data)


###DataFrame.applymap
def f(s,n=2):
    return s[:n]   #前2行
data.apply(f,axis=0)


func=lambda x:x**2
data.applymap(func)

###Series.apply(针对Series 对象进行逐元素处理)

s=pd.Series([2,1,3,7],index=list('abcd'))

f=lambda x:x**2
s.map(f)



#####排序
data=pd.DataFrame(np.random.randint(10,15,16).reshape(4,4),columns=['one','two','three','four'],index=['SH','SZ','GZ',np.nan])
data.sort_index()  #对索引排序
data.sort_values(by='four')  #基于‘four’列进行排序

data.sort_values(by=['four','three'])  #先排序'four'，在排序'three'
data.sort_values(by='three').sort_values(by='four',ascending=False)


#####数据合并
df1 = pd.DataFrame({'key1':['foo','bar','baz','foo'],'data1':list(np.arange(1,5))})
df2 = pd.DataFrame({'key1':['foo','bar','qux','bar'],'data2':list(np.arange(5,9))})


df1.merge(df2,left_on='key1',right_on='key1',how='left') #inner:内联;outer:外联；left:左联;右联：right
df1.merge(df2,on='key1',how='outer')  #如果合并时，两个表合并的列名是一样，用on


left1=pd.DataFrame({'key':['a','c','b','c'],'value1':[1,2,3,4],'value2':[4,5,6,7]},index=['a','b','c','e'])
right1=pd.DataFrame([[7,8],[9,10],[11,12],[13,14]],index=['b','c','d','a'],columns=['value3','value4'])
left1.merge(right1,left_index=True,right_index=True)  ###根据索引合并
left1.merge(right1,left_on=['key'],right_index=True)  ####根据1表的key,和2表的index合并



#######concat  合并Series
s1=pd.Series(np.arange(5))
s2=pd.Series(np.random.randint(1,10,5),index=[0,1,2,4,8])

pd.concat([s1,s2],axis=0)
pd.concat([s1,s2],axis=1)



#######conmbine_first  合并重叠数据  ####>>>>>去重
df1 = pd.DataFrame({'a':[1,np.nan,5.,np.nan],'b':[np.nan,2,np.nan,6],'c':list(np.arange(2,18,4))})
df2 = pd.DataFrame({'a':[5,4,np.nan,3,7],'b':[np.nan,3,4,6,8]})

df1.combine_first(df2)


print(df1.combine_first(df2))
# print(left1.merge(right1,left_on=['key'],right_index=True))

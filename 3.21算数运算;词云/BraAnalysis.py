import pymongo
import pandas as pd
import numpy
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'Simhei'


client = pymongo.MongoClient('localhost')
db = client['JD']

def get_data():
    '''
    获取数据
    :return:
    '''
    data=pd.DataFrame(list(db['BraItem'].find()))#从数据库提取数据，转化为DataFrame对象
    data=data.drop(['_id','id',],axis=1)#删除无关变量
    data.to_csv('./data/bradata.csv',encoding='gb18030',index=False)#保存数据
    return data

def get_cup(cup_str):
    '''
    提取罩杯信息系
    :param cup_str:
    :return:
    '''
    cups = ['A','B','C','D','E']
    for cup in cups:
        if cup in cup_str.upper():
            return cup

def get_cup_distribute(cup_series):
    '''
    绘制罩杯占比分布图
    :param cup_series:
    :return:
    '''
    cup_count=cup_series.value_counts()#统计罩杯频数
    cup_rate = cup_count.div(cup_count.sum())*100#统计频率
    labels = cup_rate.index+'罩杯'
    plt.figure(figsize=(5,5))
    #绘制饼状图
    plt.pie(list(cup_rate.values),labels=labels,autopct='%.2f%%')
    #保存图片
    plt.savefig('./image/CupImg.png',dpi=400,bbox_inches='tight')


def main():
    data=get_data()#获取数据
    # print(data.info())
    data['cup']=data['productSize'].apply(get_cup)#提取罩杯信息
    get_cup_distribute(data['cup'])#绘制罩杯分布图

if __name__=='__main__':
    main()
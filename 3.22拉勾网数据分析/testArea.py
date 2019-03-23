import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
plt.rcParams['font.sans-serif'] = 'Simhei'




def get_city_distribute(city_series,pathname,num=0):
    
                    
    '''
    统计不同城市的频数和频率，并绘制饼状图
    :param city_series:
    :return:
    '''
    city_counts=city_series.value_counts()
    #判断是否需要提取’其他‘项
    if num>0:
        city_main = city_counts[city_counts>=num]
        city_other = city_counts[city_counts < num].sum()
        city_other=pd.Series(city_other,index=['其他'])
        city_counts=pd.concat([city_main,city_other])#统计频数
    city_rate=city_counts.div(city_counts.sum())*100
    plt.figure(figsize=(6,6))
    plt.pie(city_rate.values,labels=city_rate.index,autopct='%.2f%%')
    plt.show()

def get_field_count(field_sries):
    field_dict={}
    print(field_sries.iloc[0])

    # for i in range(len(field_sries)):
    #     for field in field_sries.iloc[i]:
    #         field=field.strip()
    #         if field !='':
    #             if field in field_dict:
    #                 field_dict[field]+=1
    #             else:
    #                 field_dict[field]=1
    #     print(field_dict)
    # return field_dict







def main():
    data = pd.read_csv('/home/aallen/git/3.3数据分析/数据阶段/3.22拉勾网数据分析/data/LagouPostion.csv',encoding='gb18030')
    data=data.drop_duplicates()#去重
    data=data[data['jobNature']=='全职']#提取‘全职’的招聘信息
    get_city_distribute(data['city'],'/home/aallen/git/3.3数据分析/数据阶段/3.22拉勾网数据分析/image/cityneed.png',num=100)#统计城市的频数和频率，并绘图
    # print(data['industryField'].unique())
    data['field']=data['industryField'].str.strip().str.replace('、',',').str.replace(' ',',').str.split(',')
    field_dict=get_field_count(data['field'])##



if __name__=='__main__':
    main()
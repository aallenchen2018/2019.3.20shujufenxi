import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
plt.rcParams['font.sans-serif'] = 'Simhei'

def get_field_count(field_seiris):
    '''
    统计不同行业出现的频数，用来统计词频
    :param field_seiris:包含行业的Series对象，每个元素为list
    :return:
    '''
    field_dict={}
    for i in range(len(field_seiris)):#对数据数量进行循环
        for field in field_seiris.iloc[i]:#循环每个元素出现的行业
            field = field.strip()
            if field != '':#判断在字典是否出现过该词
                if field in field_dict:
                    field_dict[field] += 1
                else:#如果不存在则进行初始化
                    field_dict[field] = 1
    return field_dict

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
    city_rate = city_counts.div(city_counts.sum())*100#每个城市的频率
    #数据可视化
    plt.figure(figsize=(6,6))
    plt.pie(city_rate.values,labels=city_rate.index,autopct='%.2f%%')
    plt.savefig(pathname,dpi=400,bbox_inches='tight')

def get_word_cloud(word_dict,pathname,max_font_size=3000):
    '''
    绘制词云图
    :param word_dict: #词频字典
    :param pathname: 保存的图片路径和名字
    :param max_font_size: #最大字体
    :return:
    '''
    plt.figure(figsize=(6,6))
    backgroud_img = plt.imread('/home/aallen/git/3.3数据分析/数据阶段/3.22拉勾网数据分析/data/timg.jpg')#读取背景图
    #声明词云对象
    wc = WordCloud(
        background_color='white',#背景色
        mask=backgroud_img,#背景图片
        font_path='./data/simhei.ttf',#字体路径
        colormap='hsv',#色谱
        max_font_size=max_font_size,#最大字体
        max_words=1000#显示字数
    )
    wc.generate_from_frequencies(word_dict)#将词频加入词云对象
    plt.imshow(wc)#将此云放到plt中
    plt.axis('off')#去除坐标显示
    plt.savefig(pathname,dpi=400,bbox_inches='tight')#保存


def main():
    data = pd.read_csv('/home/aallen/git/3.3数据分析/数据阶段/3.22拉勾网数据分析/data/LagouPostion.csv',encoding='gb18030')
    data=data.drop_duplicates()#去重
    data=data[data['jobNature']=='全职']#提取‘全职’的招聘信息
    get_city_distribute(data['city'],'/home/aallen/git/3.3数据分析/数据阶段/3.22拉勾网数据分析/image/cityneed.png',num=100)#统计城市的频数和频率，并绘图
    # print(data['industryField'].unique())
    data['field']=data['industryField'].str.strip().str.replace('、',',').str.replace(' ',',').str.split(',')

    field_dict = get_field_count(data['field'])#统计行业频数
    get_word_cloud(field_dict,'./image/行业词云1.png')#绘制行业词云图
    #不同工作年限的需求分布
    get_city_distribute(data['workYear'],pathname='./image/工作年限.png')




if __name__=='__main__':
    main()
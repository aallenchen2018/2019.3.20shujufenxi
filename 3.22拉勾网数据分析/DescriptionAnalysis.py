import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'Simhei'
from SalaryAnalysis import get_salary
from AreaAnalysis import get_field_count,get_word_cloud
import jieba
import re
plt.rcParams['font.sans-serif'] = 'Simhei'

def get_stop_word(filepath='./data/中文停用词库.txt'):
    '''
    获取停用词
    :param filepath:
    :return:
    '''
    stop_words=[]
    with open(filepath,'r',encoding='gb18030') as f:
        lines= f.readlines()
    for line in lines:
        stop_words.append(line.strip())
    return stop_words

def get_description(description_str):
    '''
    拆解描述信息,提取词语信息
    :param description_str:
    :return:
    '''
    #替换一些无关词
    description_str = description_str.strip().replace('职责','').replace('岗位','').replace('要求','').replace('工作','')
    word_gen=jieba.cut(description_str)#进行分词
    useless=['职位','描述','负责','数据','/','.']
    stop_words = get_stop_word()
    words=[]
    for word in word_gen:#循环每个词
        word = word.strip()
        #判断是否满足要求
        if word != '' and word not in stop_words and word not in useless:
            words.append(word)
    return words

def get_skill(description_str):
    '''
    提取技能信息
    :param description_str:
    :return:
    '''
    #正则表达式提取英文词语
    skills=re.findall(r'([a-zA-Z]+)',description_str,re.S)
    skill_word=[]
    for skill in skills:
        skill = skill.upper()
        #修正一些词语
        if 'EXC' in skill:
            skill='EXCEL'
        if 'POWERPOINT' in skill:
            skill='PPT'
        skill_word.append(skill)
    return skill_word

def get_skill_salary(df):
    '''
    获取不同技能下的平均薪酬
    :param df:
    :return:
    '''
    #数据分析相关的一些技能
    skills = ['EXCEL','PPT','SQL','统计学','PYTHON','R','SAS','SPSS','机器学习','HIVE','HADOOP','SPARK']
    salary_skill_sum={}#每个技能下所有薪酬的总和
    salary_skill_count={}#每个技能出现的次数
    for skill in skills:#主要技能进行循环
        for i in range(len(df)):#数据集每行进行循环
            if skill in df['description'].iloc[i].upper():#判断技能是否在职位描述里面
                #判断当前循环的技能是否在字典里面
                #如果在，则在原来的基础上进行相加
                if skill in salary_skill_count:
                    salary_skill_sum[skill] += df['money'].iloc[i]
                    salary_skill_count[skill] += 1
                #如果不在，就进行初始化处理
                else:
                    salary_skill_sum[skill] = df['money'].iloc[i]
                    salary_skill_count[skill] = 1
    #统计每个技能下的平均薪酬
    salary_skill_mean={}
    for skill in salary_skill_count:
        salary_skill_mean[skill]=salary_skill_sum[skill]/salary_skill_count[skill]
    return salary_skill_mean

def get_skill_salary_distribute(salary_skill):
    '''
    不同技能的薪酬分布
    :param salary_skill: dict，不同技能的薪酬
    :return:
    '''
    salary_skill_series = pd.Series(salary_skill)#转化为Series对象
    plt.figure(figsize=(8,5))
    salary_skill_series.plot(kind='bar')#绘制柱状图
    plt.xticks(rotation=0,fontsize=12)
    x = range(len(salary_skill_series))
    y = list(salary_skill_series.values)
    #添加数字标签
    for a,b in zip(x,y):
        plt.text(a,b+0.3,str(round(b,2)),horizontalalignment='center',fontsize=10)
    plt.ylabel('薪酬(K/月)',fontsize=12)
    plt.savefig('./image/技能薪酬.png',dpi=400)


def main():
    data = pd.read_csv('./data/LagouPosition1234.csv', encoding='gb18030')
    data = data.drop_duplicates()  # 去重
    data = data[data['jobNature'] == '全职']  ##提取‘全职’的招聘信息
    #对描述信息进行分词，去除停用词和无用词
    data['describe']=data['description'].apply(get_description)
    #统计职责词频
    word_dict = get_field_count(data['describe'])
    #绘制职责的词云图
    get_word_cloud(word_dict,'./image/职责描述.png',max_font_size=300)

    #统计技能
    data['skill']=data['description'].apply(get_skill)
    #统计技能词频
    skill_dict = get_field_count(data['skill'])
    #绘制技能词云图
    get_word_cloud(skill_dict, './image/技能需求.png', max_font_size=300)

    data['money']=data['salary'].apply(get_salary)#薪酬处理
    #不同技能下的薪酬均值
    salary_skill=get_skill_salary(data[['description','money']])
    #绘制不同技能下薪酬柱状图
    get_skill_salary_distribute(salary_skill)


if __name__=='__main__':
    main()
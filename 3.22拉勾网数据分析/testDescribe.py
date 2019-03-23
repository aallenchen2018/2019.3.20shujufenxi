import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'Simhei'
from SalaryAnalysis import get_salary
from AreaAnalysis import get_field_count,get_word_cloud
import jieba
import re
import csv


def get_stop_word(filepath='数据阶段/3.22拉勾网数据分析/data/中文停用词库.txt'):
    stop_words=[]
    with open(filepath,'r',encoding='gb18030')as f:
        lines=f.readlines()
    
    for line in lines:
        stop_words.append(line.strip())
    return stop_words


def get_description(description_str):

    description_str=description_str.strip().replace('职责','').replace('岗位','').replace('要求','')
    word_gen=jieba.cut(description_str)
    useless=['职位','描述','负责','/']
    stop_words=get_stop_word()
    words=[]
    for word in word_gen:
        word=word.strip()
        if word!='' and word not in stop_words and word not in useless:
            words.append(word)
    return words







def main():
    data=pd.read_csv('/home/aallen/git/3.3数据分析/数据阶段/3.22拉勾网数据分析/data/LagouPosition1234.csv',encoding='gb18030')
    data=data.drop_duplicates()
    data=data[data['jobNature']=='全职']
    data['describe']=data['description'].apply(get_description)
    with open('/home/aallen/git/3.3数据分析/数据阶段/3.22拉勾网数据分析/data/descri.csv','w',encoding='gb18030') as f:
        writer=csv.writer(f)
        writer.writerows(data['describe'])
    #统计职责的词频
    word_dict=get_field_count(data['describe'])
    



if __name__=='__main__':
    main()

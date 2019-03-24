from AreaAnalysis import *

def get_salary(saraly_str):
    '''
    提取薪酬信息
    :param saraly_str:
    :return:
    '''
    saraly_li=saraly_str.strip().replace('k','').replace('K','').split('-')
    # print(saraly_str)
    area = int(saraly_li[1])-int(saraly_li[0])
    return int(saraly_li[0])+0.5*area

def get_salary_distribute(salary_series):
    '''
    薪酬分布
    :param salary_series:
    :return:
    '''
    bins=[0,8,16,24,30,float('inf')]
    plt.figure(figsize=(8, 5))
    #离散化，并绘制柱状图
    pd.cut(salary_series.values,bins=bins).value_counts().plot(kind='bar')
    plt.xticks(rotation=30)
    plt.xlabel('薪酬区间(K/月)',fontsize=12)
    plt.savefig('./image/薪酬分布.png',dpi=400,bbox_inches='tight')

def get_city_salary_distribute(df):
    '''
    获取不同城市的薪酬的分布
    :param df:
    :return:
    '''
    #主要城市
    cities = ['北京','上海','深圳','广州','杭州','成都']
    city_salary=[]#不同城市包含的所有的薪酬列表
    avg_salary=[]#不同城市的薪酬均值
    for city in cities:
        city_salary.append(df[df['city']==city]['money'])#某城市的所有的薪酬
        avg_salary.append(df[df['city'] == city]['money'].mean())#某城市的薪酬的均值
    plt.figure(figsize=(8,5))
    plt.boxplot(city_salary,labels=cities)#箱型图
    plt.xticks(fontsize=13,rotation=30)
    plt.ylabel('薪酬：K/月')
    plt.scatter(range(1,len(avg_salary)+1),avg_salary,marker='s')
    plt.savefig('./image/城市薪酬分布.png',dpi=400)


def get_education_salary_distribute(df,pathname,by='education'):
    '''
    不同教育背景的薪酬分布
    :param df:
    :return:
    '''
    df=df[df[by] != '博士']#博士的岗位比较少，进行剔除
    #提取不同类别情况下的薪酬
    a=df.groupby(by=[by])['money'].apply(lambda x:x.values)
    #提取不同类别的薪酬中位数，并进行排序
    b=df.groupby(by=[by])['money'].median().sort_values()
    #对数据进行重排
    a = pd.Series(a,index=b.index)
    plt.figure(figsize=(8,5))
    plt.boxplot(a,labels=a.index)#箱型图
    plt.xticks(fontsize=13)
    plt.savefig(pathname,dpi=400)

def main():
    data = pd.read_csv('/home/aallen/git/3.3数据分析/数据阶段/3.22拉勾网数据分析/data/LagouPostion.csv',encoding='gb18030')
    data = data.drop_duplicates()  # 去重
    data = data[data['jobNature'] == '全职']  ##提取‘全职’的招聘信息
    data['money']=data['salary'].apply(get_salary)#提取工资信息
    get_salary_distribute(data['money'])#薪酬分布
    get_city_salary_distribute(data[['money','city']])#不同城市的薪酬分布
    #不同教育背景的薪酬分布
    get_education_salary_distribute(data[['education','money']],'./image/教育背景薪酬.png')
    #不同工作年限的薪酬分布
    get_education_salary_distribute(data[['workYear','money']],'./image/工作经验薪酬.png',by='workYear')

if __name__=='__main__':
    main()
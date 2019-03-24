from AreaAnalysis import *

def get_salary(salary_str):

    saraly_li=salary_str.strip().replace('k','').replace('K','').split('-')
    area=int(saraly_li[1])-int(saraly_li[0])
    return int(saraly_li[0])+0.5*area


def get_saraly_distribute(salary_series):
    bins=[0,9,15,25,29,float('inf')]
    plt.figure(figsize=(8,5))
    pd.cut(salary_series.values,bins=bins).value_counts().plot(kind='bar')
    plt.xticks(rotation=30)
    plt.xlabel('薪酬区间（K/月）',fontsize=12)
    plt.savefig('/home/aallen/git/3.3数据分析/数据阶段/3.22拉勾网数据分析/image/薪酬分步test.png',dpi=400,bbox_inches='tight')


def get_city_salary_distribute(dis):
    cities=['北京','上海','深圳','广州','杭州','成都']
    # print(dis)
    city_salary=[]
    for city in cities:
        city_salary.append(dis[dis['city']==city]['money'])
    plt.figure(figsize=(8,5))
    plt.boxplot(city_salary,labels=cities)
    plt.xticks(fontsize=13,rotation=30)
    plt.ylabel('薪酬：K/月')
    # plt.show()
    plt.savefig('/home/aallen/git/3.3数据分析/数据阶段/3.22拉勾网数据分析/image/城市薪酬分布test.png',dpi=500)



def get_education_salary_dis(data,pathname,bywhat='education'):
    a=data.groupby(by=bywhat)['money'].apply(lambda x:x.values)
    aa=data.groupby(by=bywhat)['money']
    b=data.groupby(by=bywhat)['money'].median().sort_values()
    aaa=pd.Series(a,index=b.index)
    
    plt.figure(figsize=(8,7))
    plt.boxplot(aaa,labels=aaa.index)
    plt.xticks(fontsize=13)
    plt.savefig(pathname,dpi=600)







def main():
    data=pd.read_csv('/home/aallen/git/3.3数据分析/数据阶段/3.22拉勾网数据分析/data/LagouPostion.csv',encoding='gb18030')
    data=data.drop_duplicates()
    data=data[data['jobNature']=='全职']
    data['money']=data['salary'].apply(get_salary)
    get_saraly_distribute(data['money'])
    get_city_salary_distribute(data[['money','city']])

    get_education_salary_dis(data[['education','money']],'/home/aallen/git/3.3数据分析/数据阶段/3.22拉勾网数据分析/image/教育背景薪酬test1.png')




if __name__=='__main__':
    main()
import pandas as pd
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'Simhei'

def get_stopword(filepath='./data/中文停用词库.txt'):
    '''
    获取停用词
    :param filepath:
    :return:
    '''
    stop_word=[]
    with open(filepath,'r',encoding='gb18030') as f:
        lines=f.readlines()
    for line in lines:
        stop_word.append(line.strip())
    return stop_word

def get_fenci(rate_str):
    '''
    提取每条评论的词，去除停用词
    :param rate_str:
    :return:
    '''
    word_gen=jieba.cut(rate_str)
    stopword = get_stopword()
    words=[]
    useless = ['～','~','........','*']
    for word in word_gen:
        word = word.strip()
        if word != '' and word not in stopword and word not in useless:
            words.append(word)
    return words

def get_word_dict(words_series):
    '''
    统计词频
    :param words_series:包含词语的seires对象
    :return:
    '''
    word_dict={}
    for i in range(len(words_series)):#遍历每条评论
        for word in words_series[i]:#遍历每条评论内的词语
            if word in word_dict:#判断是否在字典中
                word_dict[word] += 1
            else:#如果不在，进行初始化
                word_dict[word] = 1
    return word_dict

#参考url:
#应用参考：https://blog.csdn.net/fly910905/article/details/77763086
#wordcloud参数：https://blog.csdn.net/yaochuyi/article/details/80094659
#colormap选择：https://matplotlib.org/examples/color/colormaps_reference.html
def get_word_cloud(word_dict):
    '''
    绘制词云图
    :param word_dict:
    :return:
    '''
    backgroud_img = plt.imread('./data/back.jpg')#读取背景图片
    #声明wordcloud对象
    wc = WordCloud(
        background_color='white',#背景颜色
        mask=backgroud_img,#背景图片
        font_path='./data/simhei.ttf',#若为中文，必须添加改路径，字体路径
        colormap='hsv',#色谱选择
        max_words=1000,#最多显示的词语数量
        max_font_size=300#最大的词语字体大小
    )
    wc.generate_from_frequencies(word_dict)#生成包含词语的词云对象
    plt.imshow(wc)#将wc对象添加到plt中显示
    plt.axis('off')#关闭坐标轴
    #保存
    plt.savefig('./image/词云图.png',dpi=400,bbox_inches='tight')

def main():
    data = pd.read_csv('./data/bradata.csv',encoding='gb18030')#读取数据
    data['words']=data['content'].apply(get_fenci)#提取每条评论的词语
    word_dict = get_word_dict(data['words'])#获得词频
    get_word_cloud(word_dict)#绘制词云图


if __name__=='__main__':
    main()
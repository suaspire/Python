# import requests
# from bs4 import BeautifulSoup
# url = "http://www.santostang.com"
#headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"}
# request = requests.get(url)
# soup = BeautifulSoup(request.text,"lxml") #使用BeautifulSoup解析这个网页
# title = soup.find("h1",class_="post-title").a.text.strip() #查找到h1标签下的 a标签 的文本信息
# print(title)
# print(request.encoding)
# print(request.status_code)

# a = []
# for i in range(1,100):
#     if i%2 != 0:
#         a.append(i)
# print(a)
#
# import re
# str1 = '你好$$$我正在学Python@#@#现在需要&%&%&修改字符串'
# str2 = str1.replace('$$$','\n').replace('@#@#','').replace('&%&%&','')
# str3 = re.sub(r'[$@#%&]+','',str1)
# print(str3)

####get post 两种不同的请求方式
# import requests
#
# url = "http://httpbin.org"
# key_dict = {'key1':'value1','key2':'value2'}
# # r = requests.post(url+'/post',data=key_dict)
# # print('URL以争取编码',r.url)     #URL以争取编码 http://httpbin.org/post
# # print('字符串方式的响应体\n',r.text)
# try:
#     r = requests.get(url + '/get', params=key_dict, timeout=10)
#     print('URL以争取编码', r.url)  # URL以争取编码 http://httpbin.org/get?key1=value1&key2=value2
#     print('字符串方式的响应体\n', r.text)
# except  requests.exceptions.ConnectTimeout:
#     print('timeout')



# headers = {'Host': 'www.santostang.com',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}
# r = requests.get('http://www.santostang.com',headers=headers)
# print(r.status_code)

##############爬取豆瓣top250
import re
import csv
import pandas as pd
import requests
from bs4 import BeautifulSoup
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

def get_movie_name(url,m):
    movie_list = []

    headers = {'Host': 'movie.douban.com',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}
    for i in range(0,m):
        ######print(i,'================================================')
        r = requests.get(url+str(i*25),headers=headers)
        soup = BeautifulSoup(r.text,'lxml')
        totalContent = soup.find('ol',{'class':'grid_view'}).findAll('li')
        for item in totalContent:
            rank = item.em.text.strip()
            link = item.a['href']
            nameList = item.find_all('span',{'class':'title'})
            Chinesename = nameList[0].get_text()
            if(len(nameList) == 2):
                Englishname = nameList[1].get_text().replace('/','')
            else:
                Englishname = None
            othername = item.find('span',{'class':'other'}).get_text().replace('/','')
            relate = item.find('p',{'class':''}).get_text().replace(' ','')  #主演导演信息
            rating = item.find('span',{'class':'rating_num','property':'v:average'}).get_text()
            starDiv = item.find('div',{'class':'star'})
            ratingN = starDiv.find_all('span')[3].get_text()
            ratingNum = re.split(r"\D",ratingN)[0]
            try:
                abstract = item.find('span', {'class': 'inq'}).get_text()
            except AttributeError:
                abstract = "None"
            OutputStr = "排名: " + rank + '\t网址:\t' + link +'中文名\t'+Chinesename+ '别名\t'+othername+ '评分\t'+rating
            ########print(OutputStr)
            eachList = [rank,link,Chinesename,Englishname,othername,rating,ratingNum,abstract,relate]
            movie_list.append(eachList)
    return movie_list
def storeToCsv(movies):
    csvFile = open('movies.csv','a+',encoding='utf-8')
    try:
        writer = csv.writer(csvFile)
        writer.writerow(('排名',"网址",'中文名','英文名','别名','评分','评价人数','摘要','相关信息'))
        for i in movies:
            writer.writerow(i)
    finally:
        csvFile.close()

def csvPandas(movie):
    columns = ['排名',"网址",'中文名','英文名','别名','评分','评价人数','摘要','相关信息']
    test = pd.DataFrame(columns=columns,data=movie)
    test.to_csv('test.csv')  #,header=False)

if __name__ == '__main__':
    names = []
    plot_dicts = []
    url = 'https://movie.douban.com/top250?start='
    movie = get_movie_name(url,2)
    for item in movie:
        names.append(item[2])
        plot_dict = {
            'value':int(item[6]),
            'label':item[1]
        }
        plot_dicts.append(plot_dict)
    #storeToCsv(movie)
    csvPandas(movie)   #利用Pandas进行数据的存储
    my_style = LS('#333366', base_style=LCS)

    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.title_font_size = 24
    my_config.label_font_size = 14
    my_config.major_label_font_size = 18
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1000
    chart = pygal.Bar(my_config, style=my_style)

    chart.title = 'Movie Rank'
    chart.x_labels = names
    chart.add('', plot_dicts)
    chart.render_to_file('movies.svg')



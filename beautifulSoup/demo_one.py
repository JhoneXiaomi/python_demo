'''
    获取URL
    获取Python100 url
    联系的url
'''
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'http://www.runoob.com/python/python-100-examples.html'
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
r = requests.get(url,headers = headers).content.decode("utf-8")
# print(r)
# soup = BeautifulSoup()
# 解析 使用bs4
# print(type(html))
soup = BeautifulSoup(r,'lxml')
# 查找每个联系的A 标签获取对应的连接地址,返回100个A标签的列表
a_list = soup.find(id='content').find_all('a')
# 创建一个列表
lis = []
for attr in a_list:
    lis.append(attr.attrs['href'])
# print(lis)

'''
    根据获取每个练习的连接地址获取每个页面的内容请求每个练习
'''

datas = []
for x in lis:
    dic  = { }
    # 请求详细页面
    ar = requests.get('http://www.runoob.com/'+x,headers=headers).content.decode('utf-8')
    # 解析HTML文档
    soup_ar = BeautifulSoup(ar,'lxml')
    # 查找联系内容
    # find标题
    dic['title'] = soup_ar.find(id = 'content').h1.text
    # find题目
    dic['tm'] = soup_ar.find(id = 'content').find_all('p')[1].text
    # print(tm)
    dic['cxfx'] = soup_ar.find(id = 'content').find_all('p')[2].text
    # print(cxfx)
    try:
        dic['code'] = soup_ar.find(class_='hl-main').text
    except Exception as e:
        dic['code'] = soup_ar.find('pre').text
    '''
    datas.append(dic)
    data = pd.DataFrame(datas)
    data.to_csv('D:\py.txt')
    '''
    with open('D:\py.txt','a+',encoding='utf-8') as file:
        file.write(dic['title']+'\n')
        file.write(dic['tm'] + '\n')
        file.write(dic['cxfx'] + '\n')
        file.write(dic['code'] + '\n')
        file.write('*'* 50 + '\n')



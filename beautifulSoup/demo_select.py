'''
    css选择器
'''
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'web.html'
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
soup = BeautifulSoup(open(url,'r',encoding='utf-8'),'lxml')
# 通过标签进行查找，返回所有的标签列表
'''
print(soup.select('span'))
print(soup.select('a'))
'''

# 通过类名进行查找
'''
print(soup.select('.header'))
'''

# 通过ID进行查找
'''
print(soup.select('#header'))
'''

# 通过属性进行查找
# print(soup.select('div[title~="head"]'))

# 组合查找
print(soup.select('#header span')[0].text)

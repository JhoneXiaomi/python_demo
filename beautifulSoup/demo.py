from bs4 import BeautifulSoup
import requests

'''
r = requests.get('http://www.baidu.com').content.decode('UTF-8')
# 解析HTML文档对象
soup = BeautifulSoup(r,'html.parser')
html = soup.prettify()
print(html)
'''
# 操作DOM
soup = BeautifulSoup(open('web.html','r',encoding='utf-8'),'lxml')
# print(type(soup))
'''
四大对象
'''
# Tag
'''
print(soup.div.attrs['id'])
'''
# NavigableString
print(type(soup.div.span.string))

'''
直接遍历文档树
'''

# 直接子节点，获取子节点时候会将换行符都取到 contents children
print(soup.div.contents)
print("============================")
print(soup.div.contents[0])
print(soup.div.contents[2])
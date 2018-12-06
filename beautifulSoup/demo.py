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
'''
print(soup.div.contents)
print("============================")
print(soup.div.contents[0])
print(soup.div.contents[2])
print(soup.div.span.string)
print(soup.div.span.text)
'''
'''
获取当前节点的父节点，空格也作为一个子节点
next_sibling 兄弟节点
previous_sibling 上一个节点
'''
# print(soup.div.contents[1].parents)
# print(soup.div)
# menu = soup.div.next_sibling.next_sibling
# print(menu.previous_sibling.previous_sibling)


'''
搜索文档树
    find_all 查找所有的动态节点，可以与正则表达式结合使用
    find 常与单独的一个节点结合使用
'''

'''
result = soup.find_all('div')
for r in result:
    print(r.text)
    # print(r.attrs['href'])
'''

# print(soup.find(id='header').find_all('span',limit=1))



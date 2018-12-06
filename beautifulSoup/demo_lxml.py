from lxml import etree

# 解析为HTML文档
html = etree.HTML(open('web.html',encoding='utf-8').read())
# html = etree.parse(open('web.html',encoding='utf-8'))
# html = etree.fromstring(open('web.html',encoding='utf-8').read())
''' 
# 使用decode进行解码
result = etree.tostring(html,pretty_print=True,encoding='utf-8').decode('utf-8')
print(result)
'''

'''
    选取节点，Xpath选取，以列表的形式返回
    '/'从根节点开始选取
    '//'从相对位置开始选取,返回文档中所有的标签
    '@'属性
'''
dom = html.xpath('/div')
dom = html.xpath('//div')
dom = html.xpath('/html/.')
dom = html.xpath('//div[@id]')
print(dom)


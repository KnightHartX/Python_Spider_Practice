#导入bs4模块
from bs4 import BeautifulSoup
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

#做一个美味汤
soup = BeautifulSoup(html, 'html.parser')
#输出结果
print(soup.prettify())
# 找出所有为<a>的标签
for link in soup.find_all('a'):
    print("为a的标签：")
    print(link.get('href'))
# 获取所有的文字内容
print("获取所有文字内容：")
print(soup.get_text())
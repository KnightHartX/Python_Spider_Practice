import bs4
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
#首先我们先将html文件已lxml的方式做成一锅汤
soup = bs4.BeautifulSoup(open('demo.html'), 'lxml')

#我们把结果输出一下，是一个很清晰的树形结构。
print(soup.prettify())
print("-----------------------")
tag = soup.find_all('a')
print(tag)
print("-----------------------")
print(tag[1])
print("-----------------------")

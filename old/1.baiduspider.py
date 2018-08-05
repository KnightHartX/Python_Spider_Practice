import urllib.request
response = urllib.request.urlopen('https://www.baidu.com/')
html = response.read()
print (html)
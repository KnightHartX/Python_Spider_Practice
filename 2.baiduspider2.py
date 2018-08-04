import urllib.request
req = 'https://www.baidu.com'
response = urllib.request.urlopen(req)
the_page = response.read()
print (the_page)
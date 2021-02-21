# 網路連線
# https://docs.python.org/3/library/urllib.request.html
import urllib.request as request
import ssl #for Mac
ssl._create_default_https_context = ssl._create_unverified_context #for Mmac
src = 'https://www.netflix.com/'
src_2 = 'https://www.books.com.tw/'

with request.urlopen(src_2) as response:
    #data = response.read() #取得網站的原始碼(HTML, CSS, JavaScript)
    data = response.read().decode('utf-8')
print(data)
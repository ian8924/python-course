# step 1: 連線到特定網址，抓取資料
# step 2: 擷取有意義的資料，進行分析

# step 1: 連線到特定網址，抓取資料 
# urllib.error.HTTPError: HTTP Error 403: Forbidden
import urllib.request as req
import ssl #for Mac
ssl._create_default_https_context = ssl._create_unverified_context #for mac
url = 'https://www.dcard.tw/f'
# view-source: https://www.dcard.tw/f 網頁原始碼
with req.urlopen(url) as response:
    data = response.read().decode('utf-8')
print(data)



import urllib.request as req
import ssl #for Mac
ssl._create_default_https_context = ssl._create_unverified_context #for mac
# 如何模擬真正的使用者
# 右鍵 -> inspect -> Network -> 重新整理網頁
# Request Headers: 使用者在連線到網站時所發出的資料
# user-agents 完全複製user-agents的內容
url = 'https://www.dcard.tw/f'
# view-source:https://www.dcard.tw/f 網頁原始碼 
# 建立request物件與header資訊
request = req.Request(url, headers={
    'user-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
})
with req.urlopen(request) as response:
    data = response.read().decode('utf-8')
print(data)

# 使用BeautifulSoup Module來抓取資料
# pip3 install beautifulSoup4

import urllib.request as req
import ssl #for Mac
ssl._create_default_https_context = ssl._create_unverified_context #for mac
import bs4 # pip3 install beautifulsoup4
url = 'https://www.dcard.tw/f'
# 建立request物件與header資訊
request = req.Request(url, headers={
    'user-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
})
with req.urlopen(request) as response:
    data = response.read().decode('utf-8')

# 使用beautifulsoup
parsed_data = bs4.BeautifulSoup(data,'html.parser')

# 找出所有標題
# find_all
titles = parsed_data.find_all('a', class_ = 'tgn9uw-3 ebwnQU') # 找尋class = 'tgn9uw-3 ebwnQU'的標籤
print(titles) # list

# mini challenge
# 印出所有標題(不含HTML tag)
# 我有一個PR99的女友
# 想幫我爸找一位恩人
# #更 廁所有毒？
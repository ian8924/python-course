import urllib.request as req
import ssl #for Mac
ssl._create_default_https_context = ssl._create_unverified_context #for mac
import bs4 # pip3 install beautifulsoup4
url = 'https://www.dcard.tw/f/trending'
# 建立request物件與header資訊
request = req.Request(url, headers={
    'user-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
})
with req.urlopen(request) as response:
    data = response.read().decode('utf-8')

# 使用beautifulsoup
parsed_data = bs4.BeautifulSoup(data,'html.parser')
# print(parsed_data)
# print(parsed_data.title) # 抓到tiltle標籤 title="Dcard"
# print(parsed_data.title.string) # 抓到tiltle文字

# 抓出文章標題
# find，找出一個符合的條件
# <a class="tgn9uw-3 ebwnQU" href="/f/relationship/p/234496937">
# <span>我有一個PR99的女友</span>
# </a>
# titles = parsed_data.find('a', class_ = 'tgn9uw-3 iuyCWN') # 找尋class = 'tgn9uw-3 ebwnQU'的標籤
# print(titles.span.string)
# content = parsed_data.find('div', class_ = 'tgn9uw-4 dcYnIB') # 找尋class = 'tgn9uw-3 ebwnQU'的標籤
# print(content.span.string)

print('--------------')

titles = parsed_data.find_all('a', class_ = 'tgn9uw-3 iuyCWN') # 找尋class = 'tgn9uw-3 ebwnQU'的標籤
# print(titles)
for title in titles:
    print(title.span.string)
# content = parsed_data.findAll('div', class_ = 'tgn9uw-4 dcYnIB')[3] # 找尋class = 'tgn9uw-3 ebwnQU'的標籤
# print(content.span.string)
# 抓出文字
# print(titles.string)



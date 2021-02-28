import json
import urllib.request as req
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context 
import bs4 
url = 'https://movies.yahoo.com.tw/chart.html?cate=us'
# 建立request物件與header資訊
request = req.Request(url, headers={
    'user-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
})
with req.urlopen(request) as response:
    data = response.read().decode('utf-8')
parsed_data = bs4.BeautifulSoup(data,'html.parser')
titles = parsed_data.find_all('div',class_="rank_txt")
print(titles)
# times = parsed_data.find_all('span',class_="time") 
# for i in range(0,len(titles)):
#     print(f'{i+1}. {titles[i].string} {times[i].string}')

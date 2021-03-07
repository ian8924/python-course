import json
import urllib.request as req
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context 
import bs4 
url = 'https://kma.kkbox.com/charts/hourly?terr=hk&lang=tc'
# 建立request物件與header資訊
request = req.Request(url, headers={
    'user-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
})
with req.urlopen(request) as response:
    data = response.read().decode('utf-8')
# print(data)
parsed_data = bs4.BeautifulSoup(data,'html.parser')
# print(parsed_data.html.body)
titles = parsed_data.find_all('div',class_="_7effa9d9b3900e9698aa6e0423a1e841-scss _98a17d59ea3df3c60b9699a6afe43816-scss")
print(titles)
# times = parsed_data.find_all('span',class_="time") 
# for i in range(0,len(titles)):
#     print(f'{i+1}. {titles[i].string} {times[i].string}')

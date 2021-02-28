# 將某個特定版標題寫入dcard.txt，並且換行
# 抓出該版前十大熱門話題
# Dcard 前十熱門討論
# 1. 我有一個PR99的女友 
# 2. 想幫我爸找一位恩人 
# 3. #更 廁所有毒？...

import json
import urllib.request as req
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context 
import bs4 
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
titles = parsed_data.find_all('a', class_ = 'tgn9uw-3 iuyCWN') # 找尋class = 'tgn9uw-3 ebwnQU'的標籤
with open('dcard.txt', 'w', encoding='utf-8') as file:
    for i in range(0,10):
        file.write(f'{i+1}.{titles[i].span.string}\n')

# extra challenge
# 抓出該版前十大熱門話題外加表情回應
# 寫入dcard2.txt，並且換行
# 標題：我有一個PR99的女友  回應：7028
# 標題：想幫我爸找一位恩人  回應：5247
# 標題：#更 廁所有毒？  回應：4420
# titles = parsed_data.find_all('a', class_ = 'tgn9uw-3 iuyCWN') 
likes = parsed_data.find_all('div', class_ = 'cgoejl-3 fkFjDX') 

with open('dcard2.txt', 'w', encoding='utf-8') as file:
    for i in range(0,len(titles)):
        file.write(f'標題：{titles[i].span.string} 回應：{likes[i].string}\n')

import csv
header=['排名','標題','表情數']
with open('dcard.csv', mode = 'w',newline='', encoding='utf-8-sig') as csvfile:
    # 建立csv檔案寫入器
    writer = csv.writer(csvfile)
    # 寫入標題
    writer.writerow(header)
    for i in range(0,len(titles)):
        writer.writerow([i+1,titles[i].span.string,likes[i].string])
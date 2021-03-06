import urllib.request as request
import ssl #for Mac
import json #json格式
ssl._create_default_https_context = ssl._create_unverified_context #for Mmac
src = 'https://data.taipei/api/v1/dataset/f737b13b-b223-4158-b539-df3585324f09?scope=resourceAquire'

with request.urlopen(src) as response:
    data = json.load(response) #取得網站的原始碼(HTML, CSS, JavaScript)
#print(data)

# 取得景點列表
people_list = data['result']['results']
# print(spot_list)
# print(type(spot_list))

# 如何取得list裡面的每一個物件呢
# 寫入檔案
with open('people.txt', 'w', encoding='utf-8') as file:
    for spot in people_list:
        file.write(f'{spot["年月底別"]}  {spot["行政區"]}  人口數:{spot["人口數/總計[人]"]}\n')
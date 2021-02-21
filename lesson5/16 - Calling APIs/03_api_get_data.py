import urllib.request as request
import ssl #for Mac
import json #json格式
ssl._create_default_https_context = ssl._create_unverified_context #for Mmac
src = 'https://data.taipei/api/v1/dataset/36847f3f-deff-4183-a5bb-800737591de5?scope=resourceAquire'

with request.urlopen(src) as response:
    data = json.load(response) #取得網站的原始碼(HTML, CSS, JavaScript)
#print(data)

# 取得景點列表
spot_list = data['result']['results']
# print(spot_list)
# print(type(spot_list))

# 如何取得list裡面的每一個物件呢
for spot in spot_list:
    print(spot['stitle'])
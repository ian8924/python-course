# 台北市資料大平台 https://data.taipei/
# 臺北旅遊網景點資料(中文)
# https://data.taipei/api/v1/dataset/36847f3f-deff-4183-a5bb-800737591de5?scope=resourceAquire

import urllib.request as request
import ssl #for Mac
import json #json格式
ssl._create_default_https_context = ssl._create_unverified_context #for Mmac
src = 'https://data.taipei/api/v1/dataset/f737b13b-b223-4158-b539-df3585324f09?scope=resourceAquire'

with request.urlopen(src) as response:
    data = json.load(response) #取得網站的原始碼(HTML, CSS, JavaScript)
print(data)
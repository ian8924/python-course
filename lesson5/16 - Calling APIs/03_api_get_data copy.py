import urllib.request as request
import ssl #for Mac
import json #json格式
ssl._create_default_https_context = ssl._create_unverified_context #for Mmac
src = 'https://data.sfgov.org/resource/nxjg-bhem.json'

with request.urlopen(src) as response:
    data = json.load(response) #取得網站的原始碼(HTML, CSS, JavaScript)
print(data)

# 取得景點列表
# people_list = data
# print(spot_list)
# print(type(spot_list))

# 如何取得list裡面的每一個物件呢
for spot in data:
    print(spot["hospital"],spot["patientcount"])
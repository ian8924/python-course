# import json module
import json
# 讀取json資料，存在變數data裡
with open('data2.json', mode = 'r') as file:
    data = json.load(file)
# print(data) # dictionary
# print(data['name'])
# print(data['job'])

# 修改變數data的資料
data['name'] = 'ian'
data['job'] = 'softEngineer'
data['hobby'] = 'movie'
data['birth'] = '9/15'
del data['birth']

# 寫入json檔案
with open('data2.json', mode = 'w') as file:
    json.dump(data,file)


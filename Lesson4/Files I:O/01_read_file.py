# 讀取檔案
# 讀取已存在的檔案
# file = open('test.txt', mode = 'r', encoding='utf-8') # 開啟檔案
# data = file.read() # 檔案操作
# print(data)
# file.close() # 關閉檔案

# with 
with open('test.txt', mode = 'r', encoding='utf-8') as file:
    data = file.read()
print(data)

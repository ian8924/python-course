# 檔案處理流程
# step 1: 開啟檔案
# step 2: 讀取/讀寫file裡的資料
# step 4: 關閉檔案

# 開啟檔案
# 檔案物件 = open(檔案路徑, mode=開啟模式,encoding=編碼)
# 中文檔案使用encoding='utf-8'

# 檔案讀寫類型
# read - 'r' 讀取檔案
# append - 'a' 加入檔案
# write - 'w' 覆寫檔案
# create - 'x' 新增檔案，會報錯如果檔案已存在

# 讀取檔案
# 模式一：讀取全部文字
# 檔案物件.read()
# 模式二：一次讀取一行
# for 變數 in 檔案物件:
#   依序讀取每一行
# 模式三：讀取JSON格式
# import json
# 讀取到的資料 = json.load(檔案物件)

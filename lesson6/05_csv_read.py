import csv

# 開啟csv檔案
with open('mrt.csv', newline='', encoding='utf-8') as csvfile:
    # 讀取csv檔案內容
    rows = csv.reader(csvfile)
    # 迴圈輸出每一列
    for row in rows:
        print(row) # list形式

with open('mrt.csv', newline='', encoding='utf-8') as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        print(row) # dictionary形式

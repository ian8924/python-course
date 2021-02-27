import csv

header = ['編號','建案名稱', '樓地板面積', '每坪月租金','管理機關']
rows = [['1','永春站交19','26.44 ~ 65.30','4858','捷運局'],['2','永春站交19','26.44 ~ 65.30','4858','捷運局']]
rows_dic = [{'編號':'1','建案名稱':'永春站交19','樓地板面積':'26.44 ~ 65.30','每坪月租金':'4858','管理機關':'捷運局'},{'編號':'2','建案名稱':'永春站交19','樓地板面積':'26.44 ~ 65.30','每坪月租金':'4858','管理機關':'捷運局'}]

# 寫入 csv
# newline: 讓資料中包含的換行字元可以正確被解析
with open('mrt_new.csv', mode = 'w',newline='', encoding='utf-8-sig') as csvfile:
    # 建立csv檔案寫入器
    writer = csv.writer(csvfile)
    # 寫入一列資料
    writer.writerow(header)
    writer.writerows(rows)

with open('mrt_dic.csv', mode = 'w',newline='', encoding='utf-8-sig') as csvfile:
    writedCsv = csv.DictWriter(csvfile, header)
    writedCsv.writeheader()
    writedCsv.writerows(rows_dic)

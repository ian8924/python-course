# 寫入檔案
# 創建一個number.txt的檔案
# 一行一行寫入 10 20 30 40 50

# 讀取檔案
# 讀取number.txt的文字
# 並且印出來

# 讀取number.txt檔案每一行，並且把數字加總起來
# 印出加總
# hint: for loop!

import json

with open('number.txt', mode = 'w') as file:
    file.write('10\n')
    file.write('20\n')
    file.write('30\n')
    file.write('40\n')
    file.write('50')

with open('number.txt', mode = 'r') as file:
    data = file.read().split('\n') 
    #  ['10','20','30','40','50']
    total = 0
    for i in data:
        total = total+ int(i)
        # print(i)
print (total)


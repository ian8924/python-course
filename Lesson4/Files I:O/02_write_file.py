# 寫入檔案
# 若檔案存在，直接寫入
# 若檔案不存在，創建檔案並寫入
# file = open('test2.txt', mode = 'w') # 開啟檔案
# file.write('Hello World') # 檔案操作
# file.close() # 關閉檔案

# file = open('test2.txt', mode = 'w') # 開啟檔案
# file.write('Hello World\nAnother New Line') # 寫入多行
# file.close() # 關閉檔案

# file = open('test2.txt', mode = 'w', encoding = 'utf-8') # 中文檔案 
# file.write('我熱愛學習')
# file.close() # 關閉檔案

# with寫法
with open('test3.txt', mode = 'w', encoding = 'utf-8') as file:
    file.write('我是 Ian\n')
    file.write('我住在 Taipei')

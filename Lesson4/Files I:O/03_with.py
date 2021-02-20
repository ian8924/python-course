# 使用with就不需要file.close()
# 寫入檔案
with open('test.txt', mode = 'w', encoding='utf-8') as file:
    file.write('第一行\n第二行')

# 讀取檔案
with open('test.txt', mode = 'r', encoding='utf-8') as file:
    data = file.read()
print(data)
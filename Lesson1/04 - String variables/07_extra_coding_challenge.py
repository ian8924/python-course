# 1
# 定義一個String，存在變數string1
# 印出該String的反向
string1=input('string')
string1=string1[::-1]
print(string1)  

# 例子
# string1 = 'apple'
# 在terminal需印出 elppa

# 2
string2 = 'I love learning Python'
# 印出不含空白的字串 IlovelearningPython
print(string2.replace(" ",''))
# 3
# 請修正下列程式碼，使其能正確執行
bornYear = int(input('請輸入你的出生年份：'))
nowYear = int(input('請輸入今年的年份：'))
age =str(nowYear - bornYear)
print(f'你今年{age}歲')

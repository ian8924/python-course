# 讓我們來看看input()出來的結果是什麼類型
# your_age = input('How old are you? ')
# 使用type()
# print(type(your_age))

# first_num = input('請輸入一個數字 ')
# second_num = input('請再輸入一個數字 ')
# print(type(first_num))

# 如果你想將字串轉換成數字
# int() 會將字串轉化成整數
# print(int(first_num) + int(second_num))

# float() 會將字串轉化成小數
# print(float(first_num) + float(second_num))

height = int(input('身高是'))
weight = int(input('體重是'))
total= height+weight
print('身高加體重是：'+str(total))
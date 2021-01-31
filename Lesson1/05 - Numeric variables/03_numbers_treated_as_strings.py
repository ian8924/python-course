# Python會去'猜測'變數的形式

# 由於input() 回傳的是字串
# 賦予的變數形式將會是字串
first_num = input('Enter first number ')
second_num = input('Enter second number ')

# 若使用 + 在字串處理，則會直接連結兩個字串
print(first_num + second_num)
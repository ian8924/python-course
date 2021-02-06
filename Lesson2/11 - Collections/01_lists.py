my_list = ['Alice', 'Tobey', 100, 99, 98]
print(type(my_list))
print(my_list[0])
my_list[0] = 'Vickie'
print(my_list)
print(len(my_list))

# 在list的最後增加使用append
my_list.append('one more new name')
print(my_list)

# 若使用insert，必須要說明想要insert的位置
my_list.insert(1, 500)
print(my_list)

# 移除list裡的物件使用remove
my_list.remove('Tobey')
print(my_list)
my_list.remove(3000)
print(my_list)

# More functions
# https://docs.python.org/3/tutorial/introduction.html#lists

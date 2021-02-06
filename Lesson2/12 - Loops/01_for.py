# Python主要有兩種loops形式
# for loops
# while loops

# loops是在給定條件為True的情況下，會持續執行的迴圈
# a loop is used to execute a set of statements as long as a given condition is true

for i in range(5):
	print(i)

# String
for c in "python":
	print(c)

# list
my_list = ['Alice', 'Tobey']
for name in my_list:
	print(name)

# dictionary
my_dict = {
    'Name' : 'Alice',
    'Job': 'Software Engineer',
    'Hobby': 'Shopping'
}
# 只有key值 for default
for item in my_dict:
	print(item)
# 用items來取得key-value pair
for k, v in my_dict.items():
	print(f'key is {k} and value is {v}')
	print('key is ' + k + ' and value is ' + v)
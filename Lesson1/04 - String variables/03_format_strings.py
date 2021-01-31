# 要求使用者輸入他的姓名
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')

# capitalize()會把首字母變成大寫
# 其餘字母還是小寫
print ('Hello ' + first_name.capitalize() + ' ' \
       + last_name.capitalize())

# string formating alternative
print(f'Hello {first_name.capitalize()} {last_name.capitalize()}')
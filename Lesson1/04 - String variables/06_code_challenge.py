# 用變數(variable)來儲存輸入的英文姓(last name)
# 用變數(variable)來儲存輸入的名(first name)
# 印出全名
# 在姓和名之間加空格並印出來
# 印出首字母大寫(capitalize case)的全名
# 印出全部字母大寫(upper case)的全名
# 印出小寫(lower case)的全名
last_name = input('last name:')
first_name = input('first name:')
name=f'{last_name} {first_name}'
print(name)
name=f'{last_name.capitalize()} {first_name.capitalize()}'
print(name)
print(name.upper())
print(name.lower())
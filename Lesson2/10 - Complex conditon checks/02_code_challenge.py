# 當你進入學校/公司之後，需要製作英文名片
# 必須根據你的英文名字長度來判斷
# step 1: 要求使用者輸入英文名，存在first_name變數
# step 2: 要求使用者輸入英文姓，存在last_name變數
# stpe 3: 如果輸入的英文名長度小於5、輸入的英文姓小於5
# 印出全名
# stpe 4: 如果輸入的英文名長度大於等於5、輸入的英文姓小於5
# 印出英文名字首 + 英文名
# stpe 5: 如果輸入的英文名長度大於等於5、輸入的英文姓大於等於5
# 只印英文姓

# 請測試以下姓名
# 你的英文姓名
# Ann Yang -> Ann Yang
# Michelle Li -> M. Li
# Taylor Swift -> Swift
first_name=input('input first name:')
last_name=input('input last name:')
if len(first_name)<5 and len(last_name):
    print(f'{first_name} {last_name}')
elif (len(first_name)>=5) and (len(last_name)<5):
    print(f'{first_name[0]}. {last_name}')
else:
    print(f'{first_name}')
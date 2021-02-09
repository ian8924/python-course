# 使用方程式來畫星星！
# 1. 要求使用者輸入一個數字，存在變數裡
# 2. 定義方程式，將步驟1的數字帶入 
# 3. 呼叫方程式，在terminal印出以下圖案

# 例：使用者輸入3
# 在terminal印出(不包括 #)
# *
# **
# ***

# 例：使用者輸入5
# 在terminal印出(不包括 #)
# *
# **
# ***
# ****
# *****

def draw(num):
    for i in range(1,num+1):
        row=''
        for i in range(0,i):
            row=row+'*'
        print(row)
num= int(input('enter a number:'))
draw(num)
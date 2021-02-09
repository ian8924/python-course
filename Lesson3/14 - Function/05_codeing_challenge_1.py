# Create a calculator function
# 寫出計算方程式 def calculate(parameter...)
# 方程式接受三個變數
# first_num: 運算的第一個數字
# second_num:運算的第二個數字
# operation: 英文字串 'add' 或是 'subtract' 或是 'multiply'

# 方程式需回傳(return)兩數相加、相減或相除的結果
# 例如輸入5, 8, add
# 回傳13
# 例如輸入5, 8, subtract
# 回傳-3
# 例如輸入5, 8, multiply
# 回傳40

def calculate(first_num,second_num,operation):
    if operation=='add':
        return first_num+second_num
    elif operation=='subtract':
        return first_num-second_num
    elif operation=='multiply':
        return first_num*second_num

print(calculate(5,8,'add'))
print(calculate(5,8,'subtract'))
print(calculate(5,8,'multiply'))




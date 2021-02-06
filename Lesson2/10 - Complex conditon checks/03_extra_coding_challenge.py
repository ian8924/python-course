# 四則運算
# 1. 要求使用者輸入一個數字，存在變數1
# 2. 要求使用者輸入另一個數字，存在變數2
# 3. 要求使用者輸入運算符號(+,-,*,/)，存在變數3
# 4. 若使用者輸入運算符號無效，印出('無效運算')
num_1= int(input('input num1:'))
num_2= int(input('input num2:'))
do_what=input('enter +,-,*,/:')
if do_what=='+':
    print(f'{num_1}+{num_2}={num_1+num_2}')
elif do_what=='-':
    print(f'{num_1}-{num_2}={num_1-num_2}')
elif do_what=='*':
    print(f'{num_1}*{num_2}={num_1*num_2}')
elif do_what=='/':
    print(f'{num_1}/{num_2}={num_1/num_2}')
else:
    print('無效運算')
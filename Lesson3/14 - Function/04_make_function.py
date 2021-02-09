# sum2 = 0
# for x in range(11):
#     sum2 = sum2 + x
# print(sum2)

# sum2 = 0
# for x in range(21):
#     sum2 = sum2 + x
# print(sum2)

# def calculate():
#     sum2 = 0
#     for x in range(11):
#         sum2 = sum2 + x
#     print(sum2)

# calculate()

# mini challenge: 利用參數讓calculate方程式可以對不同輸入值做變化
def calculate (num1,num2):
    total = 0
    for x in range( num1, num2+1):
        total = total + x
    return total/2

print(calculate( 2, 5))
print(calculate( 40, 50))

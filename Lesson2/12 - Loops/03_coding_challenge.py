# 利用while loop計算1加到10
# total = 0
# x = 1
# while x < 11:
#     total = total + x
#     x = x + 1
# print(total)
# 利用for loop計算1加到10
# total = 0
# for i in range(1,11) :
#     total = total+i
# print(total)

# [10,20,30,40,50]
# 相乘結果
# total = 1
# for i in [ 10, 20, 30, 40, 50] :
#     total = total * i
# print(total)
x = 1
total = 1
while x < 6:
    total = x * 10 * total
    x = x + 1
print(total)

# 定義一個方程式square
# 方程式要輸入一個list
# 算出list裡面數字的平方和
# 印出結果在terminal
# 注意：不可以使用print

# 例子
# [1,2,3] -> 回傳14
# [10,11,12,13,14,15] -> 回傳955
# [10, 100, 1000, 10000]-> 回傳101010100
def square(list):
    total=0
    for i in list:
        total=total+i**2
    return total
print(square([1,2,3]))
print(square([10,11,12,13,14,15]))
print(square([10, 100, 1000, 10000]))
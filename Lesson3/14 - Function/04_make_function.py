sum2 = 0
for x in range(11):
    sum2 = sum2 + x
print(sum2)

sum2 = 0
for x in range(21):
    sum2 = sum2 + x
print(sum2)

def calculate():
    sum2 = 0
    for x in range(11):
        sum2 = sum2 + x
    print(sum2)

calculate()

# mini challenge: 利用參數讓calculate方程式可以對不同輸入值做變化
def calculate2(num):
    sum2 = 0
    for x in range(num+1):
        sum2 = sum2 + x
    print(sum2)

calculate2(20)

# 印出九九乘法表
for i in range(1,10):
    arr=''
    for j in range(1,10):
       arr=arr+(f'{j}*{i}={i*j} ')
    print (arr)
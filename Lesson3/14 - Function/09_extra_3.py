# 印出九九乘法表
for i in range(1,10):
    str1=''
    for j in range(1,10):
       str1=str1+(f'{j}*{i}={i*j} ')
    print (str1)
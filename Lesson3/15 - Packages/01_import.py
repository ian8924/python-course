# Modules(https://docs.python.org/3/tutorial/modules.html) 
# 用來儲存程式碼，要使用任何modules只要import便可以使用該module裡的程式碼
# Python Module Index: https://docs.python.org/3/py-modindex.html

# import math
# x = 10.47
# print(math.floor(x))
# print(math.ceil(x))
# print(math.factorial(5))

# ModuleNotFoundError: No module named 'camelcase'
# # $ pip3 install camelcase
import camelcase
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))

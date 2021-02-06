age = int(input('how old are you? '))

if age >= 18:
	# 年齡大於18歲，可以獲得10%的折扣
	discount = 0.1
else:
	# 未滿18歲，沒有任何折扣
	discount = 0

print('discount:'+str(discount))
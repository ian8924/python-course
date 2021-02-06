# 看看你究竟買不買得起iPhone
iphone_11_pro_price = float(input('How much is an iPhone 11 Pro? '))
iphone_11_price = float(input('How much is an iPhone 11? '))

# 可以用Boolen(True/False)賦予值
if iphone_11_pro_price > 999.99 and iphone_11_price > 799.99:
	can_afford = False
else:
	can_afford = True

# 可以用Boolen值來確認是否買得起iPhone
if can_afford:
	print('You can afford buy iPhone 11 Pro or iPhone 11')

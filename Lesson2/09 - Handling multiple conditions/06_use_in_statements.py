country = input('Which country were you born: ')
# 可以用in來結合多種條件
if country.lower() in ('taiwan', 'vietnam'):
	print('Covid safe')
elif country.lower() in ('us', 'china'):
	print('Covid alert')
elif country.lower() in ('uk','korea'):
	print ('Covid watch list')
else:
	print('Covid status unknown')
	
country = input('Which country were you born: ')
age = int(input('How old are you? '))

if country.lower() == 'taiwan' and age > 30:
	print('covid safe')
elif country.lower() == 'us':
	print('Covid alert')
elif country.lower() == 'japan':
	print('Covid watch list')
else:
	print('Covid status unknown!')
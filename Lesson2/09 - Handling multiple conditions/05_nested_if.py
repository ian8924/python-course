country = input('Which country were you born: ')
age = int(input('How old are you? '))

if country.lower == 'taiwan':
	if  age >= 30:
		print('Taiwan No.1!')
	elif age >= 18 and age < 30:
		print('Sad!')
	elif age < 18:
		print('Not bad!')
else:
	print('alright!')

# Dictionary用來儲存key-value pair
my_dict = {
    'Name' : 'Alice',
    'Job': 'Software Engineer',
    'Hobby': 'Shopping'
}

print(my_dict)
print(type(my_dict))
print(my_dict['Name'])
print(my_dict.get('Job'))

keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()
print(keys)
print(values)
print(items)

# More functions
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries
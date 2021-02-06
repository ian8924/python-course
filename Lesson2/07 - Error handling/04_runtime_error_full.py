x = 8
y = 0
try:
    print(x / y)
except ZeroDivisionError as e:
# except SyntaxError as e:   
    # 可以將Error印出用來Debug
    print(f'Oops! Something went wrong: {e}')
except:
    print(f'Some other erros')
finally:
    print('This line will always run')

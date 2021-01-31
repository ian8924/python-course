# 你可以對字串(string)進行不同的操作
sentence = 'I love Learning Python oh oh ya'
name = '   Alice   '

# upper() 會讓字串裡的字母都變成大寫
print(sentence.upper())

# lower() 會讓字串裡的字母都變成小寫
print(sentence.lower())

# capitalize() 會讓字串裡的第一個字母變成大寫
print(sentence.capitalize())

# count() 會計算指定字母出現在字串的次數
print(sentence.count('o'))
print(sentence.count('oh'))

# len() 會計算字串的長度
# 空格也會計算
print(len(sentence))

# strip()會將字串前後的空白刪去
print(name.strip())

# replace()
print(name.replace('A', 'Z'))
print(name.replace('Al', 'Zty'))

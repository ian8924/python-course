# 要求使用者輸入名字
# 如果字首是A或B或C開頭
# 被分配到房間ABC(Room ABC)
# 如果字首是D開頭
# 被分配到房間D(Room D)
# 如果都不是，要求使用者輸入他們的姓
# 如果字首是Y或Z開頭，被分配到房間YZ(Room YZ)
# 如果都不是，被分配到房間Other(Room Other)
full_name=input('enter your name:')
first_word=full_name[0]
if first_word.upper() in ('A','B','C'):
    print('Room ABC')
elif first_word.upper()=='D':
    print('Room D')
else:
    last_name=input('enter your last name:')
    if last_name[0].upper() in ('Y','Z'):
        print('Room YZ')
    else:
        print('Room Other')
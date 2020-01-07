def y(yen):
    yen = int(yen)
    if yen % 4 != 0:
        return False
    elif yen % 100 != 0:
        return True
    elif yen % 400 != 0:
        return False
    else:
        return True

a = y(yen=input('請輸入公元年分: '))

if a:
    print('閏年')
else:
    print('平年')

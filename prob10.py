menu = input('메뉴: ')

dict = {'오뎅':300, '순대':400, '만두':500}

if menu in dict.keys():
    print('가격: {}'.format(dict[menu]))
else:
    print('가격: 0')

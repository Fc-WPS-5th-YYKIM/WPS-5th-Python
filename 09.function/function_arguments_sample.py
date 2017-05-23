def make_gugu ( num ):
    return [(num, i, num *i) for i in range(1, 10)]

#print( make_gugu ( 3 ) )

print('--------------------------------------')

def print_gugu( print_type, gugu_list ):
    if print_type == 'simple':
        for item in gugu_list:
            print(item)
    elif print_type == 'normal':
        for x, y, z in gugu_list:
            print('{} x {} = {}'.format(x, y, z))
    else:
        print('해당하는 출력 타입이 없습니다.')

print_gugu('simple', make_gugu(3))

print('--------------------------------------')

def gugu(range_, print_type, make_gugu_function, print_gugu_function):
    for num in range_:
        print('{:=^10}'.format(' ' + str(num) + '단'))
        cur_gugu_list = make_gugu_function(num)
        print_gugu_function(print_type, cur_gugu_list)
        print('')


gugu(range(2,4), 'normal', make_gugu, print_gugu)






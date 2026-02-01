needed_potatoes = int(input('dksfjkjdslf'))
pealed_potatoes = 0

while pealed_potatoes < needed_potatoes:
    print('dlflsf')
    is_rotten = input('картошка гнилая?')
    if is_rotten == 'да':
        print('выкидаем')
        continue
    print('чистиим картошку')
    pealed_potatoes +=1
    print(f'готово! почищено :{pealed_potatoes}')
    is_tired = input ('вы устали?')
    if is_tired == 'да':
        break
else:
    print('почистить всю картошку')

print(f'Почистили {pealed_potatoes} картоплі!')





while True:
    number1 = float(input('введите первое число'))
    number2 = float(input('введите второе число'))
    action = input('выберите операцию (+, -, *, /) : ')
    
    match action:
        case '+': print(f'{number1} + {number2} = {number1 + number2}')
        case '-': print(f'{number1} - {number2} = {number1 - number2}')
        case '*': print(f'{number1} * {number2} = {number1 * number2}')
        case '/':
            if number2 == 0: print('нельзя делить на ноль')
            else: print(f'{number1} / {number2} = {number1 / number2}')
        case _: print ('некоректная операция')

q = input('Input \'q\' to quit or press Enter to continue: ')
if q == 'q':
    break
number = (input('Введите целое число: '))
while  type(number) != int:
    try:
        number = int(number)
        if number<0:
                print('Введите число от 1 до 9')
                number = (input('Введите целое число: '))
        elif number>10:
                print('Введите число от 1 до 9')
                number = (input('Введите целое число: '))
        else:
            print(number ** 2)
            number = (input('Введите целое число: '))
    except ValueError:
        print('Введите целое число: ')
        number = (input('Введите целое число: '))
        

        

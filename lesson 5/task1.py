number = int(input('Введите целое число: '))

if number == 0:
    print('нулевое число')

else:
    if number > 0:
        positive_negative = 'положительное'
        
    else:
        positive_negative = 'отрицательное'

    if number % 2 == 0:
        print(positive_negative, 'четное число')

    else:
        print(positive_negative, 'нечетное число')
        print('число не является четным')

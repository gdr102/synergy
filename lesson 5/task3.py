X = int(input('Минимальная сумма: '))
A = int(input('Сколько денег у Майкла: '))
B = int(input('Сколько денег у Ивана:'))

if A >= X and B >= X:
    print(2)

elif A >= X:
    print('Mike')

elif B >= X:
    print('Ivan')

elif A + B >= X:
    print(1)

else:
    print(0)
    
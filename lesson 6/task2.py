x = int(input('Введите натуральное число X: '))
count = 0

for i in range(1, x + 1):
    if x % i == 0:
        count = count + 1

print('Количество натуральных делителей числа', x, ':', count)

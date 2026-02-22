n = int(input('Введите количество чисел: '))
count = 0

for i in range(n):
    number = int(input('Введите число: '))
    if number == 0:
        count = count + 1

print('Количество нулей:', count)

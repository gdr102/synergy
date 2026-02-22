a = int(input('Введите число A: '))
b = int(input('Введите число B (b больше чем a): '))

print('Четные числа на отрезке от ', a, 'до', b, ':')

for i in range(a, b + 1):
    if i % 2 == 0:
        print(i, end=' ')

import random

print('Программа для сложения матриц')
print('=' * 50)

n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))

matrix_1 = []
matrix_2 = []

for i in range(n):
    row = []
    for j in range(m):
        num = random.randint(-10, 20)
        row.append(num)
    matrix_1.append(row)

for i in range(n):
    row = []
    for j in range(m):
        num = random.randint(-10, 20)
        row.append(num)
    matrix_2.append(row)

print('\nПервая матрица:')
for i in range(n):
    for j in range(m):
        print(f'{matrix_1[i][j]:4}', end=' ')
    print()

print('\nВторая матрица:')
for i in range(n):
    for j in range(m):
        print(f'{matrix_2[i][j]:4}', end=' ')
    print()

matrix_3 = []

for i in range(n):
    row = []
    for j in range(m):
        sum_element = matrix_1[i][j] + matrix_2[i][j]
        row.append(sum_element)
    matrix_3.append(row)

print('\nРезультат сложения:')
for i in range(n):
    for j in range(m):
        print(f'{matrix_3[i][j]:4}', end=' ')
    print()

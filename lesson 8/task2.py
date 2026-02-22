n = int(input('Введите количество чисел: '))

print(f'Введите {n} чисел через пробел:')
numbers_str = input().split()
numbers = []
for i in range(n):
    numbers.append(int(numbers_str[i]))

result = []
result.append(numbers[n - 1])
for i in range(n - 1):
    result.append(numbers[i])

for i in range(len(result)):
    print(result[i], end=' ')
print()

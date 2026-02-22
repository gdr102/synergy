n = int(input('Введите количество чисел:'))

numbers = []
print(f'Введите {n} чисел :')
for i in range(n):
    x = int(input())
    numbers.append(x)

reversed_numbers = []
for i in range(len(numbers) - 1, -1, -1):
    reversed_numbers.append(numbers[i])

for i in range(len(reversed_numbers)):
    print(reversed_numbers[i])

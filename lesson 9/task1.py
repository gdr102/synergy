n = int(input('введите количество чисел: '))

print('Введите числа через пробел:')
numbers_str = input().split()

unique_numbers = set()

for i in range(n):
    num = int(numbers_str[i])
    unique_numbers.add(num)

print(len(unique_numbers))

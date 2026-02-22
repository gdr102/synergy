numbers_str = input('Введите последовательность чисел: ').split()

seen_numbers = set()

for num_str in numbers_str:
    num = int(num_str)
    
    if num in seen_numbers:
        print('YES')
    else:
        print('NO')
        seen_numbers.add(num)

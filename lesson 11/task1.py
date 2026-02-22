def factorial(n):
    '''Функция для вычисления факториала числа'''
    result = 1

    for i in range(1, n + 1):
        result = result * i
        
    return result

num = int(input('Введите натуральное число: '))

fact_num = factorial(num)
print(f'Факториал числа {num} = {fact_num}')

factorials_list = []

for i in range(fact_num, 0, -1):
    factorials_list.append(factorial(i))

print('Список факториалов в убывающем порядке:')
print(factorials_list)

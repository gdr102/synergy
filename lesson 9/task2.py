print('Введите первый список чисел через пробел:')
list1_str = input().split()
list1 = []
for num in list1_str:
    list1.append(int(num))

print('Введите второй список чисел через пробел: ')
list2_str = input().split()
list2 = []
for num in list2_str:
    list2.append(int(num))

set1 = set(list1)
set2 = set(list2)

common = set()
for num in set1:
    if num in set2:
        common.add(num)

print('количество общих чисел: ')
print(len(common))

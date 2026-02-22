my_dict = {}

for num in range(10, -6, -1):
    my_dict[num] = num ** num

print('Словарь с числами и их степенями:')
for key, value in my_dict.items():
    print(f'{key}:{value}')

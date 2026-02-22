pets = {}

print('Введите информацию о питомце:')
pet_name = input('Кличка питомца: ')

pet_info = {}

pet_type = input('Вид питомца:')
pet_info['Вид питомца'] = pet_type

pet_age = int(input('Возраст питомца: '))
pet_info['Возраст питомца'] = pet_age

owner_name = input('Имя владельца: ')
pet_info['Имя владельца'] = owner_name

pets[pet_name] = pet_info

age = pet_age
if age % 10 == 1 and age % 100 != 11:
    year_word = 'год'
elif age % 10 in [2, 3, 4] and not (age % 100 in [12, 13, 14]):
    year_word = 'года'
else:
    year_word = 'лет'

pet_keys = list(pets.keys())
pet_values = list(pets.values())

first_pet_name = pet_keys[0]
first_pet_info = pet_values[0]

pet_type = first_pet_info['Вид питомца']
pet_age = first_pet_info['Возраст питомца']
owner = first_pet_info['Имя владельца']

result = f'Это {pet_type} по кличке \'{first_pet_name}\'. Возраст питомца: {pet_age} {year_word}. Имя владельца: {owner}'
print(result)

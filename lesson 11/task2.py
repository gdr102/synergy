import collections

pets = {
    1:
        {
            'Мухтар': {
                'Вид питомца': 'Собака',
                'Возраст питомца': 9,
                'Имя владельца': 'Павел'
            }
        },
    2:
        {
            'Барсик': {
                'Вид питомца': 'кот',
                'Возраст питомца': 5,
                'Имя владельца': 'Саша'
            }
        }
}

def get_suffix(age):
    '''Функция для определения правильного окончания'''
    if age % 10 == 1 and age % 100 != 11:
        return 'год'
    elif age % 10 in [2, 3, 4] and not (age % 100 in [12, 13, 14]):
        return 'года'
    else:
        return 'лет'

def get_pet(ID):
    '''Функция для получения информации о питомце по ID'''
    if ID in pets.keys():
        return pets[ID]
    else:
        return False

def pets_list():
    '''Функция для отображения всех питомцев'''
    if not pets:
        print('База данных пуста')
        return
    
    print('\nСписок всех питомцев:')
    print('-' * 40)
    for ID, pet_info in pets.items():
        pet_name = list(pet_info.keys())[0]
        details = pet_info[pet_name]
        
        print(f'ID: {ID}')
        print(f'Кличка: {pet_name}')
        print(f'Вид: {details['Вид питомца']}')
        print(f'Возраст: {details['Возраст питомца']} {get_suffix(details['Возраст питомца'])}')
        print(f'Владелец: {details['Имя владельца']}')
        print('-' * 40)

def create():
    '''Функция для создания новой записи'''
    last = collections.deque(pets, maxlen=1)[0]
    new_id = last + 1
    
    print('\nДобавление нового питомца:')
    pet_name = input('Введите кличку питомца: ')
    pet_type = input('Введите вид питомца: ')
    pet_age = int(input('Введите возраст питомца: '))
    owner_name = input('Введите имя владельца: ')
    
    pets[new_id] = {
        pet_name: {
            'Вид питомца': pet_type,
            'Возраст питомца': pet_age,
            'Имя владельца': owner_name
        }
    }
    
    print(f'Питомец {pet_name} успешно добавлен с ID {new_id}')

def read():
    '''Функция для чтения информации о питомце'''
    try:
        pet_id = int(input('Введите ID питомца: '))
    except ValueError:
        print('Ошибка: ID должен быть числом')
        return
    
    pet_info = get_pet(pet_id)
    
    if pet_info == False:
        print(f'Питомца с ID {pet_id} не найдено')
        return
    
    pet_name = list(pet_info.keys())[0]
    details = pet_info[pet_name]
    
    age = details['Возраст питомца']
    suffix = get_suffix(age)
    
    result = f'Это {details['Вид питомца']} по кличке \'{pet_name}\'. Возраст питомца: {age} {suffix}. Имя владельца: {details['Имя владельца']}'
    print(result)

def update():
    '''Функция для обновления информации о питомце'''
    try:
        pet_id = int(input('Введите ID питомца для обновления: '))
    except ValueError:
        print('Ошибка: ID должен быть числом')
        return
    
    pet_info = get_pet(pet_id)
    
    if pet_info == False:
        print(f'Питомца с ID {pet_id} не найдено')
        return
    
    pet_name = list(pet_info.keys())[0]
    details = pet_info[pet_name]
    
    print(f'\nОбновление информации о питомце {pet_name}:')
    print('(Оставьте поле пустым, чтобы не менять значение)')
    
    new_name = input(f'Новая кличка (текущая: {pet_name}): ')
    new_type = input(f'Новый вид (текущий: {details['Вид питомца']}): ')
    new_age_str = input(f'Новый возраст (текущий: {details['Возраст питомца']}): ')
    new_owner = input(f'Новый владелец (текущий: {details['Имя владельца']}): ')
    
    updated_info = {}
    
    final_name = new_name if new_name else pet_name
    
    updated_details = {}
    updated_details['Вид питомца'] = new_type if new_type else details['Вид питомца']
    
    if new_age_str:
        try:
            updated_details['Возраст питомца'] = int(new_age_str)
        except ValueError:
            print('Ошибка: возраст должен быть числом. Значение не изменено')
            updated_details['Возраст питомца'] = details['Возраст питомца']
    else:
        updated_details['Возраст питомца'] = details['Возраст питомца']
    
    updated_details['Имя владельца'] = new_owner if new_owner else details['Имя владельца']

    updated_info[final_name] = updated_details

    if final_name != pet_name:
        del pets[pet_id][pet_name]
        pets[pet_id] = updated_info

    else:
        pets[pet_id] = updated_info
    
    print(f'Информация о питомце обновлена')

def delete():
    '''Функция для удаления записи о питомце'''
    try:
        pet_id = int(input('Введите ID питомца для удаления: '))
    except ValueError:
        print('Ошибка: ID должен быть числом')
        return
    
    pet_info = get_pet(pet_id)
    
    if pet_info == False:
        print(f'Питомца с ID {pet_id} не найдено')
        return
    
    pet_name = list(pet_info.keys())[0]
    confirm = input(f'Вы уверены, что хотите удалить питомца {pet_name}? (да/нет): ')
    
    if confirm.lower() == 'да':
        del pets[pet_id]
        print(f'Питомец {pet_name} удален из базы данных')
    else:
        print('Удаление отменено')

print('Программа управления базой данных ветеринарной клиники')
print('Команды: create, read, update, delete, list, stop')

command = ''
while command != 'stop':
    print()
    command = input('Введите команду: ').lower()
    
    if command == 'create':
        create()
    elif command == 'read':
        read()
    elif command == 'update':
        update()
    elif command == 'delete':
        delete()
    elif command == 'list':
        pets_list()
    elif command == 'stop':
        print('Программа завершена')
    else:
        print('Неизвестная команда. Попробуйте снова.')

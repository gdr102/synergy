class Kass:
    '''Класс для работы с кассой'''
    
    def __init__(self, initial_money=0):
        self.money = initial_money
        print(f'Касса создана. В кассе {self.money} рублей')
    
    def top_up(self, X):
        if X <= 0:
            print('Сумма пополнения должна быть положительной!')
            return
        
        self.money += X
        print(f'Касса пополнена на {X} рублей. Теперь в кассе {self.money} рублей')
    
    def count_1000(self):
        thousands = self.money // 1000
        print(f'В кассе {thousands} целых тысяч рублей')
        return thousands
    
    def take_away(self, X):
        if X <= 0:
            print('Сумма для изъятия должна быть положительной!')
            return
        
        if X > self.money:
            print(f'Ошибка: Недостаточно денег в кассе! Требуется {X}, а в кассе только {self.money}')
            raise ValueError('Недостаточно денег в кассе')
        else:
            self.money -= X
            print(f'Из кассы взято {X} рублей. Осталось {self.money} рублей')

# Создаем кассу с начальной суммой
my_kass = Kass(5000)

# Пополняем кассу
my_kass.top_up(2500)

# Проверяем, сколько тысяч
my_kass.count_1000()

# Забираем деньги
my_kass.take_away(3000)

# Попытка забрать больше чем есть 
try:
    my_kass.take_away(10000)
except ValueError as e:
    print(f'Поймана ошибка: {e}')

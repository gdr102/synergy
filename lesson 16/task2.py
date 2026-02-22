class Cherepashka:
    '''Класс для управления черепашкой на плоскости'''
    
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s
        print(f'Черепашка создана! Позиция: ({x}, {y}), шаг: {s}')
    
    def go_up(self):
        self.y += self.s
        print(f'Черепашка пошла вверх. Новая позиция: ({self.x}, {self.y})')
    
    def go_down(self):
        self.y -= self.s
        print(f'Черепашка пошла вниз. Новая позиция: ({self.x}, {self.y})')
    
    def go_left(self):
        self.x -= self.s
        print(f'Черепашка пошла влево. Новая позиция: ({self.x}, {self.y})')
    
    def go_right(self):
        self.x += self.s
        print(f'Черепашка пошла вправо. Новая позиция: ({self.x}, {self.y})')
    
    def evolve(self):
        self.s += 1
        print(f'Черепашка эволюционировала! Теперь шаг = {self.s}')
    
    def degrade(self):
        if self.s - 1 <= 0:
            print(f'Ошибка: Нельзя уменьшить шаг! Текущий шаг {self.s} станет <= 0')
            raise ValueError('Шаг не может быть меньше или равен 0')
        else:
            self.s -= 1
            print(f'Черепашка деградировала. Теперь шаг = {self.s}')
    
    def count_moves(self, x2, y2):
        print(f'\nРасчет пути от ({self.x}, {self.y}) до ({x2}, {y2}) с шагом {self.s}')
        
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        
        print(f'Разница по x: {dx}, по y: {dy}')
        
        steps_x = (dx + self.s - 1) // self.s 
        steps_y = (dy + self.s - 1) // self.s
        
        print(f'Потребуется шагов по x: {steps_x}, по y: {steps_y}')

        total_steps = max(steps_x, steps_y)
        
        print(f'Минимальное количество действий: {total_steps}')
        return total_steps
    
    def get_position(self):
        return (self.x, self.y)
    
    def show_info(self):
        print(f'Черепашка в точке ({self.x}, {self.y}), шаг = {self.s}')

my_turtle = Cherepashka(0, 0, 1)
print('\nКоманды: up, down, left, right, evolve, degrade, moves x y, pos, exit')

while True:
    command = input('\nВведите команду: ').strip().lower()
    
    if command == 'exit':
        print('Программа завершена')
        break
    elif command == 'up':
        my_turtle.go_up()
    elif command == 'down':
        my_turtle.go_down()
    elif command == 'left':
        my_turtle.go_left()
    elif command == 'right':
        my_turtle.go_right()
    elif command == 'evolve':
        my_turtle.evolve()
    elif command == 'degrade':
        try:
            my_turtle.degrade()
        except ValueError as e:
            print(f'Ошибка: {e}')
    elif command.startswith('moves'):
        parts = command.split()
        if len(parts) == 3:
            try:
                x2 = int(parts[1])
                y2 = int(parts[2])
                my_turtle.count_moves(x2, y2)
            except ValueError:
                print('Ошибка: координаты должны быть числами')
        else:
            print('Использование: moves x y')
    elif command == 'pos':
        my_turtle.show_info()
    else:
        print('Неизвестная команда')

class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def seating_capacity(self, capacity):
        '''Метод для вывода вместимости транспортного средства'''

        return f'Вместимость одного автобуса {self.name}  {capacity} пассажиров '

class Autobus(Transport):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)
    
    def seating_capacity(self, capacity=50):
        '''Переопределенный метод с вместимостью по умолчанию 50'''

        return f'Вместимость одного автобуса {self.name} : {capacity} пассажиров '

bus = Autobus('Renaul Logan', 180, 12)

print(bus.seating_capacity())

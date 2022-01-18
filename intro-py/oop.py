class Car:
    def __init__(self, name, color, speed, direction):
        self.name = name
        self.color = color
        self.speed = speed
        self.direction = direction


    def stop(self):
        if (self.speed == 0 ):
            print("Машина стоят в месте")
    
    def go(self):
        if (self.speed > 0 ):
            print('Поехала ...') 

    def direct(self):
        if (self.direction == 'forward'):
            print('Едить вперед ...')
        elif (self.direction == 'right'):
            print('Едить направо ...')
        elif (self.direction == 'left'):
            print('Едить налево ...')
        elif (self.direction == 'back'):
            print('Едить назад ...')

class WorkCar(Car):
    def __init__(self, name, color, speed, direction):
        super().__init__(name, color, speed, direction)

    def is_workcar(self):
        print('Work Car')


class TownCar(Car):
    pass

    def is_towncar(self):
        print('Town Car')


class SportCar(Car):
    def __init__(self, name, color, speed, direction, turbo = 230):
        super().__init__(name, color, speed, direction)
        self.turbo = turbo

    def is_sportcar(self):
        print('Sport Car')


scar = SportCar('Ford', 'White', 340, 'forward')
scar.is_sportcar()
print('Name: {0}, Color: {1}, Speed: {2}, Direction: {3}, Turbo: {4}'.format(scar.name, scar.color, scar.speed, scar.direct(), scar.turbo))

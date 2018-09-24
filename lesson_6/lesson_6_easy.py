# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)
 
# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


#У нас же главный объект - машина. Значит, все остальные классы просто будут наследовать его признаки? 


class Car:

    def __init__(self, name, color = 'Red',  speed = '120', is_police = 'True'):

        print ('Создан объект типа машина')
        self.name = name
        self._color = color
        self._speed = speed
        self._is_police = is_police

    
    #Setter
    def set_color(self, new_color):
        if new_color in ('White', 'Black', 'Red', 'Green'):
            self._color = new_color
        else:
            print('Choose correct color')

    def set_speed(self, new_speed):
        if new_speed in int(60, 80, 100, 120):
            self._speed = new_speed
        else:
            print('Choose correct speed')

    def set_is_police(self, answer):
        if bool(answer) == True:
            self._is_police = answer
            print('It is police car')
        else:
            print('It is not police car')


    def go(self):
        print(self.name, ' is going')

    def stop(self):
        print(self.name, 'is stopping')

    def turn(self, direction):
        if direction in ('left', 'right'):
            self.turn = direction
            print(self.name, 'is turning', direction)
        else:
            print('choose correct direction')

car = Car('Kia', 'Red', 60, True) 
car.go()
car.stop()
car.turn('left')

class TownCar(Car):
    pass
class SportCar(Car):
    pass
class WorkCar(Car):
    pass
class PoliceCar(Car):
    pass
        

    
            
            

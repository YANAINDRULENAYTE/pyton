# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

class ChooseToyParameters:

    def __init__(self, name, color = 'Red',  type = 'Animal'):

        print ('Make our toy!')
        self.name = name
        self._color = color
        self._type = type

         #Setter
    def set_color(self, new_color):
        if new_color in ('White', 'Black', 'Red', 'Green'):
            self._color = new_color
        else:
            print('Choose correct color')

    def set_type(self, new_type):
        if new_type in ('Animal', 'Mult hero'):
            self._type = new_type
        else:
            print('Choose correct type')


    def purchase_materials(self):
        print('For', self.name, 'purchase of row materials is done!')

    def sewing(self):
        print(self.name, 'is sewed!')

    def painting(self):
        print(self.name, 'is painted!')

toy = ChooseToyParameters('Cat', 'Red', 'Animal')
toy.purchase_materials()
toy.sewing()
toy.painting()

        

    
            
            

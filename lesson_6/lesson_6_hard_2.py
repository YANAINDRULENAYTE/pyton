Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

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

       
class MakeAnimalToy(ChooseToyParameters):

    def set_type(self, new_type):
        if new_type in ('Animal'):
            self._type = new_type
        else:
             print('Your toy is not animal')


class MakeMultToy(ChooseToyParameters):

    def set_type(self, new_type):
        if new_type in ('Mult hero'):
            self._type = new_type
        else:
             print('Your toy is not Mult hero')

       
toy = MakeAnimalToy('Cat', 'Red', 'GGGG')
toy.purchase_materials()
toy.sewing()
toy.painting()
#Не получилось с двумя подклассами. Должен по идее ругаться на 'GGGG'... но нет.
    
            
            

#Задание - 1
#Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
#Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва". 

#var_1
def person_card(name, age, city):
    print(name, ',', age, 'years old, lives in', city, 'city')

person_card(name = 'Alex', age = '30', city = 'Moscow')


#var_2
name = input('Enter your name: ')
age = input('Enter your age: ')
city = input('Enter city you live: ')

def is_data_correct(name, age, city):
    if name == name.title() and city == city.title() :
        try:
            int(age)
            print(name, ',', age, 'years old, lives in ', city, 'city')
        except ValueError:
            print('Enter your age correctly!')

    else:
        print('Enter your data correctly')

is_data_correct(name, age, city)


#Задание - 2
#Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

#var_1

x = int(input('Input x: '))
y = int(input('Input y: '))
z = int(input('Input z: '))
data = (x, y, z)
print (max(data))

#var_2
data = [int(i) for i in input().split()]
print(max(data))


#Задание - 3
#Создайте функцию, принимающую неограниченное количество строковых аргументов,
#верните самую длинную строку из полученных аргументов

data = [i for i in input().split()]

def shortest_arg(*args):
    print(max(*args, key=len))

shortest_arg(data)

#А это не работает, а почему - не понимаю :((

#data = [i for i in input().split()]
#result = map(lambda args: max(*args, key=len),data)
#print(list(result))

#data = [i for i in input().split()]
#result = map(lambda x, y: x if len(x) > len(y) else y, data)
#print(list(result))


#Задание - 1 (Normal)

people = ['Alex','Kelly','Martin']
salary = [700, 600, 900]
result = zip(people, salary)
print(dict(result))
#with open('salary.txt') as file:
    #result = {}
    #for line in file:
        #a, b = line.srip().split('-')
#Не успела(((


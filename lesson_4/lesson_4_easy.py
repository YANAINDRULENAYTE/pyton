# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random
count = 10
result = [random.randint(-100,100) for _ in range(count)]
result1 = [i ** 2 for i in result]
print(result, result1)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

import random
count = 4
list = ['яблоки', 'груши', 'арбузы', 'дыни', 'персики', 'киви', 'абрикосы', 'апельсины']
list1 = [random.choice(list) for _ in range(count)]
list2 = [random.choice(list) for _ in range(count)]
print (list1, list2)
list3 = set(list1)
list4 = set(list2)
list5 = list3 & list4
print(list5)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random
count = 10
list = [random.randint(-100,100) for _ in range(count)]
print (list)
for i in (list):
    if i % 3 == 0 and  i > 0 and  i % 4 != 0:
        print (i)
        
    






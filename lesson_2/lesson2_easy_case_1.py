#lesson2_easy_case_1
fruits = ['Яблоки', 'Груши', 'Бананы', 'Арбузы', 'Дыни']
for index, fruit in enumerate (fruits, start=1):
    print(index, '{0:>10}'.format(fruit))

#lesson2_easy_case_2
lst1 = ['Яблоки', 'Груши', 'Бананы', 'Арбузы', 'Дыни', 1, 5, 555]
lst2 = [1, 345, 5, 'Груши', 98]
a = [x for x in lst1 if x not in lst2]
print (a)

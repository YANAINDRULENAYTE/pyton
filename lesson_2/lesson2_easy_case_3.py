#lesson2_easy_case_3
lst = [1, 1, 2, 3, 5, 8, 13, 21]
for x in lst:
    if x % 2 == 0:
        x = x / 4
    else:
        x = x * 2
    print(x, end = ',')
    


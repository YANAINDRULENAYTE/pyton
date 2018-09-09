#lesson2_normal_case_1
lst = (2, -5, 8, 9, -25, 25, 4)

for x in lst:
    if x > 0:
        x = x ** .5
        if (x).is_integer():
            print(x, end = ',')

        
    
    


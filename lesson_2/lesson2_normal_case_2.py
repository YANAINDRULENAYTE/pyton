#lesson2_normal_case_3
import time
while True:
    date = input('Date (dd.mm.yyyy): ')
    try:
            date = time.strptime(date, '%d.%m.%Y')
            print('Good date')
            break
    except ValueError:
            print('Invalid date!')
            continue







        
    
    


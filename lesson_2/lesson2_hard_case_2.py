#lesson2_hard_case_2
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







        
    
    


step = 10
import random 
for pop_8 in range (1,9):
    print (f'Попытка номер {pop_8}')   
    number_Pc = random.randint (1,100)
    print (number_Pc)
    res = input ()
    step = round(step/2)
    if res == '=':
        print('Ура, я победил!')
        break
    elif res == '-':
        number_Pc -= step
    else:
        number_Pc += step
else:
    print('Я проиграл...')
        
        
   


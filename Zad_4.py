import random
number_1 = random.randint (1,100)
for pop_1 in range (1,8):
    print (f'Попытка номер {pop_1}')
    user_number_1 = int(input('Введите число'))
    if user_number_1 == number_1:
        print ('Верно')
        break
    elif user_number_1 < number_1:
        print ('Число меньше загаданного')
    elif user_number_1 > number_1:
        print ('Число больше загаданного')
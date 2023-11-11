import random

while True:
    n = int(input('Введите правую границу для выбора случайного числа: '))

    num = random.randrange(0, n)

    guessing = int(input(f'Угадайте число от 1 до {n}: '))
    count = 0

    while guessing != num:
        if guessing > num:
            print('Слишком много, попробуйте еще раз')
            count += 1
            guessing = int(input(f'Угадайте число от 1 до {n}: '))
        elif guessing < num:
            print('Слишком мало, попробуйте еще раз')
            count += 1
            guessing = int(input(f'Угадайте число от 1 до {n}: '))
        else:
            break
    count += 1
    choice = input(f'Вы угадали, поздравляем! Вам потребовалось столько попыток - {count}. Хотите сыграть еще? (д = да, н = нет): ')
    
    if choice.lower() == 'н':
        break
    

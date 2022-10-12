from colorama import init
from colorama import Back,  Fore

# use Colorama to make Termcolor work on Windows too
init()

import os

FILE_NAME = 'history_buy.txt'

history_buy = []
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'r') as f:
        for order in f:
            history_buy.append(order.replace('\n', ''))

def check(count):
    print(Fore.CYAN)
    summa_count = int(input('Введите сумму на сколько пополнить счет:  '))
    summa_count += count
    history_buy.append('Пополнение счета: ')
    history_buy.append(summa_count)
    return summa_count

def buy(summa_check=0):
    while summa_check != 0:
        print(Fore.GREEN, 'Меню:')
        print('1. Вода = 50')
        print('2. Кофе = 200')
        print('3. Чай = 100')
        print('4. остаток средств на счете')
        print('5. выход')

        name_buy = input('Выберите пункт меню ')
        print(Fore.BLUE)
        if name_buy == '1':
            if 50 <= summa_check:
                summa_check = summa_check - 50
                print('Покупка: Вода, Осталось средств:', summa_check)
                history_buy.append('Покупка: Вода - 50 руб.')
            else:
                print('Недостаточно средств')
        elif name_buy == '2':
            if 200 <= summa_check:
                summa_check = summa_check - 200
                print('Покупка: Кофе, Осталось средств:', summa_check)
                history_buy.append('Покупка: Кофе - 200 руб.')
            else:
                print('Недостаточно средств. Осталось средств:', summa_check)
        elif name_buy == '3':
            if 100 <= summa_check:
                summa_check = summa_check - 100
                print('Покупка: Чай, Осталось средств:', summa_check)
                history_buy.append('Покупка: Чай - 100 руб.')
            else:
                print('Недостаточно средств')
        elif name_buy == '4':
            if 0 <= summa_check:
                print(Fore.RED)
                print('На счету:', summa_check)
                history_buy.append('Остаток средств: ')
                history_buy.append(summa_check)
        elif name_buy == '5':
            print('Отмена покупки,Осталось средств:', summa_check)

            break
        else:
            print('Неверный пункт меню')

            return

a = buy()

while True:
    print('0. Очистить список покупок')
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню')
    if choice == '0':
        f = open(FILE_NAME, 'r+')
        f.truncate()

    elif choice == '1':
        a = check(0)
    elif choice == '2':
        buy(a)
    elif choice == '3':
        print(Fore.YELLOW)
        for order in history_buy:
            print(order)
        print(history_buy)

    elif choice == '4':
        with open(FILE_NAME, 'w') as f:
            for order in history_buy:
                f.write(f'{order}\n')
        break

    else:
        print('Неверный пункт меню')

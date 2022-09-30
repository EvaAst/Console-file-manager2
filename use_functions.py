def check(count):
    summa_count = int(input('Введите сумму на сколько пополнить счет '))
    summa_count += count
    return summa_count


history_buy = []


def buy(summa_check=0):
    while summa_check != 0:
        print('1. Вода = 50')
        print('2. Кофе = 200')
        print('3. Чай = 100')
        print('4. выход')

        name_buy = input('Введите продукт')
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
                print('Недостаточно средств')
        elif name_buy == '3':
            if 100 <= summa_check:
                summa_check = summa_check - 100
                print('Покупка: Чай, Осталось средств:', summa_check)
                history_buy.append('Покупка: Чай - 100 руб.')
            else:
                print('Недостаточно средств')
        elif name_buy == '4':
            print('Отмена покупки,Осталось средств:', summa_check)
            break
        else:
            print('Неверный пункт меню')

            return


a = buy()

while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню')
    if choice == '1':
        a = check(0)
    elif choice == '2':
        buy(a)
    elif choice == '3':
        print(history_buy)
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')

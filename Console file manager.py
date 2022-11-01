import os, shutil
from colorama import init
from colorama import Fore

# use Colorama to make Termcolor work on Windows too


def color(f):
    init()

    def inner(*args, **kwargs):
        print(Fore.CYAN)
        # поведение до вызова
        print('*' * 10)
        result = f(*args, **kwargs)
        # поведение после вызова
        print('*' * 10)
        return result

    return inner

@color
def name():
    ae = 'Астапцова Евгения'
    print(ae)

while True:
    print(Fore.YELLOW)
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. выход')

    try:
        choice = input('Выберите пункт меню ')
    except Exception as e:
        print('Вы ввели не число')
        print('Введите верное число')
        print(e)

    if choice == '1': # создать папку передаем путь
        for i in range(10):
            # проверка на существование
            if not os.path.exists(f'case{i}'):
                os.mkdir(f'case{i}')
    elif choice == '2':# удалить папку
        for i in range(10):
            os.rmdir(f'case{i}')
    elif choice == '3':# Копировать папку   shutil
            shutil.copytree('case1', 'case1_copy')
    elif choice == '4':# список файлов и папок
        print(os.listdir())


    elif choice == '6':# посмотреть только папки
        list = [f for f in os.listdir() if os.path.isdir(f)]
        list.insert(0, 'dirs:')
        print(list)

        if os.path.exists('listdir.txt'):

            with open('listdir.txt', 'a') as f:
                f.write('\n')
                for order in list:
                    f.write(order + ',')

        break

    # посмотреть только файлы
    elif choice == '5':
        import os.path
        listOfFiles = [f for f in os.listdir() if os.path.isfile(f)]
        listOfFiles.insert(0, 'files:')
        #listOfFiles.
        print(listOfFiles)
        if os.path.exists('listdir.txt'):

            with open('listdir.txt', 'a') as f:

                for order in listOfFiles:
                    f.write(order + ',')
        break
    # просмотр информации об операционной системе
    elif choice == '7':
        print(os.name)
    # 8. создатель программы
    elif choice == '8':
        ae = name()
    elif choice == '9':
        import viktorina
        viktorina
    elif choice == '10':
        import use_functions
        use_functions
    elif choice == '11':

            f = open('listdir.txt', 'r+')
            f.truncate()
            break

    else:
        print('Неверный пункт меню')

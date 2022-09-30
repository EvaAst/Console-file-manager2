import os, shutil

while True:
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

    choice = input('Выберите пункт меню ')

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
    elif choice == '5':# посмотреть только папки
        list = [f for f in os.listdir() if os.path.isdir(f)]
        print(list)
    # посмотреть только файлы
    elif choice == '6':
        import os.path
        listOfFiles = [f for f in os.listdir() if os.path.isfile(f)]
        print(listOfFiles)
    # просмотр информации об операционной системе
    elif choice == '7':
        print(os.name)
    # 8. создатель программы
    elif choice == '8':
        print('Астапцова Евгения')
    elif choice == '9':
        import viktorina
        viktorina
    elif choice == '10':
        import use_functions
        use_functions
    elif choice == '11':
        break
    else:
        print('Неверный пункт меню')
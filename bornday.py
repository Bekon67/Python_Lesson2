#  вложенный оператор if-else

bornyear = int(input('Привет, ты знаешь в каком году родился Пушкин?\n'))
if bornyear == 1799:
    bornday = input('А в какой день?\n')
    if bornday == '6 июня':
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год рождения')

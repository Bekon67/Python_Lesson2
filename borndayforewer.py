#  Циклы while

bornyear = 1799
bornmonth = 'июнь'
bornday = 6
answer = int(input('Привет, ты знаешь в каком году родился Пушкин?\n'))
while answer != 1799:
    if answer < bornyear:
        print('Ты ошибся. Пушкин родился позже. Попробуй еще раз!')
        answer = int(input())
    else:
        print('Ты ошибся. Пушкин родился раньше. Попробуй еще раз!')
        answer = int(input())

answer = input('Правильно! А какой месяц рождения? Введи прописью с маленькой буквы:\n')
while answer != bornmonth:
    print('Ты ошибся. Попробуй еще раз!')
    answer = input()

answer = int(input('Правильно! А какого числа?\n'))
while answer != 6:
    if answer < 1 or answer > 30:
        print('Ты ошибся.Такой даты в июне нет. Попробуй еще раз!')
        answer = int(input())
    elif answer < bornday:
        print('Ты ошибся. Пушкин родился позже. Попробуй еще раз!')
        answer = int(input())
    else:
        print('Ты ошибся. Пушкин родился раньше. Попробуй еще раз!')
        answer = int(input())

print('Bерно')

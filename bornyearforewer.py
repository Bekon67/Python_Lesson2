#  оператор while

bornyear = 1799
answer = int(input('Привет, ты знаешь в каком году родился Пушкин?\n'))
while answer != 1799:
    if answer < bornyear:
        print('Ты ошибся. Пушкин родился позже. Попробуй еще раз!')
        answer = int(input())
    else:
        print('Ты ошибся. Пушкин родился раньше. Попробуй еще раз!')
        answer = int(input())
print('Bерно')

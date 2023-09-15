# Библиотека random, импортируем модуль choice
from random import choice

# Допустим, что это - подбираемый пароль
correctPassword = "3444"

# Предположим, что пароль состоит только из цифр
pass_symbols = '0123456789'


# Функция "рандомного перебора"
def random_perebor():
    pass_ne_ugadan = True  # Переменная для цикла while
    wrongPasswords = []  # Список неверных паролей

    # Цикл перебора
    while pass_ne_ugadan:
        password = ''
        for i in range(len(correctPassword)):
            password += choice(pass_symbols) # К пустой переменной password добавляются случайные символы
        if password not in wrongPasswords:
            if password != correctPassword:
                wrongPasswords.append(password)
            else:
                pass_ne_ugadan = False
                break
    print(f'Программа подобрала пароль "{password}" c {len(wrongPasswords)} попытки.')

# Запуск функции
random_perebor()
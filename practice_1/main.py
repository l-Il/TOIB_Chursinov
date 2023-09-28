""" Чурсинов, ББМО-01-23, Вариант 6 """

# Импорт нужных библиотек
from itertools import product
from string import digits, ascii_letters
from random import sample

# В пароле будут все символы (Заглавные, обычные буквы + цифры)
characters = ascii_letters + digits


# Функция генерации пароля
def password_generation(password_length):
    return ''.join(sample(characters, password_length))


# Функция "подбора" "перебора" пароля
def password_bruteforce(password_length):  # На вход функция принимает длину предполагаемого пароля
    tries = 0  # Счётчик попыток
    for guess in product(characters, repeat=password_length):
        guessed_password = ''.join(guess)  # Наш предполагаемый пароль
        if our_password != guessed_password:  # Если пароль не подходит
            tries += 1  # Кол-во попыток увеличивается на одну
        else:
            break  # Иначе программа выходит из цикла
    return guessed_password, tries  # Функция возвращает полученный пароль, и кол-во попыток


print('Для чистоты эксперимента, будем генерировать случайный пароль.')
print('Чем длиннее пароль, тем дольше время выполнения программы...')
a = int(input('Введите длину пароля: '))
our_password = password_generation(a)
print('Пароль сгенерирован, начинается процесс подбора...')
b, c = password_bruteforce(a)
print(f'Программа подобрала пароль "{b}" c {c} попытки.')

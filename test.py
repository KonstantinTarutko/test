"""Задание 1.

Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.

Пример:
Ведите ваше имя: Василий
Ведите ваш пароль: vas
Введите ваш возраст: 45
Ваши данные для входа в аккаунт: имя - Василий, пароль - vas, возраст - 45"""

user_name = str(input("Ведите ваше имя: "))
user_password = str(input("Ведите ваш пароль: "))
user_age = int(input("Введите ваш возраст: "))
print(f"ваше имя - {user_name}, ваш пароль - {user_password}, ваш возраст - {user_age}")

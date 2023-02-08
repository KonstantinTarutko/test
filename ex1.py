
"""1. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень"""

"""первый вариант"""
month = int(input("Введите месяц в виде целого числа: "))

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for i in list_1:
    if month == 1:
        print("Зима")
    elif i in list_1:
        if month == 2:
            print("Зима")
        elif i in list_1:
            if month == 3:
                print("Весна")
            elif i in list_1:
                if month == 4:
                    print("Весна")
                elif i in list_1:
                    if month == 5:
                        print("Весна")
                    elif i in list_1:
                        if month == 6:
                            print("Лето")
                        elif i in list_1:
                            if month == 7:
                                print("Лето")
                            elif i in list_1:
                                if month == 8:
                                    print("Лето")
                                elif i in list_1:
                                    if month == 9:
                                        print("Осень")
                                    elif i in list_1:
                                        if month == 10:
                                            print("Осень")
                                        elif i in list_1:
                                            if month == 11:
                                                print("Осень")
                                            elif i in list_1:
                                                if month == 12:
                                                    print("Зима")
                                                    
 

"""ниже второй вариант, но сравнение через & не получилось, к сожалению, реализовать"""
"""month = int(input("Введите месяц в виде целого числа: "))

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]
list_4 = [10, 11, 12]


if month > 0:
    if month < 4:
        print("Зима")

elif month > 3:
    if month < 7:
        print("Весна")

elif month > 6:
    if month < 10:
        print("Лето")

elif month > 9:
    if month < 13:
        print("Осень")

else:
        print("Введено некорректное число")"""


dict = {'Зима':  [12, 1, 2],
              'Весна': [3, 4, 5],
              'Лето':  [6, 7, 8],
              'Осень': [9, 10, 11]}

month = int(input('Введите месяц в виде целого числа: '))
if month in range(1, 13):
    for i in dict.items():
        if month in i[1]:
             print(f'{i[0]}')
else:
    print('Введен некорректный номер месяца!')

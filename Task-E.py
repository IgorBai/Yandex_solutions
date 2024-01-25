# Задача E. Расселение спортсменок. Условие задачи под кодом, внизу. 
# (Источник: Тренировочный контест Яндекса)

# Принцип решения. 
# Массив с численностью команд храним как список. Массив комнат храним в списке парами  
# "вместимость, количество", иначе если распаковать в обычный список - на 60-м тесте 
# не хватает памяти. Для распаковки этого массива потребуется функция-итератор. Расселять
# будем, предварительно отсортировав команды и комнаты по убыванию, так код проще и быстрее.

import sys


def line2list():  # для считывания из консоли строк и преобразования их в списки int
    return [int(i) for i in sys.stdin.readline().split()]


def room_iter():  # на 60-м тесте не хватает памяти, поэтому комнаты распаковываем итератором
    for item in rooms:  # перебираем пары вместимость-количество
        for _ in range(item[1]):  # воспроизводим цикл для количеств одинаковых комнат
            yield item[0]  # возвращаем вместимость текущей комнаты и ждём след. запрос


def arrange(teams):  # функция расселения
    global r_number  # общее количество комнат опускаем внутрь функции
    if len(teams) > r_number:  # если команд больше, чем комнат -
        return 'No'  # возвращаем отрицательный ответ

    r = room_iter()  # так надо, чтобы дальше вычитывать итератор комнат
    for men in teams:  # перебираем команды, начиная с самой большой
        if men > next(r):  # если в команде людей больше, чем вместимость ситерированной комнаты
            return 'No'  # возвращаем отрицательный ответ

    return 'Yes'  # ну а если дошли до этой точки, то всё хорошо, расселить можно


commands = line2list()[0]  # число команд спортсменов
people = line2list()  # список из численностей команд

room_types = line2list()[0]  # количество типов комнат (тип и вместимость синонимы)
rooms = []  # массив для записи информации о доступных комнатах
r_number = 0  # счётчик комнат
for _ in range(room_types):  # перебираем типы комнат
    a, b = line2list()  # считываем пары "вместимость, количество комнат"
    rooms.append((a, b))  # комнаты храним "не распакованными", иначе ошибка memory limit
    r_number += b  # комнаты считаем прямо здесь, не отходя от кассы

people.sort(reverse=True)  # команды сортируем по убыванию численности
rooms.sort(reverse=True, key=lambda x: x[0])  # аналогично с запакованным массивом комнат

print(arrange(people))  # вызываем функцию расселения и печатаем её ответ

exit(0)  # формальность


# Условие задачи
#
# Спортивная школа по синхронному плаванию «Золотая рыбка» приехала в детский лагерь «Радость»  
# для проведения летних сборов.
# Прежде всего вожатым требуется расселить спортсменок по комнатам. Главный тренер предложил для 
# расселения следующее правило: в комнату заселяют всю команду целиком и больше никого другого.  
# Всего приехало n команд спортсменок.
# Количество комнат заданной вместимости в лагере ограничено. Определите, получится ли у вожатых 
# расселить детей?

# Формат ввода
# В первой строке задано число n – число команд спортсменок. Во второй строке записаны n чисел 
# ai — количество количество спортсменок в i-й команде.
# Далее следует число k – количество типов комнат, и k пар вида вместимость комнаты, количество 
# таких комнат.
# Все числа во входных данных положительные целые и не превосходят 10000.
#
# Формат вывода
# Выведите Yes, если у вожатых получится расселить спортсменок, и No, если не получится.
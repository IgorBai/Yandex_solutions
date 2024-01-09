# Задача C. Футбол. Условие задачи под кодом, внизу. 
# (Источник: Тренировочный контест Яндекса)


import sys
from collections import defaultdict


def line_int():  # для построчного считывания данных из консоли
    return [int(i) for i in sys.stdin.readline().split()]


n_sotr, n_igr = line_int()  # число сотрудников и количество игр  

h = defaultdict(int)  # словарь для хранения результатов игр каждого сотрудника
h = {ind: 0 for ind in range(n_sotr)}  # без раздачи нулей бывает, PyCharm сбоит, хотя не должен

cnt = 0  # счётчик, в нём будет результат

for i in range(n_igr):  # считываем данные очередной игры
    gol1, gol2 = line_int()
    ids = line_int()
    res = gol1 - gol2

    if 0 not in ids:  # если 0 не в ids, можно посчитать до, после и дифференциал добавить
        before = 0  # посчитали до
        h0 = h[0]  # немного сэкономим времени, введя переменную
        for id in ids:
            if h[id] > h0:
                before += 1

        for id in ids[:5]:  # записали участникам матча новые данные
            h[id] += res
        for id in ids[5:]:
            h[id] -= res

        after = 0  # посчитали после
        h0 = h[0]
        for id in ids:  # экономим время, сравниваем только внутри ids (по сыгравшим)
            if h[id] > h0:
                after += 1

        cnt = cnt + after - before  # старое значение плюс дифференциал
        print(cnt)  # выводим ответ

    else:  # если 0 в ids, то считать надо по всей базе, т.е. по всем h
        cnt = 0
        for id in ids[:5]:
            h[id] += res
        for id in ids[5:]:
            h[id] -= res
        for id in h:  # сравниваем по всем h
            h0 = h[0]
            if h[id] > h0:
                cnt += 1
        print(cnt)  # выводим ответ

exit()



# Условие задачи
#
# Сотрудники Яндекса любят играть в мини-футбол по выходным. В каждом матче играют две команды
# по 5 человек. Состав на игру в каждую команду выбирается случайно равновероятно из всех сотрудников Яндекса.
#
# Аркадий ведет статистику всех игр. Он записывает состав каждой команды и финальный счет игры. Кроме этого,
# он ведет статистику каждого игрока по разнице мячей: каждому игроку матча добавляется разница мячей команды,
# в составе которой он играл. Разница мячей считается как число голов cвоей команды минус число голов
# противоположной команды. Изначально статистика по разнице мячей для каждого игрока равна 0.
#
# Помогите Аркадию понять его прогресс в сезоне. После каждого матча нужно посчитать количество игроков с
# разницей мячей больше, чем у Аркадия.
#
# Формат ввода
# В первой строке записано два числа: N (10 ≤ N ≤ 10000) - число сотрудников, M (1 ≤ M ≤ 100000) — число 
# футбольных
# матчей. Затем следуют результаты каждого матча.
# В первой строке каждого матча записано два числа, gA, gB (0 ≤ gA, gB ≤ 20) — количество голов, которые забили
# команды A и B.
# Во второй строке каждого матча записаны десять чисел pi (0 ≤ pi < N) — id сотрудников, участвовавших в матче.
# Первые пять - состав команды A, вторые пять - состав команды B.
# Гарантируется, что составы команд для каждого матча выбирались случайно равновероятно.
# У Аркадия id всегда равно 0.
#
# Формат вывода
# Для каждого футбольного матча выведите одно целое число — количество игроков с разницей мячей больше, чем 
# у Аркадия.

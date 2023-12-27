# Задача C. Футбол. Условие задачи под кодом, внизу. 
# (Источник: Тренировочный контест Яндекса)


import sys


def line_int():
    return [int(i) for i in sys.stdin.readline().strip().replace('  ', ' ').split()]


n_sotr, n_igr = line_int()

h = dict()
for i in range(n_igr):
    gol1, gol2 = line_int()
    ids = line_int()
    res = gol1 - gol2

    sered = int(len(ids)/2)  # вдруг в командах не по 5 человек
    for id in ids[:sered]:   # строки ниже пока оставил в "классическом" виде
        if id in h:
            h[id] += res
        else:
            h[id] = res
    for id in ids[sered:]:
        if id in h:
            h[id] -= res
        else:
            h[id] = -res

    cnt = 0
    # for id in h:  # сравниваем по всем сыгравшим
    for id in ids:  # сравниваем только внутри игроков этого матча
        if h[id] > h[0]:
            cnt += 1
    #print(ids)
    #print(dict(sorted(h.items())))
    print(cnt)



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

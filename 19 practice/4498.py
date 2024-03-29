# (№ 4498) (А. Богданов) Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит две кучи
# камней. Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может добавить в одну из
# куч 1 или 2 камня. Игра завершается в тот момент, когда в сумме в кучах будет 13 камней. Победителем
# считается игрок, сделавший последний ход. В начальный момент в первой куче было 3 камня, во второй – S камней, 1 ≤ S ≤ 9.
# Ответьте на следующие вопросы:
#   Вопрос 1. Петя мог выиграть первым ходом, но сделал неудачный ход и Ваня выиграл. При каком минимальном значении S это возможно?
#   Вопрос 2. Найдите минимальное и максимальное значения S, при которых Петя выигрывает вторым ходом при любом ходе Вани.
#   Вопрос 3. Найдите значение S, при котором Ваня выигрывает вторым ходом при любых ходах Пети.
def f(x, y, p):
    if x + y >= 13 and p == 4:
        return 1
    elif x + y >= 13 and p != 4:
        return 0
    elif x + y < 13 and p >= 4:
        return 0
    else:
        if p % 2 == 1:
            return f(x + 1, y, p + 1) or f(x + 2, y, p + 1) or f(x, y + 1, p + 1) or f(x, y + 2,
                                                                                       p + 1)
        else:
            return f(x + 1, y, p + 1) and f(x + 2, y, p + 1) and f(x, y + 1, p + 1) and f(x, y + 2,
                                                                                          p + 1)


for i in range(1, 10):
    if f(3, i, 0):
        print(i)

for x in range(1, 22):
    slog1 = (x * (22 ** 4)) + (2 * (22 ** 3)) + (3 * (22 ** 2)) + (x * 22) + 5
    for y in range(13):
        slog2 = (6 * (13 ** 4)) + (7 * (13 ** 3)) + (y * (13 ** 2)) + (9 * 13) + y
        virash = slog1 - slog2
        if virash % 57 == 0:
            print(virash / 57)

# берем первое значение

for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = not(x == (not(z))) or ((x or w)==y)
                if f == 0:
                    print(x, w, y, z)
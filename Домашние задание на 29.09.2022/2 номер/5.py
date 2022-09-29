for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = not(x== (not(y))) or ((x and w)==z)
                if f == 0:
                    print(y, z, x, w)
for x in range(2):
    for y in range(2):
        for z in range(2):
            f = (not x or y or z) and (not x or not y or z) and (x or not y or not z)
            print(x, z, y, f)

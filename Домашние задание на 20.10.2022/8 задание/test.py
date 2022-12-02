for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = x or ((z<=w)<=(w==y))
                if f == 0:
                    print(w, y, x, z)

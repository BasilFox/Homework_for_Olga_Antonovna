for x1 in range(2):
    for x2 in range(2):
        for x3 in range(2):
            for x4 in range(2):
                for x5 in range(2):
                    for x6 in range(2):
                        for x7 in range(2):
                            for x8 in range(2):
                                f1 = x1 and not x2 and x3 and not x4 and x5 and x6 and x7 and not x8
                                # f2 = x1 or x2 or x3 or not x4 or not x5 or not x6 or x7 or x8
                                f3 = not x1 and x2 and not x3 and x4 and x5 and not x6 and x7 and not x8
                                # f4 = x1 or not x2 or not x3 or not x4 or not x5 or not x6 or x7 or not x8
                                if f1 is True and x3 == 0 and x7 == 1:
                                    print('first')
                                if f3 is True and x3 == 0 and x7 == 1:
                                    print('third')

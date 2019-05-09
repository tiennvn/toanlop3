#!/usr/bin/env python3
import time


def solve():

    consider_1 = []
    for b in range(1, 10):
        for c in range(1, 10):
            for g in range(1, 10):
                for h in range(1, 10):
                    for i in range(1, 10):
                        for e in range(1, 10):
                            cal_1 = 87 - ((13 * b) / c +
                                          (g * h) / i + 12 * e)
                            if cal_1 % 1 == 0 and -9 <= cal_1 <= 17:
                                consider_1.append(cal_1)
    consider_1_true = []
    result = 0
    for consider in consider_1:
        if consider not in consider_1_true:
            count_consider = 0
            count_consider_2 = 0
            for a in range(1, 10):
                for d in range(1, 10):
                    for f in range(1, 10):
                        if a + d - f - consider == 0:
                            count_consider_2 = count_consider_2 + 1
                            if consider not in consider_1_true:
                                consider_1_true.append(consider)
                                count_consider = consider_1.count(consider)
            if count_consider_2 is not 0:
                result = result + (count_consider_2 * count_consider)

    return result


def main():
    start = time.time()
    print(solve())
    print('Time =', time.time() - start)


if __name__ == "__main__":
    main()

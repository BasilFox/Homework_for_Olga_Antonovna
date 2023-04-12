import sys
sys.setrecursionlimit(2000)
def f(n):
    if n >= 10000:
        return n
    elif n % 3 == 0 and n < 10000:
        return n + f(n / 3)
    else:
        return 2*n+f(n+3)
print(f(999)-f(46))

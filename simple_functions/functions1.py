from functools import lru_cache

__all__ = ['my_sum', 'factorial','sin_series']


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


@lru_cache(maxsize=None)  # Note: -> @cache in python >= 3.9
def factorial(n):
    return n * factorial(n-1) if n else 1


def calc_part(x,n):
    return (x**(2*n+1))*((-1)**n)/(factorial(2*n+1))


def sin_series(x):
    lsit_series=[calc_part(x,n) for n in range(50)]
    return my_sum(lsit_series)
    


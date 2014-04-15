# -*- coding: utf-8 -*-
"""
Solution to question 12

Nicholas Staples
2014-04-15

"""

from utils.include_decorator import include_decorator


def gen_tri_num():
    prev = 1
    cur = 3
    yield prev
    yield cur
    while True:
        nxt = (cur - prev) + 1 + cur
        yield nxt
        prev = cur
        cur = nxt


# Common function to determine the number factors for any given number
def factors(n):
    return set(
        reduce(
            list.__add__,
            ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


@include_decorator(12)
def problem_12_solution():
    # Triangle numbers have a pattern in them
    # so if you know the prev two numbers you can work out the next number
    # 6, 10 -> (the difference between 6 and 10 is 4 so the next number will 10 + 5) 15
    # There is an increasing difference in the numbers, we can write a generator
    # to produce the next triangle number
    gen = gen_tri_num()
    n = next(gen)
    while len(factors(n)) < 500:
        n = next(gen)
    print n
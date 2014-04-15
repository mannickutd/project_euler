# -*- coding: utf-8 -*-
"""
Solution to question 5

Nicholas Staples
2014-04-15

"""

from utils.include_decorator import include_decorator


@include_decorator(5)
def problem_5_solution():
    # Trick **
    # since we know that 2520 is evenly divisible by
    # the first 10 integers, we know that the number in question is a
    # multiple of 2520. So we start with 2520 and increment by that much
    # until we find the smallest number that is evenly divisible by the
    # first 20 integers (1-20).
    x = 2520
    res = None
    while not res:
        if all(x % n == 0 for n in range(1, 20)):
            res = x
        x += 2520
    print res

# -*- coding: utf-8 -*-
"""
Description of question 1

Nicholas Staples
2014-04-14

"""

from utils.include_decorator import include_decorator


description = '''
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''


@include_decorator(1)
def problem_1():
    print description

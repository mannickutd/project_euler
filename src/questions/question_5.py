# -*- coding: utf-8 -*-
"""
Description of question 5

Nicholas Staples
2014-04-15

"""

from utils.include_decorator import include_decorator


description = '''
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?
'''


@include_decorator(5)
def problem_5():
    print description

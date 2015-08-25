# -*- coding: utf-8 -*-
"""
Description of question 15

Nicholas Staples
2015-08-24

"""

from utils.include_decorator import include_decorator


description = '''
Starting in the top left corner of a 2*2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''


@include_decorator(15)
def problem_15():
    print description

# -*- coding: utf-8 -*-
"""
Solution to question 6

Nicholas Staples
2014-04-15

"""

from utils.include_decorator import include_decorator


@include_decorator(6)
def problem_6_solution():
	print sum(x for x in range(1, 101))**2 - sum(x**2 for x in range(1, 101))
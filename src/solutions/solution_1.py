# -*- coding: utf-8 -*-
"""
Solution to question 1

Nicholas Staples
2014-04-14

"""

from utils.include_decorator import include_decorator


@include_decorator(1)
def problem_1_solution():
	print sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0])
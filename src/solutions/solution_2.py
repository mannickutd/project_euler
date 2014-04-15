# -*- coding: utf-8 -*-
"""
Solution to question 2

Nicholas Staples
2014-04-14

"""

from utils.include_decorator import include_decorator

def gen_fib():
	yield 1
	yield 2
	prev = 2
	total = 3
	while total < 4000000:
		yield total
		prev_total = total
		total = prev_total + prev
		prev = prev_total


@include_decorator(2)
def problem_2_solution():
	print sum([x for x in gen_fib() if x % 2 == 0])
# -*- coding: utf-8 -*-
"""
Solution to question 3

Nicholas Staples
2014-04-14

"""

from utils.include_decorator import include_decorator


def get_max_prime(num):
	n = num
	i = 2
	while i * i < n:
		while n % i == 0:
			n = n / i
		i = i + 1
	return n


@include_decorator(3)
def problem_3_solution():
	print get_max_prime(600851475143)

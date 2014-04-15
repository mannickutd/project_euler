# -*- coding: utf-8 -*-
"""
Solution to question 9

Nicholas Staples
2014-04-15

"""

from utils.include_decorator import include_decorator


@include_decorator(9)
def problem_9_solution():
	# Brute force use an if statement to check both equations at the same time
	# because we know the value of c We also know that a < b < c
	# We know c = 1000 - (a + b)
	# so basically c < 1000
	# That limits the brute force but still a nasty brute force
	c = 0
	a = 0
	b = 0
	for m in range(1, 1000):
		for n in range(1, 1000):
			val = 1000 - (m + n)
			if m**2 + n**2 == val**2:
				c = val
				a = m
				b = n
				break
		if c:
			break
	print a*b*c
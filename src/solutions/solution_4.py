# -*- coding: utf-8 -*-
"""
Solution to question 4

Nicholas Staples
2014-04-14

"""

from utils.include_decorator import include_decorator


def is_pal(n):
   return int(str(n)[::-1]) == n


@include_decorator(4)
def problem_4_solution():
	# is_pal is a nice way to check if its a palindrome.
	# because we are compare an int we can just reverse
	# it after converting to and from an int.
	maxPal = 0
	for a in range(999,99,-1):
	   for b in range(a,99,-1):
	      product = a*b
	      if is_pal(product) and product > maxPal:
	         maxPal = product
	print maxPal

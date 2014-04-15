# -*- coding: utf-8 -*-
"""
Solution to question 7

Nicholas Staples
2014-04-15

"""

from utils.include_decorator import include_decorator

# Generator for primes.
# Not a particulary quick one but for small primes it is fine.
# If you are consistently looking for prime numbers you would probably
# generate them once and then refer to that list. Or there is
# better algorithms to solve repeated look ups for primes.
def gen_prime():
	yield 1
	yield 2
	x = 3
	while True:
		for y in range(2, x):
			if x % y == 0:
				break
		else:
			yield x
		x += 1

@include_decorator(7)
def problem_7_solution():
	gen = gen_prime()
	print [next(gen) for __ in range(10002)][-1]
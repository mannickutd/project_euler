# -*- coding: utf-8 -*-
"""
Solution to question 10

Nicholas Staples
2014-04-15

"""

from utils.include_decorator import include_decorator
from solutions.solution_7 import gen_prime


def bf_sum_primes(n):
	'''
	Brute force to sum all primes up to n.
	'''
	res = 0
	gen = gen_prime()
	prime = next(gen)
	while prime < n:
		res += prime
		prime = next(gen)


@include_decorator(10)
def problem_10_solution_1():
	print "This is the brute force algorithm."
	print bf_sum_primes(2000000)


def soe(n):
	lst = range(2, n)
	p = 2
	while p**2 <= n:
		lst = [x for x in lst if x == p or x % p != 0]
		p += 1
	return lst


@include_decorator(10)
def problem_10_solution_2():
	print "Sieve of Eratosthenes algorithm."
	# Steps
	# 1. Create a list l of consecutive integers {2,3, ... ,N}.
	# 2. Select p as the first prime number in the list, p=2.
	# 3. Remove all multiples of p from the l.
	# 4. set p equal to the next integer in l which has not been removed.
	# 5. Repeat steps 3 and 4 until p2 > N, all the remaining numbers in the list are primes
	print sum(soe(2000000))


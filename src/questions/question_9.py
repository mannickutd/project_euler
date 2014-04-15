# -*- coding: utf-8 -*-
"""
Description of question 9

Nicholas Staples
2014-04-15

"""

from utils.include_decorator import include_decorator


description = '''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc?
'''

@include_decorator(9)
def problem_9():
	print description
# -*- coding: utf-8 -*-
"""
Description of question 10

Nicholas Staples
2014-04-15

"""

from utils.include_decorator import include_decorator


description = '''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million?
This brute force algorithm takes too long.
'''


@include_decorator(10)
def problem_10():
    print description
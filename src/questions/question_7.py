# -*- coding: utf-8 -*-
"""
Description of question 7

Nicholas Staples
2014-04-15

"""

from utils.include_decorator import include_decorator


description = '''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.
What is the 10001st prime number?
'''


@include_decorator(7)
def problem_7():
    print description

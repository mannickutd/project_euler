# -*- coding: utf-8 -*-
"""
Description of question 3

Nicholas Staples
2014-04-14

"""

from utils.include_decorator import include_decorator


description = '''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''


@include_decorator(3)
def problem_3():
    print description

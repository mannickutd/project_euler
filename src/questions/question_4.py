# -*- coding: utf-8 -*-
"""
Description of question 4

Nicholas Staples
2014-04-14

"""

from utils.include_decorator import include_decorator


description = '''
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2 digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3 digit numbers?
'''


@include_decorator(4)
def problem_4():
    print description

# -*- coding: utf-8 -*-
"""
Solution to question 15

Nicholas Staples
2015-08-24

"""
import math
from utils.include_decorator import include_decorator

# Grid size
N = 20


@include_decorator(15)
def problem_15_solution():
    '''
    The amount of lattice paths through a 20*20 grid?
    Stumbling upon the algorithm solution simplified the
    mathematics enormously.

    http://joaoff.com/2008/01/20/a-square-grid-path-problem/

    Basically it comes down to an equation

    '''
    print math.factorial((2 * N))/(math.factorial(N) * math.factorial(N))

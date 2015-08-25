# -*- coding: utf-8 -*-
"""
Solution to question 14

Nicholas Staples
2015-08-24

"""
from utils.include_decorator import include_decorator


def calculate_next_chain_number(n):
    '''
    if n is even:
        next = n/2
    else
        next = 3n + 1
    '''
    if n == 0:
        raise Exception("n should never be zero.")
    elif n % 2 == 0:
        return n/2
    else:
        return 3 * n + 1


@include_decorator(14)
def problem_14_solution():
    '''
    From the little research I have done on the problem, I haven't been able to find
    a function which can be used to determine a chain length. However we do know that
    chains length doesn't have to be calculated to the end if we encounter a number in
    the chain that we have already calculated that chain. So we will record for each
    number its chain until zero and then store that length in a dictionary which can
    be used for further chain calculations.
    '''
    longest_chain = 0
    longest_chain_number = 0
    chain_dict = {}
    for n in range(1, 1000001):
        # Include the number in the chain
        count = 1
        next = n
        while next != 1:
            next = calculate_next_chain_number(next)
            if next in chain_dict:
                count += chain_dict[next]
                break
            else:
                count += 1
        chain_dict[n] = count
        if count > longest_chain:
            longest_chain = count
            longest_chain_number = n
    print longest_chain, longest_chain_number

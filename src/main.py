# -*- coding: utf-8 -*-
"""
Main file

Nicholas Staples
2014-04-14

"""
import sys
import signal

from utils.include_decorator import (
    available, questions_available, solutions_available)
from utils.solution_exception import SolutionException

import time
import argparse

from questions import *
from solutions import *


__choices = ['question', 'all'] 


def boolean(string):
    string = string.lower()
    if string in ['0', 'f', 'false', 'no', 'off']:
        return False
    elif string in ['1', 't', 'true', 'yes', 'on']:
        return True
    else:
        raise ValueError()


def timeout(signum, frame):
    raise SolutionException("60 seconds timeout has expired.")


def run_solution(question_num):
    '''
    Run the solution function.
    '''
    signal.signal(signal.SIGALRM, timeout)
    if question_num in solutions_available():
        for i, sol in enumerate(solutions_available()[question_num]):
            print "Solution {0}".format(i)
            t0 = time.clock()
            try:
                signal.alarm(61)
                sol()
            except SolutionException, e:
                print e.message
            except Exception, e:
                print "Unknown Exception occurred while running solution."
            finally:
                signal.alarm(0) 
            print "Question {0} solved in {1} seconds".format(
                question_num, (time.clock() - t0))
    else:
        print "There is no solution...."


def run_question(question_num):
    '''
    Run the question function.
    '''
    if question_num in questions_available():
        questions_available()[question_num]()


def run_question_solution(
    question_lst, questions=False, solutions=False
):
    '''
    For every question number in <question_lst> print out the question and
    run the solution.
    The <question_lst> will be ordered to output responses in order.
    If <questions> is set then the questions will be printed out.
    If <solutions> is set then the solutions will be printed out.
    Each solution will be timed to see how long it takes to compute the
    answer.
    '''
    for q in question_lst:
        print "\nQuestion {0}".format(q)
        print "-" * 10
        if not questions and not solutions:
            print "No question and no solution for question {0}".format(q)
        else:
            if questions:
                run_question(q)
            if solutions:
                run_solution(q)
        print "-" * 10


def parse_question_args():
    '''
    Parse command line arguments for outputting a question.
    '''
    parser = argparse.ArgumentParser(
        description=(
            'View specific a question and/or solution from the'
            'Project Euler site (https://projecteuler.net/).'
            'Some questions may have multiple solutions, this'
            ' is because a questions may be revisited after some'
            ' thought or a new insight or library is used to attempt'
            ' the problem.'),
        prog='Project Euler')
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-s', type=str,
        required=False, default="True", choices=["True", "False"],
        dest="sol", help="Print out the solution.")
    group.add_argument(
        '-q', type=str,
        required=False, default="True", choices=["True", "False"],
        dest="que", help="Print out the question.")
    parser.add_argument(
        "question", type=int, help=("Enter the question number to view"
        " the question and/or solution."),
        choices=questions_available().keys())
    args, unknown = parser.parse_known_args()
    # Run the application
    run_question_solution(
        [args.question], boolean(args.que), boolean(args.sol))


def parse_all_questions_args():
    '''
    Parse command line arguments for outputting all questions.
    '''
    parser = argparse.ArgumentParser(
        description=(
            'View all questions and/or solutions'
            'Project Euler site (https://projecteuler.net/).'
            'Some questions may have multiple solutions, this'
            ' is because a questions may be revisited after some'
            ' thought or a new insight or library is used to attempt'
            ' the problem.'),
        prog='Project Euler')
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-s', type=str,
        required=False, default="True", choices=["True", "False"],
        dest="solutions", help="Print out the solutions.")
    group.add_argument(
        '-q', type=str,
        required=False, default="True", choices=["True", "False"],
        dest="questions", help="Print out the questions.")
    args, unknown = parser.parse_known_args()
    # Run the application
    run_question_solution(
        questions_available().keys(),
        boolean(args.questions), boolean(args.solutions))


def parse_args():
    '''
    Parse command line arguments for the application.
    '''
    parser = argparse.ArgumentParser(
        description=(
            'View questions and my solutions from the'
            'Project Euler site (https://projecteuler.net/).'
            'Some questions may have multiple solutions, this'
            ' is because a questions may be revisited after some'
            ' thought or a new insight or library is used to attempt'
            ' the problem.'),
        prog='Project Euler')
    parser.add_argument(
        'option', type=str, choices=__choices,
        help=(
            "To view options for a specific command use [option] -h."
            "The options are {0}").format(__choices))
    args, unknown = parser.parse_known_args()
    # Remove the option argument
    sys.argv.pop(1)
    if args.option == 'question':
        parse_question_args()
    elif args.option == 'all':
        parse_all_questions_args()


if __name__ == '__main__':
    '''
    Run the application
    '''
    parse_args()

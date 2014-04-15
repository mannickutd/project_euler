# -*- coding: utf-8 -*-
"""
Incorporate decorator into available function to run from command line.

Nicholas Staples
2014-04-14

"""
import sys
import copy

# List of available functions to run.
__INCLUDE = {'solutions': {}, 'questions': {}}

def include_decorator(*args, **options):
    '''
    Simple decorator to register questions and answers.
    It determines whether is a question or answer by 
    looking at the module level.
    '''
    def wrapper(f):
    	question_no = None
        try:
        	# There should be just one argument
        	# and that is the question number.
            question_no = int(args[0])
        except:
            sys.exit((
                "Each include decorator ({}) of module ({}) must include a"
                " 'question number'").format(f.__name__, f.__module__))
        module_ = f.__module__.split('.')[0]
        if module_ not in ['questions', 'solutions']:
        	sys.exit((
        		"The function module needs to be either questions or answers."))
        if module_ == "questions":
        	if question_no in __INCLUDE['questions'].keys():
        		sys.exit((
        			"The question number given has already been defined."))
        	__INCLUDE['questions'][question_no] = f
        else:
        	if question_no not in __INCLUDE['solutions']:
        		__INCLUDE['solutions'][question_no] = []
        	__INCLUDE['solutions'][question_no].append(f)
        return f
    return wrapper


def available():
    '''
    Returns a dictionary of available questions and answers
    '''
    # Return a deep copy of what is available
    return copy.deepcopy(__INCLUDE)


def questions_available():
	'''
	Returns a dictionary of available questions.
	The key is the number of the question.
	The value is a function when run will output
	the question with possible examples.
	'''
	# Return a deep copy of available questions
	return copy.deepcopy(__INCLUDE['questions'])


def solutions_available():
	'''
	Returns a dictionary of available answers.
	The key is the number of the question.
	The value is a list of functions which when run
	will output an answer to the question.
	'''
	# Return a deep copy of available questions
	return copy.deepcopy(__INCLUDE['solutions'])

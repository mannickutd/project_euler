project_euler
=============

This is the repository contains my attempted answers to the questions on https://projecteuler.net/

This my attempt at the algorithms hosted on Project Euler.
Most answers are not revisited after a suitable solution has been found. The idea is to also
study how I form my answers over time, the difference in algorithm design as you encounter
increasingly harder problems which cannot be accomplished by brute force algorithms.
After each solution is found for a problem, the forums on Project Euler are viewed to study
other answers and try and learn from the community.
On Project Euler the bench-mark is that most algorithms should be completed within a minute.
In each solution file you may find more than one solution, each solution will be run for
each problem.


Installation
-------------

The standard requirements.txt file is contained for python packages needing to be installed.
However due to use of python statistical packages eg. numpy, pandas.
To install these packages use the instructions on the page http://www.scipy.org/install.html .


Timer
------
There is a seperate timer for each function and if one minute of execution time is exceeded,
then the solution function will be aborted.


View a Problem
---------------
From the src directory:

	python main.py question <question_number> -s False


View all Problems
------------------
This will give you an idea of the questions that can be run.
From the src directory:

	python main.py all -s False


Run a Solution
---------------
From the src directory:

	# With the question printed out
	python main.py question <question_number>

	# Without the question printed out
	python main.py question <question_number> -q False


Run all Solutions
------------------
From the src directory:

	# With the questions printed out for each solution
	python main.py all

	# Without the questions printed out for each solution
	python main.py all -q False


Help
-----
From the src directory:

	python main.py -h


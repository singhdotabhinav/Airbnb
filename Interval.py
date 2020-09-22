'''
Problem 1
We wish to train a machine learning algorithm on an array of floating-point numbers in the
interval [0.0, 1.0). The data is horribly unbalanced (not evenly distributed) and we wish to
filter the dataset to obtain a subset containing an equal number of values from each interval
[0, 0.2), [0.2, 0.4), ... [0.8, 1.0), throwing away as little data as possible.
1. Write a program which reads comma-separated floating-point numbers in a single
line from stdin and prints the filtered data to stdout in the same format.
2. Provide one automated test case for your program.
Trivial example:
$ echo 0.1,0.3,0.5,0.7,0.9 | /my-program
0.1,0.3,0.5,0.7,0.9
$ echo 0.1,0.3,0.5,0.7,0.9,0.5 | /my-program
0.1,0.3,0.5,0.7,0.9
$ echo 0.3,0.5,0.7,0.9,0.5 | /my-program
None
$ echo 0.15,0.12,0.35,0.38,0.55,0.56,0.57,0.75,0.77, 0.9,0.94 | /my-program
0.15,0.12,0.35,0.38,0.55,0.56,0.75,0.77,0.9,0.94
'''
'''
Solution


'''


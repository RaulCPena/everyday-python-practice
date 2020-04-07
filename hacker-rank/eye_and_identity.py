"""
Numpy identity tool returns an identity array, which is a square matrix with all the main diagonal elements as 1 and the rest as 0. Default type of elements is float

Eye tool returns a 2-d array with 1's as the diagonal  and 0's elsewhere. The diagonal can be main, upper or lower depending on the optional parameter k. a positive k is for the ipper diagonal, a negative k is for the lower, and a 0 k(default) is for the main diagonal
"""

import numpy

print(numpy.eye(*[ int(x) for x in input().split() ]))
# an asterisk * denotes iterable unpacking so it's operand must be an iterable

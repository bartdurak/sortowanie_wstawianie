# Sortowanie przez wstawianie
# Adam Chrapkowski
# www.algorytm.org
#
# Tested with Python 3.3

from functools import reduce
from bisect import bisect_left

def insertion_sort(y):
	return reduce(lambda z, x: [z.insert(bisect_left(z, x), x), z][1], y, [])

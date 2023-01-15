# Sortowanie przez wstawianie.

from functools import reduce
from bisect import bisect_left
def insertion_sort(y):
	return reduce(lambda z, x: [z.insert(bisect_left(z, x), x), z][1], y, [])

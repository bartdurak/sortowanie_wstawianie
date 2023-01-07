# Sortowanie przez wymiane


def selection_sort(y):
	for i, n in enumerate(y):
		j, m = min(enumerate(y[i:]), key = lambda a: a[1])
		y[j + i], y[i] = n, m
	return y

#przyklad uzycia
print(selection_sort([2, 6, 1, 9, 4, 3, 7]))

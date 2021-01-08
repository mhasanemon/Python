def even_numbers(x):
	for i in xrange(x):
		if i % 2 == 0:
			yield i



even_numbers_list = list(even_numbers(10))
print(even_numbers_list)
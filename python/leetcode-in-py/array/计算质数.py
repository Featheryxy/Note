def countPrimes(n):
	"""
	:type n: int
	:rtype: int
	"""
	tem = 0
	if n == 0 or n == 1:
		return 0
	i = 2
	for i in range(2, n):
		j = 2
		for j in range(2, i):
			if (i % j == 0):
				break
		else:
			tem += 1
	return tem
	
print(countPrimes(10))

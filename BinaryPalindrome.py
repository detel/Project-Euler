numbers = []
for x in xrange(1,1000000):
	num10 = str(x)
	if num10 == num10[::-1]:
		num2 = bin(x)[2:]
		if num2 == num2[::-1]:
			numbers.append(x)

print sum(numbers)

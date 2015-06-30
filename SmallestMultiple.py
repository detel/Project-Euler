def smallest_multiple(num):

	bar = [2]
	result = 2

	for i in xrange(3,num+1):
		for multiple in bar:
			if i%multiple == 0:
				i /= multiple
		result *= i
		bar.append(i)

	return result

num = 20
print "Smallest positive number that is evenly divisible by all of the numbers from 1 to",num,"is",\
			smallest_multiple(num)

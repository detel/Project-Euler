from math import sqrt

def count_divisors(num):

	divisors = []
	SQRT = sqrt(num)

	for i in xrange(1,int(SQRT)+1):
		if i == SQRT:
			divisors.append(i)
		elif num%i == 0:
			divisors.extend([i,num/i])

	return len(divisors)

n = 1
while True:
	triangle_number = (n*(n+1))/2
	if count_divisors(triangle_number) > 500:
		print triangle_number
		break
	n += 1

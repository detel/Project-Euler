from math import sqrt

def sum_proper_divisors(num):

	divisors = [1]
	SQRT = sqrt(num)
	for i in xrange(2,int(SQRT)+1):
		if num%i == 0:
			divisors.append(num/i)
			if i not in divisors:
				divisors.append(i)
	return sum(divisors)

abundant_numbers = []
for i in xrange(12,28124):
	if sum_proper_divisors(i) > i:
		abundant_numbers.append(i)

sigma = []
for i in abundant_numbers:
	for j in abundant_numbers:
		if i+j < 28124:
			sigma.append(i+j)
print sum(list(set(xrange(28124))-set(sigma)))

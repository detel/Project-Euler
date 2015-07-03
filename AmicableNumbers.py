from math import sqrt

def sum_proper_divisors(num):

	divisors = [1]
	SQRT = sqrt(num)
	for i in xrange(2,int(SQRT)+1):
		if num%i == 0:# and i not in divisors:
			divisors.append(num/i)
			if i not in divisors:
				divisors.append(i)

	return sum(divisors)

sum_divisors = [-1]
for i in xrange(1,10000):
	sum_divisors.append(sum_proper_divisors(i))

amicable_numbers = []
for i in xrange(2,10000):
	if i != sum_divisors[i]:
		if sum_divisors[i] < 10000:
			if sum_divisors[sum_divisors[i]] == i:
				amicable_numbers.append(i)

print sum(amicable_numbers)

import math

def get_digits(num):
	digits = []

	while num:
		digits.append(num%10)
		num /= 10

	return digits
final = []
for i in xrange(10,50000):
	s = 0
	for j in get_digits(i):
		s += math.factorial(j)
	if s == i:
		final.append(i)

print final
print sum(final)

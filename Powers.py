fifth_power = [i**5 for i in range(10)]

def get_digits(num):
	digits = []

	while num:
		digits.append(num%10)
		num /= 10

	return digits

final = []
for i in xrange(10,1000000):
	numbers = get_digits(i)
	s = 0
	for n in numbers:
		s += fifth_power[n]
	if s == i:
		final.append(i)

print final
print sum(final)

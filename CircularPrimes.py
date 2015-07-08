cyclic = []
def getDigits(num):
	digits = []

	while num:
		digits.append(str(num%10))
		num /= 10

	return digits
	
def sprimes():
	primes = []
	permutations = []
	isPrime = [True for i in xrange(1000000)]
	isPrime[0],isPrime[1] = False,False

	for i in xrange(1001):
		if isPrime[i]:
			for j in xrange(i*i,1000000,i):
				isPrime[j] = False

	for i in xrange(1000000):
		if isPrime[i]:
			dig = getDigits(i)
			if '2' in dig or '4' in dig or '5' in dig or '6' in dig or '8' in dig or '0' in dig:
				pass
			else:
				no = []
				for x in xrange(len(dig)):
					no.append(int(''.join(dig[x:]+dig[:x])))
				cyclic.append(no)
				primes.append(i)

	return primes

special_primes = sprimes()
final = set()
final.add(2)
final.add(5)
for numb in cyclic:
	found = True
	for no in numb:
		if no not in special_primes:
			found = False
	if found:
		final.update(numb)

print len(sorted(list(final)))

from math import sqrt

primes = []
TWO_MILLION = 2000000

def get_primes(num):

	is_prime = [True]*(num+1)
	is_prime[0] = False
	is_prime[1] = False

	for i in xrange(2,int(sqrt(num))+1):
		if is_prime[i]:
			for j in xrange(i*i,num+1,i):
				is_prime[j] = False

	for i in xrange(len(is_prime)):
		if is_prime[i]:
			primes.append(i)

	return sum(primes)

print get_primes(TWO_MILLION)

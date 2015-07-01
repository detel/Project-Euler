def collatz_sequence(num):

	i = 1
	while num != 1:
		if num%2 == 0:
			num /= 2
		else:
			num = 3*num+1
		i += 1

	return i

longest = 1
for x in xrange(1,1000000):
	chain_length = collatz_sequence(x)
	#print x,chain_length
	if longest < chain_length:
		longest = chain_length
		num = x
print num

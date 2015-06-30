from math import sqrt

def largest_prime_factor(num):
	
	if num <= 3:
		return num
	
	if num%2 == 0:
		temp = largest_prime_factor(num/2)
		if temp == num/2:
			return num/2
		else:
			return temp

	if num%3 == 0:
		temp = largest_prime_factor(num/3)
		if temp == num/3:
			return num/3
		else:
			return temp

	for i in xrange(5,int(sqrt(num))+1,6):
		if num%i == 0:
			temp = largest_prime_factor(num/i)
			if temp == num/i:
				return num/i
			else:
				return temp
		if num%(i+2) == 0:
			temp = largest_prime_factor(num/(i+2))
			if temp == num/(i+2):
				return num/(i+2)
			else:
				return temp

	return num

print largest_prime_factor(600851475143)

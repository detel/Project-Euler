NUM = 2**1000
result = 0

while NUM != 0:
	result += NUM%10
	NUM /= 10

print result

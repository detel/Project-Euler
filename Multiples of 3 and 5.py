def sum(num):
	terms = 999/num
	first = num
	last = 999 - 999%num

	return (terms*(first+last))/2

print sum(3)+sum(5)-sum(15)

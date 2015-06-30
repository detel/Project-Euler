def largest_palindrome(min,max):

	foo = [0,min,min]

	for i in xrange(min,max+1):
		for j in xrange(min,max+1):
			num = i*j
			if str(num) == str(num)[::-1]:
				if num > foo[0]:
					foo = num,i,j

	return foo

#print largest_palindrome(100,999)
min,max = 100,999
foo = largest_palindrome(min,max)

print "Largest palindrome between",min,"and",max,"is",foo[0],"=",foo[1],"*",foo[2]

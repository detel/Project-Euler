# Project-Euler
#https://projecteuler.net/

fib = [1,2]
fibo_sum = 2

while True:
	term = fib[-1]+fib[-2]
	if term >= 4000000:
		break
	fib.append(term)
	if term%2 == 0:
		fibo_sum += term

print fibo_sum

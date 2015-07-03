fibo = [1,1]
i = 2

while True:
	fibo.append(fibo[i-1] + fibo[i-2])
	if len(str(fibo[i])) == 1000:
		print i+1
		break
	i += 1 

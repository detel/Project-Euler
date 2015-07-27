is_prime = [True for _ in xrange(22500)]
primes = []
prev_n = 0

for i in xrange(2,150):
        if is_prime[i]:
                for j in xrange(i*i,22500,i):
                        is_prime[j] = False
                primes.append(i)

for i in xrange(150,1000):
        if is_prime[i]:
                primes.append(i)

for a in xrange(-999,1000,2):
        for b in primes:
                f = lambda m: m*m + a*m + b
                n = 0
                while is_prime[abs(f(n))]:
                        n += 1
                if n > prev_n:
                        result = a*b
                        prev_n = n
        
print result                      

def get_primes(n):
    
    sieve = [True] * (n/2)

    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

def longest_recurring_cycle(n):
        primes = get_primes(n)[::-1]
        for d in primes:
                period = 1
                while pow(10, period, d) != 1:
                        period += 1
                if d-1 == period:
                        break
        return d

print longest_recurring_cycle(1000)
